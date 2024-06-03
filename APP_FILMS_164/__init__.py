from flask import Flask
from environs import Env
import sys

# Définition de l'application Flask
app = Flask(__name__)

try:
    obj_env = Env()
    obj_env.read_env()
    HOST_MYSQL = obj_env("HOST_MYSQL")
    USER_MYSQL = obj_env("USER_MYSQL")
    PASS_MYSQL = obj_env("PASS_MYSQL")
    PORT_MYSQL = int(obj_env("PORT_MYSQL"))
    NAME_BD_MYSQL = obj_env("NAME_BD_MYSQL")
    NAME_FILE_DUMP_SQL_BD = obj_env("NAME_FILE_DUMP_SQL_BD")

    ADRESSE_SRV_FLASK = obj_env("ADRESSE_SRV_FLASK")
    DEBUG_FLASK = obj_env("DEBUG_FLASK")
    PORT_FLASK = obj_env("PORT_FLASK")
    SECRET_KEY_FLASK = obj_env("SECRET_KEY_FLASK")

    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY_FLASK
    )

    from APP_FILMS_164.database import database_tools
    from APP_FILMS_164.essais_wtf_forms import gestion_essai_wtf
    from APP_FILMS_164.essais_wtf_forms import gestion_wtf_forms_demo_select
    from APP_FILMS_164.genres import gestion_genres_crud
    from APP_FILMS_164.demos_om_164 import routes_demos

    from APP_FILMS_164.films_genres import gestion_films_genres_crud
    from APP_FILMS_164.erreurs import msg_avertissements

    from APP_FILMS_164.films import gestion_films_crud
    from APP_FILMS_164.films import gestion_films_wtf_forms

    from APP_FILMS_164.mails import gestion_mails_crud
    from APP_FILMS_164.mails import gestion_mails_wtf_forms

    from APP_FILMS_164.camions import gestion_camions_crud
    from APP_FILMS_164.camions import gestion_camions_wtf_forms

    from APP_FILMS_164.chauffeurs import gestion_chauffeurs_crud
    from APP_FILMS_164.chauffeurs import gestion_chauffeurs_wtf_forms

    from APP_FILMS_164.chauffeurs_camions.gestion_chauffeurs_camions_crud import bp as chauffeurs_camions_bp

    app.register_blueprint(chauffeurs_camions_bp, url_prefix='/gestion_chauffeurs_camions')

except Exception as e:
    print(f"4567756434 Une erreur est survenue {type(e)} dans"
          f"__init__ {e.args}")
    sys.exit()
