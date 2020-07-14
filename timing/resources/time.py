from datetime import datetime

import falcon
from sqlalchemy import func

from timing.authorization import Authorization
from timing.models.time import Time, DATETIME_FORMAT
from timing.paginate import Paginate
from timing.schemas.time import TimeInSchema


class TimesResource(object):

    @falcon.before(Authorization())
    def on_post(self, req, resp):
        data = TimeInSchema(
            user_id=req.context['user_id'],
            createdAt=req.params.get('t', None),
            hours=req.media['hours'],
        )

        time = Time(**data.dict(exclude_unset=True))
        req.context.db_session.add(time)
        req.context.db_session.commit()

        resp.media = time.to_dict()

    @falcon.before(Authorization())
    @falcon.before(Paginate())
    def on_get(self, req, resp):
        time_query = self._get_times(req, query_on=Time)

        total_count = time_query.count()
        time_query = time_query \
            .order_by(Time.created_at) \
            .limit(req.context['limit']) \
            .offset(req.context['offset']) \

        resp.media = [t.to_dict() for t in time_query]
        resp.set_header('X-COUNT', total_count)

    @falcon.before(Authorization())
    def on_get_calculator(self, req, resp):
        sum_times = self._get_times(req, query_on=func.sum(Time.hours)).one()
        sum_times = int(sum_times[0] or 0)

        resp.media = Time(
            created_at=datetime.utcnow(),
            hours=sum_times,
        ).to_dict()

    def _get_times(self, req, query_on):
        time_query = req.context.db_session.query(query_on) \
            .filter(Time.user_id == req.context.user_id)
        if from_ := req.params.get('from'):
            time_query = time_query.filter(
                Time.created_at >= datetime.strptime(from_, DATETIME_FORMAT)
            )
        if to_ := req.params.get('to'):
            time_query = time_query.filter(
                Time.created_at <= datetime.strptime(to_, DATETIME_FORMAT)
            )
        return time_query
