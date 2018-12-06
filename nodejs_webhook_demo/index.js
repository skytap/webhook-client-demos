require('dotenv').config();
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
var worker = require('./worker');

app.use(bodyParser.json());

app.post('/', function(req, res) {
  worker.enqueue('processVM', 'process_running_vms', req.body.payload);
  res.status(200).send('OK');
});

app.listen(process.env.SERVER_PORT, process.env.SERVER_HOSTNAME, () => {
  console.log('Example app listening on port 8080!');
});
