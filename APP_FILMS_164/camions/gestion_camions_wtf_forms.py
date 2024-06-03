"""
    Fichier : gestion_camions_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, BooleanField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired, Regexp, NumberRange

class FormWTFAjouterCamions(FlaskForm):
    """
        Formulaire pour ajouter un camion.
    """
    vin_wtf = StringField("Clavioter le VIN ", validators=[Length(min=2, max=20, message="min 2 max 20")])
    marque_wtf = StringField("Clavioter la marque ", validators=[Length(min=2, max=40, message="min 2 max 40")])
    modele_wtf = StringField("Clavioter le modèle ", validators=[Length(min=2, max=40, message="min 2 max 40")])
    date_construction_wtf = DateField("Date de construction", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    annee_achat_wtf = DateField("Année d'achat", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    km_totaux_wtf = IntegerField("Kilométrage total ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    carburant_wtf = StringField("Type de carburant ", validators=[Length(min=2, max=20, message="min 2 max 20")])
    charge_wtf = IntegerField("Charge maximale ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    hauteur_wtf = IntegerField("Hauteur ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    disponibilite_wtf = BooleanField("Disponibilité ")
    submit = SubmitField("Enregistrer camion")


class FormWTFUpdateCamion(FlaskForm):
    """
        Formulaire pour mettre à jour un camion.
    """
    vin_update_wtf = StringField("Clavioter le VIN ", validators=[Length(min=2, max=20, message="min 2 max 20")])
    marque_update_wtf = StringField("Clavioter la marque ", validators=[Length(min=2, max=40, message="min 2 max 40")])
    modele_update_wtf = StringField("Clavioter le modèle ", validators=[Length(min=2, max=40, message="min 2 max 40")])
    date_construction_update_wtf = DateField("Date de construction", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    annee_achat_update_wtf = DateField("Année d'achat", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    km_totaux_update_wtf = IntegerField("Kilométrage total ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    carburant_update_wtf = StringField("Type de carburant ", validators=[Length(min=2, max=20, message="min 2 max 20")])
    charge_update_wtf = IntegerField("Charge maximale ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    hauteur_update_wtf = IntegerField("Hauteur ", validators=[InputRequired(), NumberRange(min=0, message="Valeur positive requise")])
    disponibilite_update_wtf = BooleanField("Disponibilité ")
    submit = SubmitField("Mettre à jour le camion")


class FormWTFDeleteCamion(FlaskForm):
    """
        Formulaire pour effacer un camion.
        nom_camion_delete_wtf : Champ qui reçoit la valeur du nom du camion, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "camion".
        submit_btn_annuler : Bouton qui permet d'annuler l'opération.
    """
    nom_camion_delete_wtf = StringField("Effacer ce Camion")
    submit_btn_del = SubmitField("Effacer camion")
    submit_btn_conf_del = SubmitField("Etes-vous sûr d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
