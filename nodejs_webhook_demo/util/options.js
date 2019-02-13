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
const minimist = require('minimist');

/**
This handles command line arguments. 
	Args: 
		splunk: False by default. Send Skytap events (JSON) format to Splunk if True.
*/ 
let args = minimist(process.argv.slice(2), {
  default: {
    splunk: false
  }
});

module.exports.args = args;