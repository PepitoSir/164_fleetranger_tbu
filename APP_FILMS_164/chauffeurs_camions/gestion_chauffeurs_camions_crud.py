from pathlib import Path
from flask import redirect, request, session, url_for, flash, render_template
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import ExceptionChauffeursAfficher, ExceptionChauffeursAjouterWtf, \
    ExceptionChauffeurUpdateWtf, ExceptionChauffeurDeleteWtf
from APP_FILMS_164.chauffeurs_camions.gestion_chauffeurs_camions_wtf_forms import FormWTFAjouterChauffeursCamions, \
    FormWTFDeleteChauffeurCamion, FormWTFUpdateChauffeurCamion


@app.route("/chauffeurs_camions_afficher/<string:order_by>/<int:id_chauffeur_camion_sel>", methods=['GET', 'POST'])
def chauffeurs_camions_afficher(order_by, id_chauffeur_camion_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_chauffeur_camion_sel == 0:
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, 
                                                                Chauffeur.CategoriePermis, Chauffeur.DateEngagement, 
                                                                camion.Marque, camion.Modele
                                                             FROM Chauffeur
                                                             JOIN camion ON Chauffeur.Id_camion = camion.Id_camion
                                                             ORDER BY Chauffeur.Id_Chauffeur ASC"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher)
                elif order_by == "ASC":
                    valeur_id_chauffeur_camion_selected_dictionnaire = {
                        "value_id_chauffeur_camion_selected": id_chauffeur_camion_sel}
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, 
                                                                Chauffeur.CategoriePermis, Chauffeur.DateEngagement, 
                                                                camion.Marque, camion.Modele
                                                             FROM Chauffeur
                                                             JOIN camion ON Chauffeur.Id_camion = camion.Id_camion
                                                             WHERE Chauffeur.Id_Chauffeur = %(value_id_chauffeur_camion_selected)s"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher,
                                        valeur_id_chauffeur_camion_selected_dictionnaire)
                else:
                    strsql_chauffeurs_camions_afficher = """SELECT Chauffeur.Id_Chauffeur, Chauffeur.Nom, Chauffeur.Prénom, 
                                                                Chauffeur.CategoriePermis, Chauffeur.DateEngagement, 
                                                                camion.Marque, camion.Modele
                                                             FROM Chauffeur
                                                             JOIN camion ON Chauffeur.Id_camion = camion.Id_camion
                                                             ORDER BY Chauffeur.Id_Chauffeur DESC"""
                    mc_afficher.execute(strsql_chauffeurs_camions_afficher)

                data_chauffeurs_camions = mc_afficher.fetchall()

                if not data_chauffeurs_camions and id_chauffeur_camion_sel == 0:
                    flash("""La table "Chauffeur" est vide !!""", "warning")
                elif not data_chauffeurs_camions and id_chauffeur_camion_sel > 0:
                    flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données chauffeurs affichées !!", "success")

        except Exception as e:
            raise ExceptionChauffeursAfficher(f"fichier : {Path(__file__).name}  ;  "
                                              f"{chauffeurs_camions_afficher.__name__} ; "
                                              f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeurs_camions_afficher.html", data=data_chauffeurs_camions)


@app.route("/chauffeurs_camions_ajouter", methods=['GET', 'POST'])
def chauffeurs_camions_ajouter_wtf():
    form = FormWTFAjouterChauffeursCamions()
    if request.method == "POST":
        try:
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
                return redirect(url_for('chauffeurs_camions_afficher', order_by='ASC', id_chauffeur_camion_sel=0))

        except Exception as e:
            raise ExceptionChauffeursAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                                f"{chauffeurs_camions_ajouter_wtf.__name__} ; "
                                                f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeurs_camions_ajouter_wtf.html", form=form)


@app.route("/chauffeur_camion_update/<int:id_chauffeur_camion_update>", methods=['GET', 'POST'])
def chauffeur_camion_update_wtf(id_chauffeur_camion_update):
    form_update = FormWTFUpdateChauffeurCamion()
    try:
        if request.method == "POST" and form_update.validate_on_submit():
            nom = form_update.nom_update_wtf.data
            prenom = form_update.prenom_update_wtf.data
            categorie_permis = form_update.categorie_permis_update_wtf.data
            date_engagement = form_update.date_engagement_update_wtf.data
            id_camion = form_update.id_camion_update_wtf.data

            valeur_update_dictionnaire = {
                "id_chauffeur": id_chauffeur_camion_update,
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
            return redirect(url_for('chauffeurs_camions_afficher', order_by="ASC",
                                    id_chauffeur_camion_sel=id_chauffeur_camion_update))

        elif request.method == "GET":
            str_sql_id_chauffeur_camion = "SELECT Id_Chauffeur, Nom, Prénom, CategoriePermis, DateEngagement, Id_camion FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur_camion)s"
            valeur_select_dictionnaire = {"value_id_chauffeur_camion": id_chauffeur_camion_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_chauffeur_camion, valeur_select_dictionnaire)
                data_nom_chauffeur_camion = mybd_conn.fetchone()

            if data_nom_chauffeur_camion:
                form_update.nom_update_wtf.data = data_nom_chauffeur_camion["Nom"]
                form_update.prenom_update_wtf.data = data_nom_chauffeur_camion["Prénom"]
                form_update.categorie_permis_update_wtf.data = data_nom_chauffeur_camion["CategoriePermis"]
                form_update.date_engagement_update_wtf.data = data_nom_chauffeur_camion["DateEngagement"]
                form_update.id_camion_update_wtf.data = data_nom_chauffeur_camion["Id_camion"]
            else:
                flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                return redirect(url_for('chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_camion_sel=0))

    except Exception as e:
        raise ExceptionChauffeurUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                          f"{chauffeur_camion_update_wtf.__name__} ; "
                                          f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeur_camion_update_wtf.html", form_update=form_update,
                           id_chauffeur_camion_update=id_chauffeur_camion_update)


@app.route("/chauffeur_camion_delete/<int:id_chauffeur_camion_delete>", methods=['GET', 'POST'])
def chauffeur_camion_delete_wtf(id_chauffeur_camion_delete):
    form_delete = FormWTFDeleteChauffeurCamion()
    data_chauffeurs_camions_associes = None
    btn_submit_del = None

    try:
        if request.method == "POST" and form_delete.validate_on_submit():
            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("chauffeurs_camions_afficher", order_by="ASC", id_chauffeur_camion_sel=0))

            choix_suppression = form_delete.choix_suppression.data

            if form_delete.submit_btn_conf_del.data:
                data_chauffeurs_camions_associes = session.get('data_chauffeurs_camions_associes', None)
                flash(f"Effacer le {choix_suppression} de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                if choix_suppression == 'chauffeur':
                    valeur_delete_dictionnaire = {"value_id_chauffeur_camion": id_chauffeur_camion_delete}
                    str_sql_delete_chauffeur_camion = """DELETE FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur_camion)s"""
                else:
                    valeur_delete_dictionnaire = {"value_id_camion": data_chauffeurs_camions_associes[0]['Id_camion']}
                    str_sql_delete_chauffeur_camion = """DELETE FROM camion WHERE Id_camion = %(value_id_camion)s"""

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_chauffeur_camion, valeur_delete_dictionnaire)

                flash(f"{choix_suppression.capitalize()} définitivement effacé !!", "success")
                return redirect(url_for('chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_camion_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_chauffeur_camion": id_chauffeur_camion_delete}

            str_sql_chauffeurs_camions_associes = """SELECT camion.Id_camion, camion.Marque, camion.Modele FROM camion
                                             WHERE Id_camion IN (SELECT Id_camion FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur_camion)s)"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_chauffeurs_camions_associes, valeur_select_dictionnaire)
                data_chauffeurs_camions_associes = mydb_conn.fetchall()
                session['data_chauffeurs_camions_associes'] = data_chauffeurs_camions_associes

                str_sql_id_chauffeur_camion = "SELECT Id_Chauffeur, Nom FROM Chauffeur WHERE Id_Chauffeur = %(value_id_chauffeur_camion)s"
                mydb_conn.execute(str_sql_id_chauffeur_camion, valeur_select_dictionnaire)
                data_nom_chauffeur_camion = mydb_conn.fetchone()

                if data_nom_chauffeur_camion:
                    form_delete.nom_chauffeur_delete_wtf.data = data_nom_chauffeur_camion["Nom"]
                else:
                    flash(f"Le chauffeur demandé n'existe pas !!", "warning")
                    return redirect(url_for('chauffeurs_camions_afficher', order_by="ASC", id_chauffeur_camion_sel=0))

            btn_submit_del = False

    except Exception as e:
        raise ExceptionChauffeurDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                          f"{chauffeur_camion_delete_wtf.__name__} ; "
                                          f"{str(e)}")

    return render_template("chauffeurs_camions/chauffeur_camion_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_chauffeurs_camions_associes=data_chauffeurs_camions_associes,
                           id_chauffeur_camion=id_chauffeur_camion_delete)

