function running_vms_from_payload(data) {
  if (data['type'] == 'Run Environment') {
      var op_array = data['operated_on'];
      return process_payload(op_array);
  }
}

function process_payload(op_array) {
  var vm_ids = [];
  for (i = 0; i < op_array.length; i++) {
    if (op_array[i]['resource_type'] === 'environment') {
      var env_id = op_array[i]['id'];
    } else if (op_array[i]['resource_type'] === 'vm') {
      vm_ids.push(op_array[i]['id']);
    }
  }
  return {[env_id]: vm_ids};
}

module.exports.running_vms_from_payload = running_vms_from_payload;
