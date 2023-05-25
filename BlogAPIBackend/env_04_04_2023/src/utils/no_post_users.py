import redis
from models import PostModel, UserModel
from rq import Queue
from datetime import date, datetime

from tasks import send_nopost_email

connection = redis.Redis(host='localhost', port=6379)
queue = Queue("emails", connection=connection)


def no_post_users():
    users = UserModel.query.all()
    for user in users:
        #chk_post = PostModel.query.filter(PostModel.user_id == user.id).first()
        

        today = date.today()
        chk_post = PostModel.query.filter(PostModel.user_id == user.id, PostModel.created_date >= datetime.combine(today, datetime.min.time())).first()


        if chk_post is None:
            queue.enqueue(send_nopost_email,"aanaymariai@gmail.com", user.username)
    return 'Sent emails to No Post Users..!'
