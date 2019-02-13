// Copyright 2019 Skytap Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
const NodeResque = require('node-resque');
let utility = require('./util/utility');
let skytap = require('./util/api');

const connectionDetails = {
  pkg: process.env.REDIS_PKG,
  host: process.env.REDIS_HOST,
  password: process.env.REDIS_PASSWORD,
  port: process.env.REDIS_PORT,
  database: process.env.REDIS_DATABASE
};

class JobPlugin extends NodeResque.Plugin {
  beforePerform() {
    var env_id = this.args[0];
    var vm_id = this.args[1];
    return skytap.is_vm_running(env_id, vm_id);
  }
};

const jobs = {
  'process_running_vms': {
    perform: (data) => {
      let vm_info = utility.running_vms_from_payload(data);
      for (var env_id in vm_info) {
        vm_info[env_id].forEach(function(vm_id) {
          addToSuspendQueue(env_id, vm_id);
        });
      }
      return 'Done';
    }
  },
  'suspend_running_vms': {
    plugins: [JobPlugin, 'Retry'],
    pluginOptions: {
      JobPlugin: {},
      Retry: {
        retryLimit: 5,
        retryDelay: 1000
      }
    },
    perform: (env_id, vm_id) => {
      skytap.suspend_vms(env_id, vm_id)
      return "Done"
    }
  }
};

const queue = new NodeResque.Queue({connection: connectionDetails }, jobs)
const worker = new NodeResque.Worker({ connection: connectionDetails, queues: ['processVM', 'suspendVM'] }, jobs)


function addToSuspendQueue(env_id, vm_id) {
  enqueue('suspendVM', 'suspend_running_vms', [env_id, vm_id])
};

async function startWorker(){
  await worker.connect()
  worker.start()
  worker.on('start', () => { console.log('worker started') })
  worker.on('failure', (queue, job, failure) => { console.log(`job failure ${queue} ${JSON.stringify(job)} >> ${failure}`) })
  worker.on('error', (error, queue, job) => { console.log(`error ${queue} ${JSON.stringify(job)}  >> ${error}`) })
  worker.on('pause', () => { console.log('worker paused') })
  return worker
};

function startQueue () {
  queue.on('error', function (error) { console.log(error) })
  queue.connect()
};

function enqueue (queue_name, job, data){
 queue.enqueue(queue_name, job, data)
};

startWorker()
startQueue()
module.exports.enqueue = enqueue;
