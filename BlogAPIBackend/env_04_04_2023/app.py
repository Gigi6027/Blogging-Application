import os

from flask import Flask, jsonify
from flask_cors import CORS # Added
from flask_smorest import Api
from flask_jwt_extended import JWTManager, create_access_token
from flask_migrate import Migrate
from flask_crontab import Crontab
from dotenv import load_dotenv

from db import db
from cache import cache
from blocklist import BLOCKLIST
from sqlalchemy.engine import Engine
from sqlalchemy import event

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint
from resources.tag import blp as TagBlueprint
from resources.user import blp as UserBlueprint
from resources.add_post import blp as PostBlueprint
from resources.profile import blp as ProfileBlueprint
from resources.followers import blp as FollowersBlueprint
from src.utils.no_post_users import no_post_users
from src.utils.validate_path import create_path_if_not_exist

crontab = Crontab()

def create_app(db_url=None):
    app = Flask(__name__)
    CORS(app) # Added
    load_dotenv()

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Blog REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or "sqlite:///blogdata.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.config["JWT_SECRET_KEY"] = "jose"

    db.init_app(app)
    crontab.init_app(app)
    cache.init_app(app)
    api = Api(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    with app.app_context():
        db.create_all()

    images_path = os.getenv('IMAGE_FOLDER_PATH') or os.path.join(
        os.path.abspath(os.getcwd()), "images")
    os.environ['images_path'] = images_path
    create_path_if_not_exist(images_path)

    # this will valid all the foreign key relation when data inserting
    @event.listens_for(Engine, "connect")
    def set_sqlite_pragma(dbapi_connection, connection_record):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {"description": "The token has been revoked.", "error": "token_revoked"}
            ),
            401,
        )

    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return (
            jsonify(
                {
                    "description": "The token is not fresh.",
                    "error": "fresh_token_required",
                }
            ),
            401,
        )

    @jwt.additional_claims_loader
    def add_claims_to_jwt(identity):
        # Look in the database and see whether the user is an admin
        if identity == 1:
            return {"is_admin": True}
        return {"is_admin": False}

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return (
            jsonify({"message": "The token has expired.", "error": "token_expired"}),
            401,
        )

    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return (
            jsonify(
                {"message": "Signature verification failed.", "error": "invalid_token"}
            ),
            401,
        )

    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return (
            jsonify(
                {
                    "description": "Request does not contain an access token.",
                    "error": "authorization_required",
                }
            ),
            401,
        )

    # @app.before_first_request
    # def create_tables():
    #     db.create_all()

    @crontab.job(minute="0", hour="9", day="*", month="*", day_of_week="*")
    def my_scheduled_job():
        no_post_users()

  #  api.register_blueprint(ItemBlueprint)
  #  api.register_blueprint(StoreBlueprint)
  #  api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)
    api.register_blueprint(PostBlueprint)
    api.register_blueprint(ProfileBlueprint)
    api.register_blueprint(FollowersBlueprint)

    return app


if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000)
