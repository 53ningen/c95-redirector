from chalice import Chalice, Response

app = Chalice(app_name='c95-redirector')

def getRedirectResponse(url):
    return Response(body='', status_code=301, headers={'Content-Type': 'text/plain', 'Location': url})

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/kumamoto/airportbus-timetables')
def kumamoto_airportBusTimetables():
    url = 'https://www.kyusanko.co.jp/sankobus/airport/limousine/'
    return getRedirectResponse(url)

@app.route('/kumamoto/citytram-timetables')
def kumamoto_cityTramTimeTables():
    url = 'http://www.kotsu-kumamoto.jp/timetable/pub/rosen.aspx?c_id=42'
    return getRedirectResponse(url)

