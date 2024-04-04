"""
    Fichier : gestion_mails_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjoutermails(FlaskForm):
    """
        Dans le formulaire "mails_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_mails_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_mails_wtf = StringField("Clavioter le mails ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                   Regexp(nom_mails_regexp,
                                                                          message="Pas de chiffres, de caractères "
                                                                                  "spéciaux, "
                                                                                  "d'espace à double, de double "
                                                                                  "apostrophe, de double trait union")
                                                                   ])
    submit = SubmitField("Enregistrer mails")


class FormWTFUpdatemails(FlaskForm):
    """
        Dans le formulaire "mails_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_mails_update_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    nom_mails_update_wtf = StringField("Clavioter le mails ", validators=[Length(min=2, max=20, message="min 2 max 20"),
                                                                          Regexp(nom_mails_update_regexp,
                                                                                 message="Pas de chiffres, de "
                                                                                         "caractères "
                                                                                         "spéciaux, "
                                                                                         "d'espace à double, de double "
                                                                                         "apostrophe, de double trait "
                                                                                         "union")
                                                                          ])
    date_mails_wtf_essai = DateField("Essai date", validators=[InputRequired("Date obligatoire"),
                                                               DataRequired("Date non valide")])
    submit = SubmitField("Update mails")


class FormWTFDeletemails(FlaskForm):
    """
        Dans le formulaire "mails_delete_wtf.html"

        nom_mails_delete_wtf : Champ qui reçoit la valeur du mails, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "mails".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_mails".
    """
    nom_mails_delete_wtf = StringField("Effacer ce mails")
    submit_btn_del = SubmitField("Effacer mails")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
