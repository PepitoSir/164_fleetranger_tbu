"""Gestion des "routes" FLASK et des données pour les mails.
Fichier : gestion_mails_crud.py
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
from APP_FILMS_164.mails.gestion_mails_wtf_forms import FormWTFAjoutermails
from APP_FILMS_164.mails.gestion_mails_wtf_forms import FormWTFDeletemails
from APP_FILMS_164.mails.gestion_mails_wtf_forms import FormWTFUpdatemails

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /mails_afficher
    
    Test : ex : http://127.0.0.1:5575/mails_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_mails_sel = 0 >> tous les mails.
                id_mails_sel = "n" affiche le mails dont l'id est "n"
"""


@app.route("/mails_afficher/<string:order_by>/<int:id_mails_sel>", methods=['GET', 'POST'])
def mails_afficher(order_by, id_mails_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_mails_sel == 0:
                    strsql_mails_afficher = """SELECT * FROM Assurance"""
                    mc_afficher.execute(strsql_mails_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_mails"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du mails sélectionné avec un nom de variable
                    valeur_id_mails_selected_dictionnaire = {"value_id_mails_selected": id_mails_sel}
                    strsql_mails_afficher = """SELECT * FROM Assurance"""

                    mc_afficher.execute(strsql_mails_afficher, valeur_id_mails_selected_dictionnaire)
                else:
                    strsql_mails_afficher = """SELECT * FROM Assurance"""

                    mc_afficher.execute(strsql_mails_afficher)

                data_mails = mc_afficher.fetchall()

                print("data_mails ", data_mails, " Type : ", type(data_mails))

                # Différencier les messages si la table est vide.
                if not data_mails and id_mails_sel == 0:
                    flash("""La table "t_mails" est vide. !!""", "warning")
                elif not data_mails and id_mails_sel > 0:
                    # Si l'utilisateur change l'id_mails dans l'URL et que le mails n'existe pas,
                    flash(f"Le mails demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_mails" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données mails affichés !!", "success")

        except Exception as Exception_mails_afficher:
            raise ExceptionmailsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{mails_afficher.__name__} ; "
                                          f"{Exception_mails_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("mails/mails_afficher.html", data=data_mails)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /mails_ajouter
    
    Test : ex : http://127.0.0.1:5575/mails_ajouter
    
    Paramètres : sans
    
    But : Ajouter un mails pour un film
    
    Remarque :  Dans le champ "name_mails_html" du formulaire "mails/mails_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/mails_ajouter", methods=['GET', 'POST'])
def mails_ajouter_wtf():
    form = FormWTFAjoutermails()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                name_mails_wtf = form.nom_mails_wtf.data
                name_mails = name_mails_wtf.lower()
                valeurs_insertion_dictionnaire = {"value_intitule_mails": name_mails}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_mails = """INSERT INTO t_mails (id_mails,intitule_mails) VALUES (NULL,%(value_intitule_mails)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_mails, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('mails_afficher', order_by='DESC', id_mails_sel=0))

        except Exception as Exception_mails_ajouter_wtf:
            raise ExceptionmailsAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{mails_ajouter_wtf.__name__} ; "
                                            f"{Exception_mails_ajouter_wtf}")

    return render_template("mails/mails_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /mails_update
    
    Test : ex cliquer sur le menu "mails" puis cliquer sur le bouton "EDIT" d'un "mails"
    
    Paramètres : sans
    
    But : Editer(update) un mails qui a été sélectionné dans le formulaire "mails_afficher.html"
    
    Remarque :  Dans le champ "nom_mails_update_wtf" du formulaire "mails/mails_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/mails_update", methods=['GET', 'POST'])
def mails_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_mails"
    id_mails_update = request.values['id_mails_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatemails()
    try:
        # 2023.05.14 OM S'il y a des listes déroulantes dans le formulaire
        # La validation pose quelques problèmes
        if request.method == "POST" and form_update.submit.data:
            # Récupèrer la valeur du champ depuis "mails_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            name_mails_update = form_update.nom_mails_update_wtf.data
            name_mails_update = name_mails_update.lower()
            date_mails_essai = form_update.date_mails_wtf_essai.data

            valeur_update_dictionnaire = {"value_id_mails": id_mails_update,
                                          "value_name_mails": name_mails_update,
                                          "value_date_mails_essai": date_mails_essai
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_intitulemails = """UPDATE t_mails SET intitule_mails = %(value_name_mails)s, 
            date_ins_mails = %(value_date_mails_essai)s WHERE id_mails = %(value_id_mails)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_intitulemails, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_mails_update"
            return redirect(url_for('mails_afficher', order_by="ASC", id_mails_sel=id_mails_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_mails" et "intitule_mails" de la "t_mails"
            str_sql_id_mails = "SELECT id_mails, intitule_mails, date_ins_mails FROM t_mails " \
                               "WHERE id_mails = %(value_id_mails)s"
            valeur_select_dictionnaire = {"value_id_mails": id_mails_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_mails, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom mails" pour l'UPDATE
            data_nom_mails = mybd_conn.fetchone()
            print("data_nom_mails ", data_nom_mails, " type ", type(data_nom_mails), " mails ",
                  data_nom_mails["intitule_mails"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "mails_update_wtf.html"
            form_update.nom_mails_update_wtf.data = data_nom_mails["intitule_mails"]
            form_update.date_mails_wtf_essai.data = data_nom_mails["date_ins_mails"]

    except Exception as Exception_mails_update_wtf:
        raise ExceptionmailsUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mails_update_wtf.__name__} ; "
                                      f"{Exception_mails_update_wtf}")

    return render_template("mails/mails_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /mails_delete
    
    Test : ex. cliquer sur le menu "mails" puis cliquer sur le bouton "DELETE" d'un "mails"
    
    Paramètres : sans
    
    But : Effacer(delete) un mails qui a été sélectionné dans le formulaire "mails_afficher.html"
    
    Remarque :  Dans le champ "nom_mails_delete_wtf" du formulaire "mails/mails_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/mails_delete", methods=['GET', 'POST'])
def mails_delete_wtf():
    data_films_attribue_mails_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_mails"
    id_mails_delete = request.values['id_mails_btn_delete_html']

    # Objet formulaire pour effacer le mails sélectionné.
    form_delete = FormWTFDeletemails()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("mails_afficher", order_by="ASC", id_mails_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "mails/mails_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_films_attribue_mails_delete = session['data_films_attribue_mails_delete']
                print("data_films_attribue_mails_delete ", data_films_attribue_mails_delete)

                flash(f"Effacer le mails de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer mails" qui va irrémédiablement EFFACER le mails
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_mails": id_mails_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_films_mails = """DELETE FROM t_mails_film WHERE fk_mails = %(value_id_mails)s"""
                str_sql_delete_idmails = """DELETE FROM t_mails WHERE id_mails = %(value_id_mails)s"""
                # Manière brutale d'effacer d'abord la "fk_mails", même si elle n'existe pas dans la "t_mails_film"
                # Ensuite on peut effacer le mails vu qu'il n'est plus "lié" (INNODB) dans la "t_mails_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_films_mails, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idmails, valeur_delete_dictionnaire)

                flash(f"mails définitivement effacé !!", "success")
                print(f"mails définitivement effacé !!")

                # afficher les données
                return redirect(url_for('mails_afficher', order_by="ASC", id_mails_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_mails": id_mails_delete}
            print(id_mails_delete, type(id_mails_delete))

            # Requête qui affiche tous les films_mails qui ont le mails que l'utilisateur veut effacer
            str_sql_mails_films_delete = """SELECT id_mails_film, nom_film, id_mails, intitule_mails FROM t_mails_film 
                                            INNER JOIN t_film ON t_mails_film.fk_film = t_film.id_film
                                            INNER JOIN t_mails ON t_mails_film.fk_mails = t_mails.id_mails
                                            WHERE fk_mails = %(value_id_mails)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_mails_films_delete, valeur_select_dictionnaire)
                data_films_attribue_mails_delete = mydb_conn.fetchall()
                print("data_films_attribue_mails_delete...", data_films_attribue_mails_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "mails/mails_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_films_attribue_mails_delete'] = data_films_attribue_mails_delete

                # Opération sur la BD pour récupérer "id_mails" et "intitule_mails" de la "t_mails"
                str_sql_id_mails = "SELECT id_mails, intitule_mails FROM t_mails WHERE id_mails = %(value_id_mails)s"

                mydb_conn.execute(str_sql_id_mails, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom mails" pour l'action DELETE
                data_nom_mails = mydb_conn.fetchone()
                print("data_nom_mails ", data_nom_mails, " type ", type(data_nom_mails), " mails ",
                      data_nom_mails["intitule_mails"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "mails_delete_wtf.html"
            form_delete.nom_mails_delete_wtf.data = data_nom_mails["intitule_mails"]

            # Le bouton pour l'action "DELETE" dans le form. "mails_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_mails_delete_wtf:
        raise ExceptionmailsDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{mails_delete_wtf.__name__} ; "
                                      f"{Exception_mails_delete_wtf}")

    return render_template("mails/mails_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_films_associes=data_films_attribue_mails_delete)
