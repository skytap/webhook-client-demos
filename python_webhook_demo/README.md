# Skytap Python Event Streaming Demo
## Requirements:
* Python 2.7.10+
* flask
* apscheduler
* rq

## Using the tool
Clone the repo and install all the required python libraries.
Configure your Skytap information in `settings.py`

| Variable            | Purpose                                              |
|---------------------|------------------------------------------------------|
| SKYTAP_USERNAME     | Username to login your skytap account 				 |
| SKYTAP_API_TOKEN    | Skytap API token 	                                 |
| SKYTAP_HOSTNAME     | https://cloud.skytap.com by default              |
| SERVER_HOST         | This should be the same as the one you put in for the Webhook                           |
| SERVER_PORT         | This should be the same as the one you put in for the Webhook                          |
| SSL_VERIFY          | True by default. For security purpose, this variable should always be set to True			                         |
| DEBUG               | False by default.                          |


Below are the settings you need to fill out if you would like to send the data to your Splunk server

| Variable            | Purpose                                              |
|---------------------|------------------------------------------------------|
| SPLUNK_HOSTNAME     | Your Splunk hostname. It is set to Splunk cloud by default.                          |
| SPLUNK_PORT         | 8088 by default. Please specify the port if the default setting is different from yours                           |
| SPLUNK_EC_TOKEN     | Splunk Event collector token.                           |
| SPLUNK_EC_ENDPOINT  | Splunk Event collector endpoint                     |

## Run the application
```python app.py```

If you would like to send webhook data to Splunk, you should start the application with:
```python app.py --splunk```
