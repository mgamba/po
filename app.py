import falcon

class Home:
    def on_get(self, req, resp):
        html = """
                <!DOCTYPE html>
                <html>
                <body>
                  <h1>Hello.</h1>
                </body>
                </html>
               """

        resp.content_type = falcon.MEDIA_HTML
        resp.body = html

api = falcon.API()
api.add_route('/', Home())
