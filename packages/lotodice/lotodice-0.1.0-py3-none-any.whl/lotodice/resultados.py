#!/usr/bin/env python3

import requests
import json


def resultado(jogo="megasena"):
    # Make the HTTP request
    response = requests.get('https://loteriascaixa-api.herokuapp.com/api/{}/latest'.format(jogo))

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract the 'dezenas' array and join its elements with a comma
    result = ','.join(map(str, data['dezenas']))
    return result

def resultado_mega():
    return resultado()

def resultado_quina():
    return resultado(quina)
