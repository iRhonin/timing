import falcon

from timing.db import table_utils
from timing.db.engine import metadata
from timing.db.middleware import SQLAlchemySessionManager
from timing.db.session import Session
from timing.resources.register import RegisterResource
from timing.resources.time import TimesResource

register_resource = RegisterResource()
time_resource = TimesResource()


def create_app():
    app = falcon.API(
        middleware=[
            SQLAlchemySessionManager(Session)
        ]
    )
    app.add_route('/register', register_resource)
    app.add_route('/time/add', time_resource)
    app.add_route('/time/get', time_resource)
    app.add_route('/time/calculator', time_resource, suffix='calculator')

    # Setup tables
    table_utils.drop_tables(metadata)
    table_utils.create_tables(metadata)

    return app
