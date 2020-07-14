import falcon

from timing.models.user import User


class RegisterResource(object):

    @staticmethod
    def on_post(req, resp):
        user = User(username=req.media['username'])
        req.context.db_session.add(user)
        req.context.db_session.commit()
        resp.media = user.to_dict()
