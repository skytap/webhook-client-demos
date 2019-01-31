# Skytap NodeJS Event Streaming Demo
## Requirements:
* axios
* dotenv
* express
* minimist
* node-resque

## Using the tool
Clone the repo and install all the required python libraries.
Configure your Skytap and redis information in `.env`

| Variable            | Purpose                                              |
|---------------------|------------------------------------------------------|
| SKYTAP_USERNAME     | Username to login your skytap account 				 |
| SKYTAP_API_TOKEN    | Skytap API token 	                                 |
| SKYTAP_HOSTNAME     | https://cloud.skytap.com by default              |
| SERVER_HOST         | This should be the same as the one you put in for the Webhook                           |
| SERVER_PORT         | This should be the same as the one you put in for the Webhook                           |
| SSL_VERIFY          | True by default. For security purpose, this variable should always be set to True       |
| REDIS_PKG           | ioredis by default.                          |
| REDIS_HOST          | 127.0.0.1 by default. Please specify the host if it's different from the default setting|
| REDIS_PASSWORD      | null by default. Please specify the password if it's different from the default setting |
| REDIS_PORT          | 6379 by default. Please specify the port if it's different from the default setting     |
| REDIS_DATABASE      | 0 by default. Please specify the database if it's different from the default setting    |


Below are the settings you need to fill out if you would like to send the data to your Splunk server

| Variable            | Purpose                                              |
|---------------------|------------------------------------------------------|
| SPLUNK_HOSTNAME     | Your Splunk hostname. It is set to Splunk cloud by default.                          |
| SPLUNK_PORT         | 8088 by default. Please specify the port if it's different from the default setting  |
| SPLUNK_EC_TOKEN     | Splunk Event collector token.                           |
| SPLUNK_EC_ENDPOINT  | Splunk Event collector endpoint                     |

## Run the application
```node index.js```

If you would like to send webhook data to Splunk, you should start the application with:
```node index.js --splunk```
