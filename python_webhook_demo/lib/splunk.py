import requests
import json

class SplunkController(object):
    def __init__(self, config):
        self.hostname = config['SPLUNK_HOSTNAME']
        self.port = config['SPLUNK_PORT']
        self.ec_endpoint = config['SPLUNK_EC_ENDPOINT']
        self.token = config['SPLUNK_EC_TOKEN']
        self.ssl_verification = config['SSL_VERIFY']
        return None

    def build_endpoint(self):
        return "%s:%s/%s" % (self.hostname,
                             self.port,
                             self.ec_endpoint)

    def build_header(self):
        splunk_token = "Splunk %s" % self.token
        return {"Authorization": splunk_token}

    def add(self, data):
        event = {"event": data}
        result = requests.post(self.build_endpoint(),
                               headers=self.build_header(),
                               json=event,
                               verify=self.ssl_verification)
        return result.text