# Copyright 2019 Skytap Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import json

class SplunkController(object):
    """This class handles commnunication with the Splunk Event Collector."""
    def __init__(self, config):
        self.hostname = config['SPLUNK_HOSTNAME']
        self.port = config['SPLUNK_PORT']
        self.ec_endpoint = config['SPLUNK_EC_ENDPOINT']
        self.token = config['SPLUNK_EC_TOKEN']
        self.ssl_verification = config['SSL_VERIFY']
        return None

    def build_endpoint(self):
        """This constructs the Splunk Event Collector endpoint."""
        return "%s:%s/%s" % (self.hostname,
                             self.port,
                             self.ec_endpoint)

    def build_header(self):
        """This constructs the authentication header, required for Splunk API interaction."""
        splunk_token = "Splunk %s" % self.token
        return {"Authorization": splunk_token}

    def add(self, data):
        """This method post the event from Skytap to Splunk
        
        Args:
            data (JSON): Event from Skytap. 

        Return: 
            Request result
        """
        event = {"event": data}
        result = requests.post(self.build_endpoint(),
                               headers=self.build_header(),
                               json=event,
                               verify=self.ssl_verification)
        return result.text