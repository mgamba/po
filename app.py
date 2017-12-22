import falcon
import pandas

class Home:
    def on_get(self, req, resp):
        header = ['Kung Foo Master','Style']
        data = [['Master Po Ping', 'Improvised and Panda Kung Fu'],
                ['Master Shifu', 'Red Panda Kung Fu'],
                ['Grand Master Oogway', 'Shaolinquan and T\'ai chi ch\'uan'],
                ['Master Tigress', 'Black Tiger Kung Fu'],
                ['Master Viper', 'Viper Kung Fu'],
                ['Master Monkey', 'Monkey Kung Fu'],
                ['Master Mantis', 'Southern Praying Mantis Kung Fu'],
                ['Master Crane', 'Fujian White Crane Kung Fu']]

        df = pandas.DataFrame(data, columns=header)
        html = df.to_html()

        resp.content_type = falcon.MEDIA_HTML
        resp.body = html

api = falcon.API()
api.add_route('/', Home())
