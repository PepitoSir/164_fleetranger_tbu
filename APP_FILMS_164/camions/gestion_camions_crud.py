"""Gestion des "routes" FLASK et des données pour les genres.
Fichier : gestion_genres_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFAjouterGenres
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFDeleteGenre
from APP_FILMS_164.genres.gestion_genres_wtf_forms import FormWTFUpdateGenre

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /camions_afficher
    
    Test : ex : http://127.0.0.1:5575/camions_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_camion_sel = 0 >> tous les genres.
                id_camion_sel = "n" affiche le camion dont l'id est "n"
"""


@app.route("/camions_afficher/<string:order_by>/<int:id_camion_sel>", methods=['GET', 'POST'])
def camions_afficher(order_by, id_camion_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_camion_sel == 0:
                    strsql_camions_afficher = """SELECT * FROM Assurance"""
                    mc_afficher.execute(strsql_camions_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_camion"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du camion sélectionné avec un nom de variable
                    valeur_id_camion_selected_dictionnaire = {"value_id_camion_selected": id_camion_sel}
                    strsql_camions_afficher = """SELECT * FROM Assurance"""

                    mc_afficher.execute(strsql_camions_afficher, valeur_id_camion_selected_dictionnaire)
                else:
                    strsql_camions_afficher = """SELECT * FROM Assurance"""

                    mc_afficher.execute(strsql_camions_afficher)

                data_camions = mc_afficher.fetchall()

                print("data_camions ", data_camions, " Type : ", type(data_camions))

                # Différencier les messages si la table est vide.
                if not data_camions and id_camion_sel == 0:
                    flash("""La table "t_camion" est vide. !!""", "warning")
                elif not data_camions and id_camion_sel > 0:
                    # Si l'utilisateur change l'id_camion dans l'URL et que le camion n'existe pas,
                    flash(f"Le camion demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_camion" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données camions affichés !!", "success")

        except Exception as Exception_camions_afficher:
            raise ExceptionCamionsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{camions_afficher.__name__} ; "
                                          f"{Exception_camions_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("camions/camions_afficher.html", data=data_camions)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /camions_ajouter
    
    Test : ex : http://127.0.0.1:5575/camions_ajouter
    
    Paramètres : sans
    
    But : Ajouter un camion pour un film
    
    Remarque :  Dans le champ "name_camion_html" du formulaire "camions/camions_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/camions_ajouter", methods=['GET', 'POST'])
def camions_ajouter_wtf():
    form = FormWTFAjouterCamions()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_camion_wtf = form.nom_camion_wtf.data
                name_camion = name_camion_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_camion": name_camion}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_camion = """INSERT INTO t_camion (id_camion,intitule_camion) VALUES (NULL,%(value_intitule_camion)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_camion, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('camions_afficher', order_by='DESC', id_camion_sel=0))

        except Exception as Exception_camions_ajouter_wtf:
            raise ExceptionCamionsAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{camions_ajouter_wtf.__name__} ; "
                                            f"{Exception_camions_ajouter_wtf}")

    return render_template("camions/camions_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /camion_update
    
    Test : ex cliquer sur le menu "camions" puis cliquer sur le bouton "EDIT" d'un "camion"
    
    Paramètres : sans
    
    But : Editer(update) un camion qui a été sélectionné dans le formulaire "camions_afficher.html"
    
    Remarque :  Dans le champ "nom_camion_update_wtf" du formulaire "camions/camion_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/camion_update", methods=['GET', 'POST'])
def camion_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "camion"
    id_camion_update = request.values['id_camion_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateCamion()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "camion_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_camion_update = form_update.nom_camion_update_wtf.data
            name_camion_update = name_camion_update.lower()
            date_camion_essai = form_update.date_camion_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_camion": id_camion_update,
                                          "value_name_camion": name_camion_update,
                                          "value_date_camion_essai": date_camion_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulecamion = """UPDATE t_camion SET intitule_camion = %(value_name_camion)s, 
            date_ins_camion = %(value_date_camion_essai)s WHERE id_camion = %(value_id_camion)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulecamion, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_camion_update"
            return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=id_camion_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_camion" et "intitule_camion" de la "t_camion"
            str_sql_id_camion = "SELECT id_camion, intitule_camion, date_ins_camion FROM t_camion " \
                               "WHERE id_camion = %(value_id_camion)s"
            valeur_select_dictionnaire = {"value_id_camion": id_camion_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_camion, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom camion" pour l'UPDATE
            data_nom_camion = mybd_conn.fetchone()
            print("data_nom_camion ", data_nom_camion, " type ", type(data_nom_camion), " camion ",
                  data_nom_camion["intitule_camion"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "camion_update_wtf.html"
            form_update.nom_camion_update_wtf.data = data_nom_camion["intitule_camion"]
            form_update.date_camion_wtf_essai.data = data_nom_camion["date_ins_camion"]

    except Exception as Exception_camion_update_wtf:
        raise ExceptionCamionUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{camion_update_wtf.__name__} ; "
                                      f"{Exception_camion_update_wtf}")

    return render_template("camions/camion_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /camion_delete
    
    Test : ex. cliquer sur le menu "camions" puis cliquer sur le bouton "DELETE" d'un "camion"
    
    Paramètres : sans
    
    But : Effacer(delete) un camion qui a été sélectionné dans le formulaire "camions_afficher.html"
    
    Remarque :  Dans le champ "nom_camion_delete_wtf" du formulaire "camions/camion_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/camion_delete", methods=['GET', 'POST'])
def camion_delete_wtf():
    data_films_attribue_camion_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_camion"
    id_camion_delete = request.values['id_camion_btn_delete_html']

    # Objet formulaire pour effacer le camion sélectionné.
    form_delete = FormWTFDeleteCamion()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("camions_afficher", order_by="ASC", id_camion_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "camions/camion_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_camion_delete = session['data_films_attribue_camion_delete']
                print("data_films_attribue_camion_delete ", data_films_attribue_camion_delete)

                flash(f"Effacer le camion de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer camion" qui va irrémédiablement EFFACER le camion
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_camion": id_camion_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_camion = """DELETE FROM t_camion_film WHERE fk_camion = %(value_id_camion)s"""
                str_sql_delete_idcamion = """DELETE FROM t_camion WHERE id_camion = %(value_id_camion)s"""
                # Manière brutale d'effacer d'abord la "fk_camion", même si elle n'existe pas dans la "t_camion_film"
                # Ensuite on peut effacer le camion vu qu'il n'est plus "lié" (INNODB) dans la "t_camion_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_camion, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idcamion, valeur_delete_dictionnaire)

                flash(f"camion définitivement effacé !!", "success")
                print(f"camion définitivement effacé !!")

                # afficher les données
                return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_camion": id_camion_delete}
            print(id_camion_delete, type(id_camion_delete))

            # Requête qui affiche tous les films_camions qui ont le camion que l'utilisateur veut effacer
            str_sql_camions_films_delete = """SELECT id_camion_film, nom_film, id_camion, intitule_camion FROM t_camion_film 
                                            INNER JOIN t_film ON t_camion_film.fk_film = t_film.id_film
                                            INNER JOIN t_camion ON t_camion_film.fk_camion = t_camion.id_camion
                                            WHERE fk_camion = %(value_id_camion)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_camions_films_delete, valeur_select_dictionnaire)
                data_films_attribue_camion_delete = mydb_conn.fetchall()
                print("data_films_attribue_camion_delete...", data_films_attribue_camion_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "camions/camion_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_camion_delete'] = data_films_attribue_camion_delete

                # Opération sur la BD pour récupérer "id_camion" et "intitule_camion" de la "t_camion"
                str_sql_id_camion = "SELECT id_camion, intitule_camion FROM t_camion WHERE id_camion = %(value_id_camion)s"

                mydb_conn.execute(str_sql_id_camion, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom camion" pour l'action DELETE
                data_nom_camion = mydb_conn.fetchone()
                print("data_nom_camion ", data_nom_camion, " type ", type(data_nom_camion), " camion ",
                      data_nom_camion["intitule_camion"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "camion_delete_wtf.html"
            form_delete.nom_camion_delete_wtf.data = data_nom_camion["intitule_camion"]

            # Le bouton pour l'action "DELETE" dans le form. "camion_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_camion_delete_wtf:
        raise ExceptionCamionDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{camion_delete_wtf.__name__} ; "
                                      f"{Exception_camion_delete_wtf}")

    return render_template("camions/camion_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_camion_delete)
