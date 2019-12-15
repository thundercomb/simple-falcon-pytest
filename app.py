import falcon
import json
import os
import requests

TYPICODE_URL = 'https://jsonplaceholder.typicode.com/posts/1'

class App:

    def on_get(self, req, resp, msg_id):
        error_flag = True

        try:
            r = requests.get(TYPICODE_URL)
        except ConnectionError:
            body = 'URL not found'
        else:
            if r.status_code == 200:
                body = (
                    r.json()
                )
            else:
                body = f'Request returned {r.status_code}'
        finally:
            resp.status_code = falcon.HTTP_200
            resp.content_type = falcon.MEDIA_JSON
            resp_body = r.json()
            resp.data = (
                json.dumps(resp_body, ensure_ascii=False)
                    .encode('utf-8')
            )

application = falcon.API()
application.req_options.auto_parse_form_urlencoded = True
application.add_route('/messages/{msg_id}', App())


def create():
    return application
