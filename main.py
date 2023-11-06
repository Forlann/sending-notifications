from bigquery import get_client
from functions import verifyUserIdentity, sendNotification, format_phone_number
import os

teamplate_name = '<YOUR_TEAMPLATE_NAME>'

# JSON key provided by Google
json_key = 'bigquery_credencials.json'

client = get_client(json_key_file=json_key, readonly=True)

query = client.query("""
#standardSQL
  SELECT
    *
  FROM your_data_base LIMIT 1000
""")

# Extract query result
results= query[1]

for user in results:
  # Extract dataframe data
  rawPhone = user['phone']
  rawName = user['name']

  phone = format_phone_number(rawPhone)

  rawName = rawName.split()
  userName = rawName[0].capitalize()

  # Verify and send notification to user
  userData = verifyUserIdentity(phone)
  userData = userData.json()
  
  # Extract user identity
  identity = userData["resource"]["identity"]

  sendNotification(os.getenv('NAMESPACE'), teamplate_name, identity, userName)
