import urllib.request as urllib2
import json


def analisaSentimento(text):
    data = {
        "Inputs": {
            "input1":
                [
                    {
                        'tweet_text': text,
                        'sentiment': ".",
                    }
                ],
        },
        "GlobalParameters": {
        }
    }

    body = str.encode(json.dumps(data))

    url = 'https://ussouthcentral.services.azureml.net/workspaces/8cddcc2282d943c1a09fdacbe4b9475f/services/6bed1d3f513640d4b4624a94617d6a11/execute?api-version=2.0&format=swagger'
    api_key = 'nsYJxPVxmiN8qDtuCJcRgfFD4KE/ChfDXDV1vsXvmTP6kVAkTMS9FYDJtzcm5V5qYSOvvwDbHkNY1rpEFVHZYw=='  # Replace this with the API key for the web service
    headers = {'Content-Type': 'application/json', 'Authorization': ('Bearer ' + api_key)}

    req = urllib2.Request(url, body, headers)

    try:
        response = urllib2.urlopen(req)

        result = json.loads(response.read())
        chave = result['Results']
        lista = chave['output1'][0]

        return lista['Scored Labels']

    except urllib2.HTTPError as error:
        print("The request failed with status code: " + str(error.code))

        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read()))