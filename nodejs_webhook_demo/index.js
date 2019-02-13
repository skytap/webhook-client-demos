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
require('dotenv').config();
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
var options = require('./util/options');
var splunk = require('./util/splunk');
var worker = require('./worker');

app.use(bodyParser.json());

app.post('/', function(req, res) {
  if (options.args['splunk'] === true){
    splunk.add(req.body.payload);
  }
  worker.enqueue('processVM', 'process_running_vms', req.body.payload);
  res.status(200).send('OK');
});

app.listen(process.env.SERVER_PORT, process.env.SERVER_HOSTNAME, () => {
  console.log('Example app listening on port 8080!');
});
