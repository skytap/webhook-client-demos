import sys
import os
import json
from lib.api import ApiController
from lib.utility import Utility


class SkytapDemo():
    def __init__(self, config):
        self.skytap = ApiController(config)
        self.utility = Utility()

    def run(self, result):
        vm_infos = self.utility.running_vms_from_payload(result)
        for env_id, vm_ids in vm_infos.items():
            for vm_id in vm_ids:
                self.skytap.suspend_vm(env_id, vm_id)
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        config = payload.get('configuration')
        result = payload.get('result')
        app = SkytapDemo(config)
        app.run(result)