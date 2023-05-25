import json
import logging

from flask import jsonify
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from db import db
from cache import cache
from models import UserModel, PostModel, FollowerModel
from schemas import ProfileSchema, FollowerSchema, PostSchema, MyFeedSchema
from src.utils.binary_to_image import convert_image_to_base64

blp = Blueprint("Profile", __name__, description="Fetch profile page details")


@blp.route("/profile/<int:user_id>")
class Profile(MethodView):
    """Fetch the profile page data
    :return:
    followers: count of followers
    following: count of users im following
    posts: all my posts
    totalPost: total post counts
    userId: user id
    """

    @jwt_required()
    @blp.response(200, ProfileSchema)
    def get(self, user_id):
        class Response:
            pass

        response = Response()
        user = UserModel.query.get_or_404(user_id)

        # getting image base64 data
        response.userProfileImage = convert_image_to_base64(user.image_path)
        response.userId = user_id

        # count of post for user_id
        post_count = PostModel.query.filter(
            PostModel.user_id == user_id
        ).count()
        response.totalPost = post_count

        # count of followers
        response.followers = FollowerModel.query.filter(
            FollowerModel.leader_user_id == user_id, 
            FollowerModel.following == True,
            FollowerModel.block == False
        ).count()

        # count of following
        response.following = FollowerModel.query.filter(
            FollowerModel.follower_user_id == user_id,
            FollowerModel.following == True,
            FollowerModel.block == False
        ).count()

        # all posts for user_id
        all_posts = PostModel.query.filter(
            PostModel.user_id == user_id
        ).all()

        for i in all_posts:
            i.postId = i.id
            i.like = 0  # TODO: Harding the like and comments value for now
            i.comments = 0
            i.image = convert_image_to_base64(i.image_path)
        response.posts = all_posts
        return response.__dict__


@blp.route("/my-feed/<int:user_id>")
class MyFeed(MethodView):
    """List of posts by people you follow"""
    @jwt_required()
    @blp.response(200, MyFeedSchema)
    @cache.cached(timeout=50)
    def get(self, user_id):
        response = {}
        following_users = FollowerModel.query.filter(
            FollowerModel.follower_user_id == user_id,
            FollowerModel.following == True,
            FollowerModel.block == False
        ).all()

        leader_user_ids = [i.leader_user_id for i in following_users]

        my_feeds = PostModel.query.filter(
            PostModel.user_id.in_(leader_user_ids)
        ).all()

        for i in my_feeds:
            i.username = UserModel.query.get(i.user_id).username
            i.name = UserModel.query.get(i.user_id).name
            i.subname = UserModel.query.get(i.user_id).subname
            i.image = convert_image_to_base64(i.image_path)
            i.userProfileImage = convert_image_to_base64(UserModel.query.get(i.user_id).image_path)

        try:
            response = MyFeedSchema(many=True).dump(my_feeds)
        except ValidationError as err:
            print(err.messages)
        else:
            print("No Error")
        
        return jsonify(response)
