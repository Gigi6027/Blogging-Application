import os

from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
import redis
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import PostModel, UserModel
from schemas import PostSchema, PostUpdateSchema
from src.utils.binary_to_image import convert_binary_to_image, delete_image_file
from src.utils.no_post_users import no_post_users
from src.utils.response import created
from rq import Queue

from tasks import send_nopost_email, send_user_registration_email

blp = Blueprint("Posts", __name__, description="Operations on Posts")
connection = redis.Redis(host='localhost', port=6379)
queue = Queue("emails", connection=connection)


@blp.route("/add-post")
class AddPost(MethodView):
    @jwt_required()
    @blp.arguments(PostSchema)
    @blp.response(200, PostSchema)
    def post(self, post_data):
        image = post_data.pop('image')
        image_file_path = convert_binary_to_image(
            base64_binary=image,
            image_path=os.path.join(os.getenv('images_path'), 'posts'),
            filename=post_data['filename']
        )
        post_data['image_path'] = image_file_path
        post = PostModel(**post_data, user=UserModel.query.get(post_data['user_id']))
        try:
            db.session.add(post)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print('This item fails one of the unique/foreign key checks!')
        except SQLAlchemyError as err:
            abort(500, message=f"An error occurred creating the post. {err}")
        return post


@blp.route("/add-post/<int:post_id>")
class AddPost(MethodView):
    @jwt_required()
    @blp.arguments(PostUpdateSchema)
    def put(self, post_data, post_id):
        post = PostModel.query.get_or_404(post_id)
        if post:
            delete_image_file(
                image_file_path=post.image_path
            )
            image_file_path = convert_binary_to_image(
                base64_binary=post_data.get('image'),
                image_path=os.path.join(os.getenv('images_path'), 'posts'),
                filename=post_data['filename']
            )
            post.image_path = image_file_path
            post.title = post_data.get('title')
            post.description = post_data.get('description')
            post.filename = post_data.get('filename')

        try:
            db.session.add(post)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            print('This item fails one of the unique/foreign key checks!')
        except SQLAlchemyError as err:
            abort(500, message=f"An error occurred creating the post. {err}")
        return created(status_code=200, message='Post Updated')

    @jwt_required()
    def delete(self, post_id):
        post = PostModel.query.get_or_404(post_id)
        delete_image_file(
            image_file_path=post.image_path
        )
        db.session.delete(post)
        db.session.commit()
        return created(status_code=200, message='Post Deleted')


@blp.route("/no-post-users")
class MyFollowers(MethodView):
    #@jwt_required()
    def get(self):
        result = no_post_users()
        return created(
            status_code=200,
            message=result
        )
