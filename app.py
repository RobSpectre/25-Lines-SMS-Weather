import os
import flask
import requests
import simplejson as json
from twilio import twiml
app = flask.Flask(__name__)


@app.route('/sms', methods=['GET', 'POST'])
def sms():
    response, data = twiml.Response(), None
    try:
        path = "http://api.wunderground.com/api/%s/conditions/q/%s.json" \
                % (os.environ.get('WUNDERGROUND_API_KEY', None),
                    flask.request.form['FromZip'])
        data = json.loads(requests.get(path).text)['current_observation']
    except:
        response.sms("No weather data could be found.")
    if data:
        response.sms("Location: %s\n Conditions: %s\n Temp: " \
            "%s\n Humidity: %s\n" % (data['observation_location']['city'],
                data['weather'], data['temp_f'], data['relative_humidity']))
    return str(response)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
