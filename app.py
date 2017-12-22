import falcon
import pandas as pd

import db

class Home:
    def on_get(self, req, resp):
        header = ['Kung Foo Master','Style']

        df = pd.read_sql_query('select * from masters', con=db.engine)
        html = df.to_html()

        resp.content_type = falcon.MEDIA_HTML
        resp.body = html

api = falcon.API()
api.add_route('/', Home())
