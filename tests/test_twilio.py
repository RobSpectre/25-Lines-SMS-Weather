import unittest
import requests
from mock import Mock
from mock import patch
from .context import app


class TwiMLTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def assertTwiML(self, response):
        self.assertTrue("<Response>" in response.data, "Did not find " \
                "<Response>: %s" % response.data)
        self.assertTrue("</Response>" in response.data, "Did not find " \
                "</Response>: %s" % response.data)
        self.assertEqual("200 OK", response.status)

    def sms(self, body, path='/sms', number='+15555555555'):
        params = {
            'SmsSid': 'SMtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'Body': body,
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound',
            'FromCity': 'BROOKLYN',
            'FromState': 'NY',
            'FromZip': '11211'}
        return self.app.post(path, data=params)

    def call(self, path='/voice', number='+15555555555', digits=None):
        params = {
            'CallSid': 'CAtesting',
            'AccountSid': 'ACtesting',
            'From': number,
            'To': '+16666666666',
            'CallStatus': 'ringing',
            'ApiVersion': '2010-04-01',
            'Direction': 'inbound'}
        if digits:
            params['Digits'] = digits
        return self.app.post(path, data=params)


class ExampleTests(TwiMLTest):
    @patch.object(requests, 'get')
    def test_sms(self, mock_get):
        test_file = file('./tests/test_assets/good_response.json')
        mock_response = Mock()
        mock_response.text = test_file.read()
        mock_get.return_value = mock_response 
        response = self.sms("Test")
        self.assertTwiML(response)
        self.assertTrue("Location" in response.data, "App did not return " \
                "weather information, instead: %s" % response.data)

    @patch.object(requests, 'get')
    def test_smsInvalidLocation(self, mock_get):
        test_file = file('./tests/test_assets/bad_response.json')
        mock_response = Mock()
        mock_response.text = test_file.read()
        mock_get.return_value = mock_response 
        response = self.sms("Test")
        self.assertTwiML(response)
        self.assertFalse("Location" in response.data, "App did returned " \
                "weather information when it shouldn't have: %s" \
                % response.data)
