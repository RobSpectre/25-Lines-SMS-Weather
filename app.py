import os
import flask
import requests
import simplejson as json
from twilio import twiml
app = flask.Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    path = "http://api.wunderground.com/api/%s/conditions/q/%s/%s.json" \
            % (app.config['WUNDERGROUND_API_KEY'],
                    flask.request.form['FromState'],
                    flask.request.form['FromCity'].title().replace(' ', '_'))
    response = requests.get(path)
    current = json.loads(response.text)['current_observation']
    response = twiml.Response()
    response.sms("Location: %s\n Conditions: %s\n Temp: %s\n Humidity: %s\n" %
            (current['observation_location']['city'], current['weather'],
                current['temp_f'], current['relative_humidity']))
    return str(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
