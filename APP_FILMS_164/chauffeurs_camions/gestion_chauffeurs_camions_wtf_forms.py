from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length

class FormWTFAjouterChauffeursCamions(FlaskForm):
    nom_wtf = StringField("Nom", validators=[DataRequired(), Length(min=2, max=200)])
    prenom_wtf = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=200)])
    categorie_permis_wtf = StringField("Catégorie Permis", validators=[DataRequired(), Length(min=1, max=10)])
    date_engagement_wtf = DateField("Date d'engagement", validators=[DataRequired()])
    id_camion_wtf = SelectField("ID Camion", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Ajouter")

class FormWTFUpdateChauffeurCamions(FlaskForm):
    nom_update_wtf = StringField("Nom", validators=[DataRequired(), Length(min=2, max=200)])
    prenom_update_wtf = StringField("Prénom", validators=[DataRequired(), Length(min=2, max=200)])
    categorie_permis_update_wtf = StringField("Catégorie Permis", validators=[DataRequired(), Length(min=1, max=10)])
    date_engagement_update_wtf = DateField("Date d'engagement", validators=[DataRequired()])
    id_camion_update_wtf = SelectField("ID Camion", validators=[DataRequired()], coerce=int)
    submit = SubmitField("Mettre à jour")

class FormWTFDeleteChauffeurCamions(FlaskForm):
    nom_chauffeur_delete_wtf = StringField("Nom", render_kw={'readonly': True})
    submit_btn_conf_del = SubmitField("Confirmer la suppression")
    submit_btn_del = SubmitField("Effacer définitivement")
    submit_btn_annuler = SubmitField("Annuler")
