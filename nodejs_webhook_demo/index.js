require('dotenv').config();
const express = require('express');
const app = express();
const bodyParser = require('body-parser');

let kue = require('kue');
let queue = kue.createQueue();

app.use(bodyParser.json());

app.get('/', function(req, res) {
	console.log(dotenv.parsed.SKYTAP_USERNAME)
  	let vmInfoJob = queue.create('process_running_vms', {
          payload: req.body.payload
  	})
  	.removeOnComplete(true)
  	.save();

  	res.status(200).send('OK');
});

app.listen(process.env.SERVER_PORT, process.env.SERVER_HOSTNAME, () => {
	console.log('Example app listening on port 8080!');
});