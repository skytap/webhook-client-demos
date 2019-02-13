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

import requests


class ApiController():
    """This class handles communication with the Skytap API.""" 

    def __init__(self, config):
        self.username = config['SKYTAP_USERNAME']
        self.api_token = config['SKYTAP_API_TOKEN']
        self.hostname = config['SKYTAP_HOSTNAME']
        self.ssl_verification = config['SSL_VERIFY']
        self.RUNNING_STATE = 'running'
        return None

    def build_auth(self):
        """This method construct the authentication, required for all API interaction."""
        return (self.username, self.api_token)

    def build_header(self):
        """This constructs the header, required for all API interaction."""
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return headers

    def build_vm_endpoint(self, env_id, vm_id):
        """This constructs the vm endpoint.

        Args: 
            env_id (str): Environment id. It is also referred as the configuration id. 
            vm_id (str): VM id. 
        """ 
        endpoint = '/configurations/%s/vms/%s' % (env_id, vm_id)
        return self.hostname + endpoint

    def vm_runstate(self, env_id, vm_id):
        """This method return the state of the specified vm.

        Args: 
            env_id (str): Environment id. It is also referred as the configuration id. 
            vm_id (str): VM id. 

        Returns: 
            The state of the vm.
        """
        result = requests.get(self.build_vm_endpoint(env_id, vm_id),
                              headers=self.build_header(),
                              auth=self.build_auth(),
                              verify=self.ssl_verification)

        data = result.json()
        return data['runstate']

    def is_vm_running(self, env_id, vm_id):
        """This method checks if the vm is in running state
        
        Args: 
            env_id (str): Environment id. It is also referred as the configuration id. 
            vm_id (str): VM id. 

        Returns: 
            True if the vm is running, throws exception on failure
        """
        if self.vm_runstate(env_id, vm_id) == self.RUNNING_STATE:
            return True
        raise(ValueError, 'vm is not in running state.')

    def suspend_vm(self, env_id, vm_id):
        """This method suspends vm

        Args: 
            env_id (str): Environment id. It is also referred as the configuration id. 
            vm_id (str): VM id. 

        Returns: 
            True if successful, throws exception on failure.
        """
        params = {'runstate': 'suspended'}

        if self.is_vm_running(env_id, vm_id):
            result = requests.put(self.build_vm_endpoint(env_id, vm_id),
                                  headers=self.build_header(),
                                  auth=self.build_auth(),
                                  params=params,
                                  verify=self.ssl_verification)
            return True
