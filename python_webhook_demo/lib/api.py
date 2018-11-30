import requests


class ApiController():
    def __init__(self, config):
        self.username = config['SKYTAP_USERNAME']
        self.api_token = config['SKYTAP_API_TOKEN']
        self.hostname = config['SKYTAP_HOSTNAME']
        self.ssl_verification = config['SSL_VERIFY']
        self.RUNNING_STATE = 'running'
        return None

    def build_auth(self):
        return (self.username, self.api_token)

    def build_header(self):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        return headers

    def build_url(self, env_id, vm_id):
        endpoint = '/configurations/%s/vms/%s' % (env_id, vm_id)
        return self.hostname + endpoint

    def vm_runstate(self, env_id, vm_id):
        result = requests.get(self.build_url(env_id, vm_id),
                              headers=self.build_header(),
                              auth=self.build_auth(),
                              verify=self.ssl_verification)

        data = result.json()
        return data['runstate']

    def is_vm_running(self, env_id, vm_id):
        if self.vm_runstate(env_id, vm_id) == self.RUNNING_STATE:
            return True
        raise(ValueError, 'vm is not in running state.')

    def suspend_vm(self, env_id, vm_id):
        params = {'runstate': 'suspended'}

        if self.is_vm_running(env_id, vm_id):
            result = requests.put(self.build_url(env_id, vm_id),
                                  headers=self.build_header(),
                                  auth=self.build_auth(),
                                  params=params,
                                  verify=self.ssl_verification)
        return None
