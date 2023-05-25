from datetime import datetime

import jwt
from flask import jsonify, current_app
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import UserModel, PostModel, FollowerModel
from schemas import ProfileSchema, FollowerSchema, PostSchema, MyFeedSchema, MyFollowerSchema, FollowingUsersSchema, \
    AllUsersSchema, RemoveFollowerSchema
from src.utils.binary_to_image import convert_binary_to_image, convert_image_to_base64
from src.utils.decode_jwt import decode_jwt
from src.utils.response import created

blp = Blueprint("Followers", __name__, description="Fetch followers and following page details")


@blp.route("/follow")
class Follow(MethodView):
    @jwt_required()
    @blp.arguments(FollowerSchema)
    def post(self, follower_data):
        # Validating whether already record exists or not before insert.
        follower_validate = FollowerModel.query.filter(
            FollowerModel.leader_user_id == follower_data["leader_user_id"],
            FollowerModel.follower_user_id == follower_data["follower_user_id"]
        ).first()
        if follower_validate is not None:
            follower_validate.block = False
            return self.update_following(
                following_data=follower_validate,
                following=follower_data["following"]
            )

        # Inserting the record
        follow = FollowerModel(**follower_data)
        try:
            db.session.add(follow)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=f"An error occurred creating the post. {err}")
        return created(201, "Inserted Successfully")

    @staticmethod
    def update_following(following_data, following=False):
        following_data.following = following
        following_data.updated_date = datetime.now()
        try:
            db.session.add(following_data)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=f"An error occurred while inserting the item. {err}")
        return created(200, "Updated Successfully")


@blp.route("/my-followers/<int:user_id>")
class MyFollowers(MethodView):
    @jwt_required()
    @blp.response(200, MyFollowerSchema)
    def get(self, user_id):
        my_followers = FollowerModel.query.filter(
            FollowerModel.leader_user_id == user_id,
            FollowerModel.following == True,
            FollowerModel.block == False
        ).all()

        for i in my_followers:
            user = UserModel.query.get_or_404(i.follower_user_id)
            i.name = user.name
            i.subname = user.subname
            i.userId = user.id
            i.userProfileImage = convert_image_to_base64(user.image_path)
        return jsonify(MyFollowerSchema(many=True).dump(my_followers))


@blp.route("/following/<int:user_id>")
class MyFollowers(MethodView):
    @jwt_required()
    @blp.response(200, FollowingUsersSchema)
    def get(self, user_id):
        following = FollowerModel.query.filter(
            FollowerModel.follower_user_id == user_id,
            FollowerModel.following == True,
            FollowerModel.block == False
        ).all()

        for i in following:
            user = UserModel.query.get_or_404(i.leader_user_id)
            i.name = user.name
            i.subname = user.subname
            i.userId = user.id
            i.userProfileImage = convert_image_to_base64(user.image_path)

        return jsonify(FollowingUsersSchema(many=True).dump(following))


@blp.route("/all-users")
class AllUsers(MethodView):
    @jwt_required()
    @blp.response(200, AllUsersSchema(many=True))
    def get(self):
        user_id = decode_jwt()['sub']
        users = UserModel.query.filter(
            UserModel.id != user_id
        ).all()
        for i in users:
            i.userProfileImage = convert_image_to_base64(i.image_path)
            i.userId = i.id
            i.following = False  # default False

            followers = FollowerModel.query.filter(
                FollowerModel.leader_user_id == i.id,
                FollowerModel.follower_user_id == user_id,
                FollowerModel.block == False
            ).all()
            for f in followers:
                i.following = f.following
        return jsonify(AllUsersSchema(many=True).dump(users))


@blp.route("/remove-follower")
class RemoveFollower(MethodView):
    @jwt_required()
    @blp.arguments(RemoveFollowerSchema)
    def post(self, remove_follower):
        follower_validate = FollowerModel.query.filter(
            FollowerModel.leader_user_id == remove_follower["leader_user_id"],
            FollowerModel.follower_user_id == remove_follower["follower_user_id"]
        ).first()
        follower_validate.block = remove_follower["block"]
        try:
            db.session.add(follower_validate)
            db.session.commit()
        except SQLAlchemyError as err:
            abort(500, message=f"An error occurred creating the post. {err}")
        return created(200, "Updated Successfully")
