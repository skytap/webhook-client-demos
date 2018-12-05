let kue = require('kue');
let queue = kue.createQueue()
let skytap = require('./util/api');

queue.process('process_running_vms', (job, done) => {
        running_vms_from_payload(job.data.payload, done);
});

queue.process('suspend_running_vms', (job, done) => {
  console.log('Working on suspending working vms');
  skytap.suspend_vms(job.data.vm_info ,done);
});

function running_vms_from_payload(data, done) {
  var result = []
  for (i = 0; i < data.length; i++) {
    if (data[i]['type'] == 'Run Environment'){
      var op_array = data[i]['operated_on']
      env_id = determine_environment_id(op_array);
      for (j = 0; j < op_array.length; j++){
        if(op_array[j]['resource_type'] == 'vm'){
          console.log([env_id, op_array[j]['id']])
          let suspendVmJob = queue.create('suspend_running_vms', {
            vm_info: [env_id, op_array[j]['id']]
          })
          .removeOnComplete(true)
          .save();
        }
      }
    }
  }
  return done();
}

function determine_environment_id(data) {
  for (i = 0; i < data.length; i ++){
    if (data[i]['resource_type'] == 'environment'){
      return data[i]['id'];
    }
  }
}