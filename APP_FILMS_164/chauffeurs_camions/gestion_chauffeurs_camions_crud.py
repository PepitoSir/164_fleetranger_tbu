from pathlib import Path
from APP_FILMS_164 import app  # Assurez-vous que ceci est correct
from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.chauffeurs_camions.gestion_chauffeurs_camions_wtf_forms import FormWTFAjouterChauffeursCamions, FormWTFDeleteChauffeurCamions, FormWTFUpdateChauffeurCamions

bp = Blueprint('gestion_chauffeurs_camions', __name__)

@bp.route("/chauffeurs_camions_afficher/<string:order_by>/<int:id_chauffeur_sel>", methods=['GET', 'POST'])
def chauffeurs_camions_afficher(order_by, id_chauffeur_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_chauffeur_sel == 0:
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, Camion.Id_camion, Camion.Marque, Camion.Modele
                                                            FROM Chauffeur
                                                            INNER JOIN Camion ON Chauffeur.Id_camion = Camion.Id_camion
                                                            ORDER BY Chauffeur.Id_Chauffeur ASC"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher)
                elif order_by == "ASC":
                    valeur_id_chauffeur_selected_dictionnaire = {"value_id_chauffeur_selected": id_chauffeur_sel}
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, Camion.Id_camion, Camion.Marque, Camion.Modele
                                                            FROM Chauffeur
                                                            INNER JOIN Camion ON Chauffeur.Id_camion = Camion.Id_camion
                                                            WHERE Chauffeur.Id_Chauffeur = %(value_id_chauffeur_selected)s
                                                            ORDER BY Chauffeur.Id_Chauffeur ASC"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher, valeur_id_chauffeur_selected_dictionnaire)
                else:
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, Camion.Id_camion, Camion.Marque, Camion.Modele
                                                            FROM Chauffeur
                                                            INNER JOIN Camion ON Chauffeur.Id_camion = Camion.Id_camion
                                                            ORDER BY Chauffeur.Id_Chauffeur DESC"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher)

                data_chauffeurs_camions = mc_afficher.fetchall()

                if not data_chauffeurs_camions and id_chauffeur_sel == 0:
                    flash("""La table "Chauffeur" est vide !!""", "warning")
                elif not data_chauffeurs_camions and id_chauffeur_sel > 0:
                    flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données chauffeurs et camions affichées !!", "success")

        except Exception as e:
            raise ExceptionChauffeursCamionsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                                     f"{chauffeurs_camions_afficher.__name__} ; "
                                                     f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeurs_camions_afficher.html", data=data_chauffeurs_camions)




@app.route("/chauffeurs_camions_ajouter", methods=['GET', 'POST'])
def chauffeurs_camions_ajouter_wtf():
    form = FormWTFAjouterChauffeursCamions()
    try:
        with DBconnection() as db:
            strsql_select_camions = "SELECT Id_camion, Marque, Modele FROM camion"
            db.execute(strsql_select_camions)
            camions = db.fetchall()
            form.id_camion_wtf.choices = [(camion['Id_camion'], f"{camion['Marque']} {camion['Modele']}") for camion in camions]

        if form.validate_on_submit():
            nom = form.nom_wtf.data
            prenom = form.prenom_wtf.data
            categorie_permis = form.categorie_permis_wtf.data
            date_engagement = form.date_engagement_wtf.data
            id_camion = form.id_camion_wtf.data

            valeurs_insertion_dictionnaire = {
                "nom": nom,
                "prenom": prenom,
                "categorie_permis": categorie_permis,
                "date_engagement": date_engagement,
                "id_camion": id_camion
            }

            strsql_insert_chauffeur_camion = """INSERT INTO Chauffeur (Nom, Prénom, CategoriePermis, DateEngagement, Id_camion) 
                                              VALUES (%(nom)s, %(prenom)s, %(categorie_permis)s, %(date_engagement)s, %(id_camion)s)"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(strsql_insert_chauffeur_camion, valeurs_insertion_dictionnaire)

            flash(f"Données insérées !!", "success")
            return redirect(url_for('chauffeurs_camions_afficher', order_by='ASC', id_chauffeur_sel=0))

    except Exception as e:
        raise ExceptionChauffeursAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                             f"{chauffeurs_camions_ajouter_wtf.__name__} ; "
                                             f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeurs_camions_ajouter_wtf.html", form=form)


@app.route("/chauffeur_camion_update/<int:id_chauffeur_update>", methods=['GET', 'POST'])
def chauffeur_camion_update_wtf(id_chauffeur_update):
    form_update = FormWTFUpdateChauffeurCamion()
    try:
        if request.method == "POST" and form_update.validate_on_submit():
            nom = form_update.nom_update_wtf.data
            prenom = form_update.prenom_update_wtf.data
            categorie_permis = form_update.categorie_permis_update_wtf.data
            date_engagement = form_update.date_engagement_update_wtf.data
            id_camion = form_update.id_camion_update_wtf.data

            valeur_update_dictionnaire = {
                "id_chauffeur": id_chauffeur_update,
                "nom": nom,
                "prenom": prenom,
                "categorie_permis": categorie_permis,
                "date_engagement": date_engagement,
                "id_camion": id_camion
            }

            str_sql_update_chauffeur_camion = """UPDATE Chauffeur SET Nom = %(nom)s, Prénom = %(prenom)s, CategoriePermis = %(categorie_permis)s, 
                                               DateEngagement = %(date_engagement)s, Id_camion = %(id_camion)s WHERE Id_Chauffeur = %(id_chauffeur)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_chauffeur_camion, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            return redirect(url_for('chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_sel=id_chauffeur_update))

        elif request.method == "GET":
            str_sql_id_chauffeur_camion = "SELECT Id_Chauffeur, Nom, Prénom, CategoriePermis, DateEngagement, Id_camion FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur)s"
            valeur_select_dictionnaire = {"value_id_chauffeur": id_chauffeur_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_chauffeur_camion, valeur_select_dictionnaire)
                data_nom_chauffeur_camion = mybd_conn.fetchone()

            if data_nom_chauffeur_camion:
                form_update.nom_update_wtf.data = data_nom_chauffeur_camion["Nom"]
                form_update.prenom_update_wtf.data = data_nom_chauffeur_camion["Prénom"]
                form_update.categorie_permis_update_wtf.data = data_nom_chauffeur_camion["CategoriePermis"]
                form_update.date_engagement_update_wtf.data = data_nom_chauffeur_camion["DateEngagement"]
                form_update.id_camion_update_wtf.data = data_nom_chauffeur_camion["Id_camion"]

                with DBconnection() as db:
                    strsql_select_camions = "SELECT Id_camion, Marque, Modele FROM camion"
                    db.execute(strsql_select_camions)
                    camions = db.fetchall()
                    form_update.id_camion_update_wtf.choices = [(camion['Id_camion'], f"{camion['Marque']} {camion['Modele']}") for camion in camions]
            else:
                flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                return redirect(url_for('gestion_chauffeurs_camions.chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_sel=0))

    except Exception as e:
        raise ExceptionChauffeurCamionsUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                                f"{chauffeur_camion_update_wtf.__name__} ; "
                                                f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeur_camion_update_wtf.html", form_update=form_update, id_chauffeur_update=id_chauffeur_update)


@app.route("/chauffeur_camion_delete/<int:id_chauffeur_delete>", methods=['GET', 'POST'])
def chauffeur_camion_delete_wtf(id_chauffeur_delete):
    form_delete = FormWTFDeleteChauffeurCamion()
    data_chauffeurs_associes = None
    btn_submit_del = None

    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("gestion_chauffeurs_camions.chauffeurs_camions_afficher", order_by="ASC", id_chauffeur_sel=0))

            if form_delete.submit_btn_conf_del.data:
                data_chauffeurs_associes = session.get('data_chauffeurs_associes', None)
                flash(f"Effacer le chauffeur de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_chauffeur": id_chauffeur_delete}

                str_sql_delete_chauffeur_camion = """DELETE FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_chauffeur_camion, valeur_delete_dictionnaire)

                flash(f"Chauffeur définitivement effacé !!", "success")
                return redirect(url_for('gestion_chauffeurs_camions.chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_chauffeur": id_chauffeur_delete}

            str_sql_chauffeurs_associes = """SELECT camion.Id_camion, camion.Marque, camion.Modele FROM camion
                                             WHERE Id_camion IN (SELECT Id_camion FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur)s)"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_chauffeurs_associes, valeur_select_dictionnaire)
                data_chauffeurs_associes = mydb_conn.fetchall()
                session['data_chauffeurs_associes'] = data_chauffeurs_associes

                str_sql_id_chauffeur = "SELECT Id_Chauffeur, Nom FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur)s"
                mydb_conn.execute(str_sql_id_chauffeur, valeur_select_dictionnaire)
                data_nom_chauffeur = mydb_conn.fetchone()

                if data_nom_chauffeur:
                    form_delete.nom_chauffeur_delete_wtf.data = data_nom_chauffeur["Nom"]
                else:
                    flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                    return redirect(url_for('gestion_chauffeurs_camions.chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_sel=0))

            btn_submit_del = False

    except Exception as e:
        raise ExceptionChauffeurCamionsDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                                f"{chauffeur_camion_delete_wtf.__name__} ; "
                                                f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeur_camion_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_chauffeurs_associes=data_chauffeurs_associes,
                           id_chauffeur=id_chauffeur_delete)
