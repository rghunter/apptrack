from desmond.settings import *  ## import the base settings
from urllib2 import Request, urlopen
import json


## Setup Mailtrap
request = Request("https://mailtrap.io/api/v1/inboxes.json?api_token={}".format(os.environ['MAILTRAP_API_TOKEN']))
response_body = urlopen(request).read()
credentials = json.loads(response_body)[0]

EMAIL_HOST = credentials['domain']
EMAIL_HOST_USER = str(credentials['username'])
EMAIL_HOST_PASSWORD = str(credentials['password'])
EMAIL_PORT = credentials['smtp_ports'][2]

DEBUG = False
ALLOWED_HOSTS = ['bts-scholarship.herokuapp.com']

