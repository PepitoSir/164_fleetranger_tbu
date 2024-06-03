"""
    Fichier : gestion_camions_crud.py
    Auteur : OM 2021.03.16
"""
from pathlib import Path
from flask import redirect, request, session, url_for, flash, render_template
from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import ExceptionCamionsAfficher, ExceptionCamionsAjouterWtf, ExceptionCamionUpdateWtf, ExceptionCamionDeleteWtf
from APP_FILMS_164.camions.gestion_camions_wtf_forms import FormWTFAjouterCamions, FormWTFDeleteCamion, FormWTFUpdateCamion

@app.route("/camions_afficher/<string:order_by>/<int:id_camion_sel>", methods=['GET', 'POST'])
def camions_afficher(order_by, id_camion_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_camion_sel == 0:
                    strsql_camions_afficher = """SELECT * FROM camion"""
                    mc_afficher.execute(strsql_camions_afficher)
                elif order_by == "ASC":
                    valeur_id_camion_selected_dictionnaire = {"value_id_camion_selected": id_camion_sel}
                    strsql_camions_afficher = """SELECT * FROM camion WHERE Id_camion = %(value_id_camion_selected)s"""
                    mc_afficher.execute(strsql_camions_afficher, valeur_id_camion_selected_dictionnaire)
                else:
                    strsql_camions_afficher = """SELECT * FROM camion"""
                    mc_afficher.execute(strsql_camions_afficher)

                data_camions = mc_afficher.fetchall()

                if not data_camions and id_camion_sel == 0:
                    flash("""La table "camion" est vide !!""", "warning")
                elif not data_camions and id_camion_sel > 0:
                    flash(f"Le camion demandé n'existe pas !!", "warning")
                else:
                    flash(f"Données camions affichés !!", "success")

        except Exception as e:
            raise ExceptionCamionsAfficher(f"fichier : {Path(__file__).name}  ;  "
                                           f"{camions_afficher.__name__} ; "
                                           f"{str(e)}")

    return render_template("camions/camions_afficher.html", data=data_camions)


@app.route("/camions_ajouter", methods=['GET', 'POST'])
def camions_ajouter_wtf():
    form = FormWTFAjouterCamions()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                vin = form.vin_wtf.data
                marque = form.marque_wtf.data
                modele = form.modele_wtf.data
                date_construction = form.date_construction_wtf.data
                annee_achat = form.annee_achat_wtf.data
                km_totaux = form.km_totaux_wtf.data
                carburant = form.carburant_wtf.data
                charge = form.charge_wtf.data
                hauteur = form.hauteur_wtf.data
                disponibilite = form.disponibilite_wtf.data

                valeurs_insertion_dictionnaire = {
                    "vin": vin,
                    "marque": marque,
                    "modele": modele,
                    "date_construction": date_construction,
                    "annee_achat": annee_achat,
                    "km_totaux": km_totaux,
                    "carburant": carburant,
                    "charge": charge,
                    "hauteur": hauteur,
                    "disponibilite": disponibilite
                }

                strsql_insert_camion = """INSERT INTO camion 
                                          (VIN, Marque, Modele, DateConstruction, AnneedAchat, KmTotaux, Carburant, Charge, Hauteur, Disponibilité) 
                                          VALUES (%(vin)s, %(marque)s, %(modele)s, %(date_construction)s, %(annee_achat)s, %(km_totaux)s, %(carburant)s, %(charge)s, %(hauteur)s, %(disponibilite)s)"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_camion, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                return redirect(url_for('camions_afficher', order_by='DESC', id_camion_sel=0))

        except Exception as e:
            raise ExceptionCamionsAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                             f"{camions_ajouter_wtf.__name__} ; "
                                             f"{str(e)}")

    return render_template("camions/camions_ajouter_wtf.html", form=form)


@app.route("/camion_update", methods=['GET', 'POST'])
def camion_update_wtf():
    id_camion_update = request.values['id_camion_btn_edit_html']
    form_update = FormWTFUpdateCamion()
    try:
        if request.method == "POST" and form_update.submit.data:
            vin = form_update.vin_update_wtf.data
            marque = form_update.marque_update_wtf.data
            modele = form_update.modele_update_wtf.data
            date_construction = form_update.date_construction_update_wtf.data
            annee_achat = form_update.annee_achat_update_wtf.data
            km_totaux = form_update.km_totaux_update_wtf.data
            carburant = form_update.carburant_update_wtf.data
            charge = form_update.charge_update_wtf.data
            hauteur = form_update.hauteur_update_wtf.data
            disponibilite = form_update.disponibilite_update_wtf.data

            valeur_update_dictionnaire = {
                "id_camion": id_camion_update,
                "vin": vin,
                "marque": marque,
                "modele": modele,
                "date_construction": date_construction,
                "annee_achat": annee_achat,
                "km_totaux": km_totaux,
                "carburant": carburant,
                "charge": charge,
                "hauteur": hauteur,
                "disponibilite": disponibilite
            }

            str_sql_update_camion = """UPDATE camion SET VIN = %(vin)s, Marque = %(marque)s, Modele = %(modele)s, 
                                       DateConstruction = %(date_construction)s, AnneedAchat = %(annee_achat)s, 
                                       KmTotaux = %(km_totaux)s, Carburant = %(carburant)s, Charge = %(charge)s, 
                                       Hauteur = %(hauteur)s, Disponibilité = %(disponibilite)s WHERE Id_camion = %(id_camion)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_camion, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=id_camion_update))
        elif request.method == "GET":
            str_sql_id_camion = "SELECT Id_camion, VIN, Marque, Modele, DateConstruction, AnneedAchat, KmTotaux, Carburant, Charge, Hauteur, Disponibilité FROM camion WHERE Id_camion = %(value_id_camion)s"
            valeur_select_dictionnaire = {"value_id_camion": id_camion_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_camion, valeur_select_dictionnaire)
            data_nom_camion = mybd_conn.fetchone()

            if data_nom_camion:  # Add this check to avoid 'NoneType' object is not subscriptable
                form_update.vin_update_wtf.data = data_nom_camion["VIN"]
                form_update.marque_update_wtf.data = data_nom_camion["Marque"]
                form_update.modele_update_wtf.data = data_nom_camion["Modele"]
                form_update.date_construction_update_wtf.data = data_nom_camion["DateConstruction"]
                form_update.annee_achat_update_wtf.data = data_nom_camion["AnneedAchat"]
                form_update.km_totaux_update_wtf.data = data_nom_camion["KmTotaux"]
                form_update.carburant_update_wtf.data = data_nom_camion["Carburant"]
                form_update.charge_update_wtf.data = data_nom_camion["Charge"]
                form_update.hauteur_update_wtf.data = data_nom_camion["Hauteur"]
                form_update.disponibilite_update_wtf.data = data_nom_camion["Disponibilité"]
            else:
                flash(f"Le camion demandé n'existe pas !!", "warning")
                return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=0))

    except Exception as e:
        raise ExceptionCamionUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                       f"{camion_update_wtf.__name__} ; "
                                       f"{str(e)}")

    return render_template("camions/camion_update_wtf.html", form_update=form_update)


