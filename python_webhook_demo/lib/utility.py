import json
from options import Options


class Utility(object):
    def __init__(self):
        self.options = Options()

    def send_data_to_splunk(self):
        return self.options["splunk"]

    def running_vms_from_payload(self, raw_data):
        result = {}
        data = json.loads(raw_data)
        for payload in data['payload']:
            if payload['type'] == 'Run Environment':
                result.update(self.process_payload(payload))
        return result

    def process_payload(self, payload):
        vm_ids = []
        for op in payload['operated_on']:
            if op['resource_type'] == 'environment':
                env_id = op['id']
            elif i['resource_type'] == 'vm':
                vm_ids.append(op['id'])
        return {env_id: vm_ids}
