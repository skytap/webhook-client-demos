import argparse


parser = argparse.ArgumentParser(description='Skytap Python Webhook Demo')
parser.add_argument('--splunk', default=False, action='store_true', help='Send Skytap events (JSON) format to Splunk', required=False)

class Options(object):
    def __new__(cls):
        args = vars(parser.parse_args())
        return args