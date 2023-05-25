# from datetime import datetime

# import jwt
# from flask import jsonify, current_app
# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from flask_jwt_extended import jwt_required
# from sqlalchemy.exc import SQLAlchemyError

# from db import db
# from models import UserModel, PostModel, FollowerModel
# from schemas import ProfileSchema, FollowerSchema, PostSchema, MyFeedSchema, MyFollowerSchema, FollowingUsersSchema, \
#     AllUsersSchema, RemoveFollowerSchema
# from src.utils.binary_to_image import convert_binary_to_image, convert_image_to_base64
# from src.utils.decode_jwt import decode_jwt
# from src.utils.response import created

# blp = Blueprint("DownloadPosts", __name__, description="Fetch download post requests and download file")


# @blp.route("/remove-follower")
# class RemoveFollower(MethodView):
#     @jwt_required()
#     @blp.arguments(RemoveFollowerSchema)
#     def post(self, remove_follower):
#         follower_validate = FollowerModel.query.filter(
#             FollowerModel.leader_user_id == remove_follower["leader_user_id"],
#             FollowerModel.follower_user_id == remove_follower["follower_user_id"]
#         ).first()
#         follower_validate.block = remove_follower["block"]
#         try:
#             db.session.add(follower_validate)
#             db.session.commit()
#         except SQLAlchemyError as err:
#             abort(500, message=f"An error occurred creating the post. {err}")
#         return created(200, "Updated Successfully")
