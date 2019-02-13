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
    # Sending all Skytap webhook data to Splunk
    if utility.send_data_to_splunk():
        splunk.add(request.data)
    vm_infos = utility.running_vms_from_payload(request.data)

    # Sending all the suspension vm task to a queue
    for env_id, vm_ids in vm_infos.items():
        for vm_id in vm_ids:
            worker.enqueue(skytap.suspend_vm, (env_id, vm_id,))
    return "OK"


if __name__ == '__main__':
    app.run(host=app.config['SERVER_HOST'],
            port=app.config['SERVER_PORT'],
            debug=app.config['DEBUG'],
            threaded=True)
