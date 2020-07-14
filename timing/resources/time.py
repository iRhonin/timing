import falcon

from timing.models.time import Time
from timing.models.user import User
from timing.schemas.time import TimeInSchema


class TimesResource(object):

    @staticmethod
    def on_post(req, resp):
        data = TimeInSchema(
            user_id=req.headers['X-IDENTITY'],
            createdAt=req.params.get('t', None),
            hours=req.media['hours'],
        )

        time = Time(**data.dict(exclude_unset=True))
        req.context.db_session.add(time)
        req.context.db_session.commit()
        resp.media = time.to_dict()
