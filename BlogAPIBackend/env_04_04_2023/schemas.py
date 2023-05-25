from marshmallow import Schema, fields, validate


class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()), dump_only=True)


class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)


class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tag = fields.Nested(TagSchema)


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserRegisterSchema(UserSchema):
    name = fields.Str(required=True)
    subname = fields.Str(required=True)
    email = fields.Str(required=True)
    image = fields.Str(required=True)


class PostSchema(Schema):
    user_id = fields.Int(load_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str(required=True)
    filename = fields.Str(required=True)
    create_date = fields.DateTime(dump_only=True)


class PostUpdateSchema(PostSchema):
    postId = fields.Int()


class PostSchemaWithLikeComments(Schema):
    postId = fields.Int()
    user_id = fields.Int()
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str(required=True)
    filename = fields.Str(required=True)
    like = fields.Int(required=True)
    comments = fields.Int(required=True)


class ProfileSchema(Schema):
    userId = fields.Int(required=True)
    profileImage = fields.Str(required=True)
    totalPost = fields.Int(required=True)
    followers = fields.Int(required=True)
    following = fields.Int(required=True)
    posts = fields.List(fields.Nested(PostSchemaWithLikeComments()), dump_only=True)


class FollowerSchema(Schema):
    leader_user_id = fields.Int(load_only=True)
    follower_user_id = fields.Int(load_only=True)
    following = fields.Boolean(required=True)


class MyFollowerSchema(Schema):
    userId = fields.Int(required=True)
    name = fields.Str(required=True)
    subname = fields.Str(required=True)
    userProfileImage = fields.Str(required=True)
    following = fields.Boolean(required=True)


class FollowingUsersSchema(Schema):
    userId = fields.Int(required=True)
    name = fields.Str(required=True)
    subname = fields.Str(required=True)
    userProfileImage = fields.Str(required=True)
    following = fields.Boolean(required=True)


class MyFeedSchema(Schema):
    user_id = fields.Int(required=True)
    name = fields.Str(required=True)
    subname = fields.Str(required=True)
    username = fields.Str(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    image = fields.Str(required=True)
    userProfileImage = fields.Str(required=True)


class AllUsersSchema(Schema):
    userId = fields.Int(required=True)
    name = fields.Str(required=True)
    subname = fields.Str(required=True)
    username = fields.Str(required=True)
    userProfileImage = fields.Str(required=True)
    following = fields.Boolean(required=True)


class RemoveFollowerSchema(Schema):
    leader_user_id = fields.Int(load_only=True)
    follower_user_id = fields.Int(load_only=True)
    block = fields.Boolean(required=True)
