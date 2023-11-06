import requests
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
clientId = os.getenv('CLIENT_ID')


headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

# Verify users only if you will send them a massage otherwise you may be banned from whatsapp
def verifyUserIdentity(phone):

    payload = {
        "id": "{{$guild}}",
        "to": "postmaster@wa.gw.msging.net",
        "method": "get",
        "uri": f"lime://wa.gw.msging.net/accounts/+55{phone}"
    }

    r = requests.post(f'https://{clientId}.http.msging.net/commands', data=json.dumps(payload), headers=headers)

    return r


def sendNotification(namespace, teamplateName, costumersId, userName):

    payload = {
        "id": "{{$guid}}",
        "to": costumersId,
        "type": "application/json",
        "content": {
            "type": "template",
            "template": {
                "namespace": namespace,
                "name": teamplateName,
                "language": {
                    "code": "pt_BR",
                    "policy": "deterministic"
                },
                "components": [
                    {
                        "type": "header",
                        "parameters": [
                            {
                                "type": "image",
                                "image": {
                                    "link": "<IMAGE_URL>"
                                }
                            }
                        ]
                    },
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "text": userName
                            }
                        ]
                    }
                ]
            }
        }
    }

    r = requests.post(f'https://{clientId}.http.msging.net/messages', data=json.dumps(payload), headers=headers)

    return r


def format_phone_number(phone):

    phone = phone.replace(" ", "")
    # Regular expression pattern to match different parts of the phone number
    pattern = r'(\+\d{0,2})?(\(?\d{2}\)?)?(\d{3,10})-?(\d{0,4})'

    # Attempt to match the pattern in the input phone number string
    match = re.match(pattern, phone)

    # Check if a match is found
    if match:
        # Extract different parts of the phone number using groups in the regex pattern
        # Group 1: Country code (optional, may not be present)
        country_code = match.group(1)
        state_code = match.group(2).strip('()')  # Group 2: State code
        # Groups 3 and 4: Phone number digits
        phone_digits = ''.join(match.groups()[2:4])

        # Create the formatted phone number string
        formatted_number = f'{state_code}{phone_digits}'

        # Return the formatted phone number
        return formatted_number
    else:
        # If no match is found, return the original phone number as is
        return phone
