import falcon

from timing.db import table_utils
from timing.db.engine import metadata
from timing.db.session import Session
from timing.db.middleware import SQLAlchemySessionManager
from timing.resources.register import RegisterResource
from timing.resources.time import TimesResource


register_resource = RegisterResource()
times_resource = TimesResource()


def create_app():
    app = falcon.API(
        middleware=[
            SQLAlchemySessionManager(Session)
        ]
    )
    app.add_route('/register', register_resource)
    app.add_route('/time/add', times_resource)
    app.add_route('/time/get', times_resource)

    # Setup tables
    table_utils.drop_tables(metadata)
    table_utils.create_tables(metadata)

    return app
