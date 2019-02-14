# Skytap Webhook Demo 
The Skytap webhook demo provides sample applications in both NodeJS and Python. The application demonstrates how to retrieve data from Skytap Event Streaming. The application will suspend any newly launched virtual machines in your Skytap account based on the event it receives from Skytap Event Streaming. The application also provides an example to send your Skytap Event to SIEM tool, like Splunk.

## Before You Begin 
Before you begin, please make sure you have:

##### NodeJS Webhook Demo:
* Node v8.0.0+
* [Redis](https://redis.io/topics/quickstart)
* Node modules:
    * axios
    * dotenv
    * express
    * minimist
    * node-resque
    * body-parser

##### Python Webhook Demo: 
* Python 2.7.10+
* [Redis](https://redis.io/topics/quickstart)
* Python libraries:
    * apscheduler
    * rq
    * redis

## Installing and Running the Skytap Webhook Demo
Clone the webhook demo repo based on your langugae preference and install all the required libraries and packages.

#### NodeJS Webhook Demo:
1. Configure your Skytap and redis information in `.env`

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

2. Navigate to the directory containing the app.py file and enter the following at the command line:
    ```node index.js```
3. If you would like to send webhook data to Splunk, you should start the application with:
    ```node index.js --splunk```

#### Python Webhook Demo:

1. Configure your Skytap information in `settings.py`

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

2. Navigate to the directory containing the app.py file and enter the following at the command line:

    ```python app.py```
    
3. If you would like to send webhook data to Splunk, you should start the application with:

    ```python app.py --splunk```

## License
MIT; see [LICENSE](LICENSE) for details.
