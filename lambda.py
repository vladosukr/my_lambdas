from __future__ import print_function
import requests

def lambda_handler(event, context):
    records = []
    for record in event['Records']:
        url = record["body"]
        records.append(url)
    request(records)
    return records

def request(data):
    for url in data:
        print(url)
        site = str(url)
        response = requests.get(site)
        print(response)
        if response.status_code == 200:
            print ("OK")
        else:
            print("Please investigate")
