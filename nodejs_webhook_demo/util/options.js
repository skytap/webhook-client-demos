const minimist = require('minimist');

let args = minimist(process.argv.slice(2), {
  default: {
    splunk: false
  }
});

module.exports.args = args;