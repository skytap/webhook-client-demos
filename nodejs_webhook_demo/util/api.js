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
const axios = require('axios');
const https = require('https');

const AUTH = {
  username: process.env.SKYTAP_USERNAME,
  password: process.env.SKYTAP_API_TOKEN
};

const HEADERS = {
  'Accept': 'application/json',
  'Content-Type': 'application/json'
};

const PARAMS = {
  'runstate': 'suspended'
};

const RUNNING_STATE = 'running';

function build_url(env_id, vm_id) {
  var endpoint = `/configurations/${env_id}/vms/${vm_id}`;
  return process.env.SKYTAP_HOSTNAME.concat(endpoint);
}

function vm_runstate(env_id, vm_id) {
  var result = axios.get(build_url(env_id, vm_id),
    {headers: HEADERS},
    {auth: AUTH}
  ).then(response => {
    var data = response.body.payload
    return data['runstate'];
  }).catch(error => {
    console.log(error)
  });
};

function is_vm_running(env_id, vm_id){
  return vm_runstate(env_id, vm_id) === RUNNING_STATE
};

function suspend_vms(env_id, vm_id) {
  axios.put(
    build_url(env_id, vm_id),
    PARAMS,
    {headers: HEADERS},
    {auth: AUTH}
  ).then(response => {
    return done();
  }).catch(error => {
    console.log(error);
  });
};

module.exports.suspend_vms = suspend_vms;
module.exports.is_vm_running = is_vm_running;
