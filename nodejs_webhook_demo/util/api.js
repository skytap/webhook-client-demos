const axios = require('axios');
const https = require('https');

var auth = {
        username: process.env.SKYTAP_USERNAME,
        password: process.env.SKYTAP_API_TOKEN
};

var headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
};

var params = {
        'runstate': 'suspended'
};


function suspend_vms(vm_info, done) {
    console.log(`in suspend vm: ${vm_info}`)
    var url = `${process.env.SKYTAP_HOSTNAME}/configurations/${vm_info[0]}/vms/${vm_info[1]}`
    axios.put(
            url,
            params,
            {headers: headers},
            {auth: auth},
            {httpsAgent: new https.Agent({
                rejectUnauthorized: false
                })
            }
        ).then(response => {
            return done();
        }).catch(error => {
            console.log(error);
        })
}

module.exports.suspend_vms = suspend_vms;