@app.route("/camion_delete", methods=['GET', 'POST'])
def camion_delete_wtf():
    data_camions_associes = None
    btn_submit_del = None
    id_camion_delete = request.values['id_camion_btn_delete_html']
    form_delete = FormWTFDeleteCamion()
    try:
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("camions_afficher", order_by="ASC", id_camion_sel=0))

            if form_delete.submit_btn_conf_del.data:
                data_camions_associes = session['data_camions_associes']
                flash(f"Effacer le camion de façon définitive de la BD !!!", "danger")
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_camion": id_camion_delete}

                str_sql_delete_camion = """DELETE FROM camion WHERE Id_camion = %(value_id_camion)s"""
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_camion, valeur_delete_dictionnaire)

                flash(f"Camion définitivement effacé !!", "success")
                return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_camion": id_camion_delete}

            str_sql_camions_associes = """SELECT Assurance.Id_Assurance, Assurance.Compagnie, Assurance.NumPolice FROM Assurance
                                          WHERE Id_camion = %(value_id_camion)s"""
            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_camions_associes, valeur_select_dictionnaire)
                data_camions_associes = mydb_conn.fetchall()
                session['data_camions_associes'] = data_camions_associes

                str_sql_id_camion = "SELECT Id_camion, Marque FROM camion WHERE Id_camion = %(value_id_camion)s"
                mydb_conn.execute(str_sql_id_camion, valeur_select_dictionnaire)
                data_nom_camion = mydb_conn.fetchone()

                if data_nom_camion:  # Add this check to avoid 'NoneType' object is not subscriptable
                    form_delete.nom_camion_delete_wtf.data = data_nom_camion["Marque"]
                else:
                    flash(f"Le camion demandé n'existe pas !!", "warning")
                    return redirect(url_for('camions_afficher', order_by="ASC", id_camion_sel=0))

            btn_submit_del = False

    except Exception as e:
        raise ExceptionCamionDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                       f"{camion_delete_wtf.__name__} ; "
                                       f"{str(e)}")

    return render_template("camions/camion_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_camions_associes=data_camions_associes)
