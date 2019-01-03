import sys
from flask import Flask, request
from worker import StartWorker
from lib.utility import Utility
from lib.api import ApiController
from lib.splunk import SplunkController


app = Flask(__name__)
app.config.from_object('settings')

skytap = ApiController(app.config)
splunk = SplunkController(app.config)
utility = Utility()
worker = StartWorker()

@app.route('/', methods=['POST'])
def webhook():
    if utility.send_data_to_splunk():
        splunk.add(request.data)
    vm_infos = utility.running_vms_from_payload(request.data)
    for env_id, vm_ids in vm_infos.items():
        for vm_id in vm_ids:
            worker.enqueue(skytap.suspend_vm, (env_id, vm_id,))
    return "OK"


if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'],
            port=app.config['SERVER_PORT'],
            debug=app.config['DEBUG'],
            threaded=True)
