const axios = require('axios');


const HEADERS = {
  'Authorization': `Splunk ${process.env.SPLUNK_EC_TOKEN}`
};

function build_url() {
  return `${process.env.SPLUNK_HOSTNAME}:${process.env.SPLUNK_PORT}/${process.env.SPLUNK_EC_TOKEN}`
};

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