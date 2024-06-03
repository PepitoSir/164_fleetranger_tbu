"""
    Fichier : gestion_chauffeurs_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import Length, InputRequired, DataRequired, Regexp

class FormWTFAjouterChauffeurs(FlaskForm):
    """
        Formulaire pour ajouter un chauffeur.
    """
    nom_wtf = StringField("Nom", validators=[Length(min=2, max=40, message="min 2 max 40"), InputRequired("Nom obligatoire")])
    prenom_wtf = StringField("Prénom", validators=[Length(min=2, max=40, message="min 2 max 40"), InputRequired("Prénom obligatoire")])
    categorie_permis_wtf = StringField("Catégorie de permis", validators=[Length(min=2, max=20, message="min 2 max 20"), InputRequired("Catégorie de permis obligatoire")])
    date_engagement_wtf = DateField("Date d'engagement", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    id_camion_wtf = IntegerField("ID Camion", validators=[DataRequired("ID Camion obligatoire")])
    submit = SubmitField("Enregistrer chauffeur")


class FormWTFUpdateChauffeur(FlaskForm):
    """
        Formulaire pour mettre à jour un chauffeur.
    """
    nom_update_wtf = StringField("Nom", validators=[Length(min=2, max=40, message="min 2 max 40"), InputRequired("Nom obligatoire")])
    prenom_update_wtf = StringField("Prénom", validators=[Length(min=2, max=40, message="min 2 max 40"), InputRequired("Prénom obligatoire")])
    categorie_permis_update_wtf = StringField("Catégorie de permis", validators=[Length(min=2, max=20, message="min 2 max 20"), InputRequired("Catégorie de permis obligatoire")])
    date_engagement_update_wtf = DateField("Date d'engagement", validators=[InputRequired("Date obligatoire"), DataRequired("Date non valide")])
    id_camion_update_wtf = IntegerField("ID Camion", validators=[DataRequired("ID Camion obligatoire")])
    submit = SubmitField("Mettre à jour le chauffeur")


class FormWTFDeleteChauffeur(FlaskForm):
    nom_chauffeur_delete_wtf = StringField("Nom du chauffeur", validators=[DataRequired()])
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_del = SubmitField("Effacer définitivement")
    submit_btn_annuler = SubmitField("Annuler")
