import falcon
import pandas as pd

import db

class Home:
    def on_get(self, req, resp):
        df = pd.read_sql_table('masters', con=db.engine, index_col='id')

        display_names = {
            'name': 'Kung Foo Master',
            'style': 'Style'
        }
        df.rename(columns=display_names, inplace=True)
        html = df.to_html(index=False)

        resp.content_type = falcon.MEDIA_HTML
        resp.body = html

api = falcon.API()
api.add_route('/', Home())
