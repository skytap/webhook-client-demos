# Skytap Webhook Demo 
The Skytap webhook demo provides NodeJS and Python sample applications that show how to retrieve data from a Skytap webhook. The demo suspends any newly launched virtual machines in your Skytap account, based on the event it receives from the Skytap webhook, and it provides an example to send the Skytap event to a security information and event management (SIEM) tool, such as Splunk.

## Before You Begin 
Before you begin, please make sure you have the following:

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

## Install and Run the Skytap Webhook Demo
Clone the webhook demo repo and install the required libraries and packages.

#### NodeJS Webhook Demo:
1. Configure your Skytap and redis information in `.env`

    | Variable Name       | Description                                                                                 |
    |---------------------|---------------------------------------------------------------------------------------------|
    | SKYTAP_USERNAME     | Your Skytap user name.                                                                      |
    | SKYTAP_API_TOKEN    | Your Skytap API token.                                                                      |
    | SKYTAP_HOSTNAME     | https://cloud.skytap.com by default.                                                        |
    | SERVER_HOST         | The **Webhook URL** that you specified in Skytap settings.                                  |
    | SERVER_PORT         | The **Webhook URL** port that you specified in Skytap settings (default is `443`).          |
    | SSL_VERIFY          | `True` by default. For security purposes, this variable should always be set to `True`.     |
    | REDIS_PKG           | `ioredis` by default.                                                                       |
    | REDIS_HOST          | `127.0.0.1` by default. Specify the host if you don't use the default.                      |
    | REDIS_PASSWORD      | null by default. Specify the password if you don't use the default.                         |
    | REDIS_PORT          | `6379` by default. Specify the port if you don't use the default.                           |
    | REDIS_DATABASE      | `0` by default. Specify the database if you don't use the default.                          |

    If you want to send webhook data to Splunk, configure these additional settings:

    | Variable Name       | Description                                                                                 |
    |---------------------|---------------------------------------------------------------------------------------------|
    | SPLUNK_HOSTNAME     | Your Splunk hostname. It is set to Splunk cloud by default.                                 |
    | SPLUNK_PORT         | `8088` by default. Please specify the port if it's different from the default setting.      |
    | SPLUNK_EC_TOKEN     | The Splunk event collector token.                                                           |
    | SPLUNK_EC_ENDPOINT  | The Splunk event collector endpoint                                                         |

2. Navigate to the directory containing the app.py file and enter the following at the command line:

    ```node index.js```
    
3. If you want to send webhook data to Splunk, start the application with the following command:

    ```node index.js --splunk```

#### Python Webhook Demo:

1. Configure your Skytap information in `settings.py`

    | Variable Name       | Description                                                                                 |
    |---------------------|---------------------------------------------------------------------------------------------|
    | SKYTAP_USERNAME     | Your Skytap user name.                                                                      |
    | SKYTAP_API_TOKEN    | Your Skytap API token.                                                                      |
    | SKYTAP_HOSTNAME     | `https://cloud.skytap.com` by default.                                                      |
    | SERVER_HOST         | The **Webhook URL** that you specified in Skytap settings.                                  |
    | SERVER_PORT         | The **Webhook URL** port that you specified in Skytap settings (default is `443`).          |
    | SSL_VERIFY          | `True` by default. For security purposes, this variable should always be set to `True`.     |
    | DEBUG               | `False` by default.                                                                         |

    If you want to send webhook data to Splunk, configure these additional settings:

    | Variable Name       | Description                                                                                 |
    |---------------------|---------------------------------------------------------------------------------------------|
    | SPLUNK_HOSTNAME     | Your Splunk hostname. It is set to Splunk cloud by default.                                 |
    | SPLUNK_PORT         | `8088` by default. Please specify the port if the default setting is different from yours.  |
    | SPLUNK_EC_TOKEN     | The Splunk event collector token.                                                           |
    | SPLUNK_EC_ENDPOINT  | The Splunk event collector endpoint                                                         |

2. Navigate to the directory containing the app.py file and enter the following at the command line:

    ```python app.py```
    
3. If you want to send webhook data to Splunk, start the application with the following command:

    ```python app.py --splunk```

## License
Apache; see [LICENSE](LICENSE) for details.
