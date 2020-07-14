import falcon

from timing.db.middleware import SQLAlchemySessionManager


# user = UserResource()
# time = TimeResource()
from timing.db.session import Session

app = falcon.API(
    middleware=[
        SQLAlchemySessionManager(Session)
    ]
)

# app.add_route('/register', register_resource)
# app.add_route('/time', user_resource)
