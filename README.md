# 25 Lines - SMS Weather 

A Twilio application that returns weather data for your area code in exactly 25
lines of code.

[![Build
Status](https://secure.travis-ci.org/RobSpectre/25-Lines-SMS-Weather.png)]
(http://travis-ci.org/RobSpectre/25-Lines-SMS-Weather)


## Summary

On a flight from LAX to SFO, I issued myself the challenge to build a compelling
Twilio app in 25 lines or less over the course of the 50 minute flight.  The
rules I set for myself were:

* It had to do something significant.  Couldn't be something silly like
  [Laughotron](http://www.laughotron.com/).
* Start to finish in *no more* than 25 lines, including whitespace.
* It had to pass my [PEP8](http://www.python.org/dev/peps/pep-0008/) vim plugin.
  No crazy single-line, more than 80 column shenanigans.
* Application had to be code complete by the time the Delta attendant started to
  scream at me for still operating an electronic device.
* It must withstand a reasonable amount of poor user input - no brittleware.

To accomplish this, I busted out the [Twilio Hackpack for Heroku and
Flask](https://github.com/RobSpectre/Twilio-Hackpack-for-Heroku-and-Flask) and
the [Weather Underground API](http://www.wunderground.com/weather/api/)
to make a super simple SMS weather reporter. 


## Usage

Text anything to (646) 606-2458 to see it work!

![Example of it
working](https://raw.github.com/RobSpectre/25-Lines-SMS-Weather/master/images/usage.png)


## Installation

Step-by-step on how to deploy, configure and develop this app.

### Deploy 

0) Get a developer API key from [Weather
Underground](http://www.wunderground.com/weather/api/).

1) Grab latest source
<pre>
git clone git://github.com/RobSpectre/25-Lines-SMS-Weather.git 
</pre>

2) Install dependencies
<pre>
make init
</pre>

3) Navigate to folder and create new Heroku Cedar app
<pre>
heroku create --stack cedar
</pre>

4) Deploy to Heroku
<pre>
git push heroku master
</pre>

5) Scale your dynos
<pre>
heroku scale web=1
</pre>

6) Configure a new TwiML app and Twilio phone number to use the app.
<pre>
python configure.py --account_sid ACxxxxxx --auth_token yyyyyyy -n -N
</pre>

8) Set your Weather Underground API key in your local and Heroku app environment
variables.
<pre>
export WUNDERGROUND_API_KEY=xxxxxxxxxx
heroku config:add WUNDERGROUND_API_KEY=xxxxxxxxxx
</pre>

8) Text the new number and get the weather!


### Configuration

This app hinges on your Weather Underground API key being set in your
environment.  This can be hardcoded into your app by changing the first string
substitution on line 14:

```python
path = "http://api.wunderground.com/api/%s/conditions/q/%s.json" \
        % ("xxxxxxxxxxx", flask.request.form['FromZip'])
```

Be sure not to expose your key (or any of your sensitive credentials) to a public GitHub repo.


### Development

Be sure to follow the configuration steps above and use this step-by-step guide to tweak to your heart's content.

1) Install the dependencies.
<pre>
make init
</pre>

2) Launch local development webserver
<pre>
foreman start
</pre>

3) Open browser to [http://localhost:5000](http://localhost:5000).

4) Tweak away on `app.py`.


## Testing

Of course its tested.  What is this? 1997?

<pre>
make test
</pre>



## Meta 

* No warranty expressed or implied.  Software is as is. Diggity.
* [MIT License](http://www.opensource.org/licenses/mit-license.html)
* Lovingly crafted by [Twilio New
 York](http://www.meetup.com/Twilio/New-York-NY/) 

[![githalytics.com
alpha](https://cruel-carlota.pagodabox.com/20e8a2e6e40a8df4a6db036953738711
"githalytics.com")](http://githalytics.com/RobSpectre/25-Lines-SMS-Weather)
