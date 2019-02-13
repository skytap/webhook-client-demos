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

/**
This method filters audit events from Skytap webook.       
  Args:
      raw_data (JSON): webhook event from Skytap.
  Returns:
      A dictionary contains of environment id and vm ids 
      for the newly launched vms. 
*/
function running_vms_from_payload(data) {
  if (data['type'] == 'Run Environment') {
      var op_array = data['operated_on'];
      return process_payload(op_array);
  }
}

/**
This method proccess 'Run Environment' audit event from Skytap Webhook
  Args:
      payload (JSON): 'Run Environment' audit event from Skytap webhook.
  Returns:
      A dictionary of environment id and vm ids for the newly launched vms. 
*/
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
