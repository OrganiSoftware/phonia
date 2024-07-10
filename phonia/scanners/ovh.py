#!/usr/bin/env python3

import requests
from lib.output import *


def scan(localNumber, numberCountry):
    if not args.scanner == 'ovh' and not args.scanner == 'all':
        return -1

    test('Running OVH scan...')

    querystring = {"country": numberCountry.lower()}

    headers = {
        'accept': "application/json",
        'cache-control': "no-cache"
    }

    try:
        response = requests.request(
            "GET", "https://api.ovh.com/1.0/telephony/number/detailedZones", data="", headers=headers, params=querystring)
        data = json.loads(response.content.decode('utf-8'))
    except Exception as e:
        error('OVH API is unreachable.')
        return -1

    if isinstance(data, list):
        askedNumber = "0" + localNumber.replace(localNumber[-4:], 'xxxx')

        for voip_number in data:
            if voip_number['number'] == askedNumber:
                plus(("One result found in OVH database!"))
                info(("Number range: {}".format(voip_number['number'])))
                info(("City: {}".format(voip_number['city'])))
                info(("Zip code: {}".format(
                    voip_number['zipCode'] if voip_number['zipCode'] is not None else ''
                )))
                askForExit()
