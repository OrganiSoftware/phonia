#!/usr/bin/env python3

from bs4 import BeautifulSoup
import hashlib
import json
from lib.output import *
from requests import get


def scan(number, apiKey):
    if not args.scanner == 'numverify' and not args.scanner == 'all':
        return -1

    try:
        res = get("http://apilayer.net/api/validate?access_key="+apiKey+"&number="+number+"&country_code=&format=1")

        data = json.loads(res.content.decode('utf-8'))
    except Exception as e:
        error('Numverify.com is not available')
        return -1

    if res.content == "Unauthorized" or res.status_code != 200:
        error(("An error occured while calling the API (bad request or wrong api key)."))
        return -1

    if 'error' in data:
        error('Numverify.com is not available')
        return -1

    if data['valid'] == False:
        error(("Error: Please specify a valid phone number. Example: +6464806649"))
        sys.exit()

    InternationalNumber = '({}){}'.format(
        data["country_prefix"], data["local_format"])

    plus(("Number: ({}) {}").format(
        data["country_prefix"], data["local_format"]))
    plus(("Country: {} ({})").format(
        data["country_name"], data["country_code"]))
    plus(("Location: {}").format(data["location"]))
    plus(("Carrier: {}").format(data["carrier"]))
    plus(("Line type: {}").format(data["line_type"]))

    if data["line_type"] == 'landline':
        warn(("This is most likely a landline, but it can still be a fixed VoIP number."))
    elif data["line_type"] == 'mobile':
        warn(("This is most likely a mobile number, but it can still be a VoIP number."))
