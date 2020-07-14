import falcon
from wsgiref import simple_server

from timing.db import table_utils
from timing.db.engine import metadata
from timing.db.session import Session
from timing.db.middleware import SQLAlchemySessionManager
from timing.resources.register import RegisterResource
from timing.resources.time import TimesResource


register_resource = RegisterResource()
times_resource = TimesResource()

# user = UserResource()
# time = TimeResource()

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

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()
