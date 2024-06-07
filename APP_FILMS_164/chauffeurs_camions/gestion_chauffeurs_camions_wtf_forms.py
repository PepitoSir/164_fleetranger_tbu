from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length
from APP_FILMS_164.database.database_tools import DBconnection


class FormWTFAjouterChauffeursCamions(FlaskForm):
    nom_wtf = StringField('Nom', validators=[DataRequired(), Length(min=2, max=20)])
    prenom_wtf = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=20)])
    categorie_permis_wtf = StringField('Catégorie Permis', validators=[DataRequired(), Length(min=1, max=10)])
    date_engagement_wtf = DateField('Date Engagement', format='%Y-%m-%d', validators=[DataRequired()])
    id_camion_wtf = SelectField('Camion', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Ajouter')

    def __init__(self, *args, **kwargs):
        super(FormWTFAjouterChauffeursCamions, self).__init__(*args, **kwargs)
        self.populate_camions()

    def populate_camions(self):
        with DBconnection() as db:
            str_sql_camions = """SELECT Id_camion, Marque, Modele FROM camion"""
            db.execute(str_sql_camions)
            data_camions = db.fetchall()
            self.id_camion_wtf.choices = [(camion['Id_camion'], f"{camion['Marque']} {camion['Modele']}") for camion in
                                          data_camions]


class FormWTFUpdateChauffeurCamion(FlaskForm):
    nom_update_wtf = StringField('Nom', validators=[DataRequired(), Length(min=2, max=20)])
    prenom_update_wtf = StringField('Prénom', validators=[DataRequired(), Length(min=2, max=20)])
    categorie_permis_update_wtf = StringField('Catégorie Permis', validators=[DataRequired(), Length(min=1, max=10)])
    date_engagement_update_wtf = DateField('Date Engagement', format='%Y-%m-%d', validators=[DataRequired()])
    id_camion_update_wtf = SelectField('Camion', choices=[], coerce=int, validators=[DataRequired()])
    submit = SubmitField('Mettre à jour')

    def __init__(self, *args, **kwargs):
        super(FormWTFUpdateChauffeurCamion, self).__init__(*args, **kwargs)
        self.populate_camions()

    def populate_camions(self):
        with DBconnection() as db:
            str_sql_camions = """SELECT Id_camion, Marque, Modele FROM camion"""
            db.execute(str_sql_camions)
            data_camions = db.fetchall()
            self.id_camion_update_wtf.choices = [(camion['Id_camion'], f"{camion['Marque']} {camion['Modele']}") for camion in data_camions]


class FormWTFDeleteChauffeurCamion(FlaskForm):
    nom_chauffeur_delete_wtf = StringField('Nom', validators=[DataRequired()], render_kw={'readonly': True})
    choix_suppression = RadioField('Choisissez ce que vous souhaitez supprimer', choices=[('chauffeur', 'Chauffeur'), ('camion', 'Camion')], default='chauffeur', validators=[DataRequired()])
    submit_btn_conf_del = SubmitField('Confirmer la suppression')
    submit_btn_annuler = SubmitField('Annuler')
    submit_btn_del = SubmitField('Effacer définitivement')
