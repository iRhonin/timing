import falcon


class Authorization(object):

    def __call__(self, req, resp, resource, params):
        req.context['user_id'] = req.get_header('X-IDENTITY')

        if req.context['user_id'] is None:
            raise falcon.HTTPUnauthorized(
                'Auth token required',
                href='/register',
            )
