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
  axios: A module provides Promise based HTTP client for the browser and node.js
*/
const axios = require('axios');

/**
  This constructs the authentication header, required for Splunk API interaction.
*/
const HEADERS = {
  'Authorization': `Splunk ${process.env.SPLUNK_EC_TOKEN}`
};

/**
  This constructs the Splunk Event Collector endpoint.
*/
function build_url() {
  return `${process.env.SPLUNK_HOSTNAME}:${process.env.SPLUNK_PORT}/${process.env.SPLUNK_EC_TOKEN}`
};

/**
  This method post the event from Skytap to Splunk      
    Args:
      data (JSON): Event from Skytap. 

    Return: 
      done() if successful, log error on failure.
*/
function add(data){
  var event = {"event": data}
  var result = axios.post(build_url(),
              event,
              {headers: HEADERS}
              ).then(response => {
                return done();
              }).catch(error => {
                console.log(error);
              });
};

module.exports.add = add;