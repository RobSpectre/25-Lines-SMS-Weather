import os
import flask
import requests
import simplejson as json
from twilio import twiml
app = flask.Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    path = "http://api.wunderground.com/api/%s/geolookup/conditions/q/%s/%s.json" \
            % (app.config['WUNDERGROUND_API_KEY'],
                    flask.request.form['FromState'],
                    flask.request.form['FromCity'].title().replace(' ', '_'))
    print path
    response = requests.get(path)
    conditions = json.loads(response.text)
    current = conditions['location']['city']['current_observation']
    response = twiml.Response()
    response.sms("Conditions: %s, Temp: %s, Humidity: %s" % (current['weather'],
        current['temp_f'], current['relative_humidity']))
    return str(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
