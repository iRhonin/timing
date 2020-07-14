class Paginate(object):
    def __init__(self, offset=0, limit=10, max_limit=100):
        self.max_limit = max_limit
        self.offset = offset
        self.limit = limit

    def __call__(self, req, resp, resource, params):
        req.context['limit'] = min(
            int(req.headers.get('X-LIMIT') or self.limit),
            self.max_limit,
        )
        req.context['offset'] = int(req.headers.get('X-OFFSET') or self.offset)
