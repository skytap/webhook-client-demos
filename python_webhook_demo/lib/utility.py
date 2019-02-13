# Copyright 2019 Skytap Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
from options import Options


class Utility(object):
    """This class handles 

    1) Parsing command line argument.
    2) Parsing payload from Skytap auditing webhook.
    """

    def __init__(self):
        self.options = Options()

    def send_data_to_splunk(self):
        return self.options["splunk"]

    def running_vms_from_payload(self, raw_data):
        """This method filters audit events from Skytap webook.
        
        Args:
            raw_data (JSON): webhook event from Skytap.
        Returns:
            A dictionary contains dictionaries of environment id and vm ids 
            for all newly launched vms. 
        """
        result = {}
        data = json.loads(raw_data)
        for payload in data['payload']:
            if payload['type'] == 'Run Environment':
                result.update(self.process_payload(payload))
        return result

    def process_payload(self, payload):
        """This method proccess 'Run Environment' audit event from Skytap Webhook
         
        Args:
            payload (JSON): 'Run Environment' audit event from Skytap webhook.
        Returns:
            A dictionary of environment id and vm ids for the newly launched vms. 
        """
        vm_ids = []
        for op in payload['operated_on']:
            if op['resource_type'] == 'environment':
                env_id = op['id']
            elif i['resource_type'] == 'vm':
                vm_ids.append(op['id'])
        return {env_id: vm_ids}
