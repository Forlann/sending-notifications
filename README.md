# README

This repository contains a Python script that interacts with Google BigQuery to query a database and send a notification in whatsapp. The script also includes functions for verifying user identity. Below is an overview of the updated code and its functionality.

## Setup

1. Create a `.env` file in the same directory as your script and add the following variables:
   ```
    CLIENT_ID = <YOUR_CLIENT_ID>
    TOKEN = <YOUR_TOKEN>
    NAMESPACE = <YOUR_NAMESPACE>
   ```

   Replace `<YOUR_TOKEN>` and `<YOUR_CLIENT_ID>` with your TakeBlip and Bot credentials. `NAMESPACE` should be set to the appropriate WhatsApp namespace you want to use for sending notifications.

2. Replace `<YOUR_TEAMPLATE_NAME>` in the `teamplate_name` variable with the appropriate template name you want to use.

3. Ensure you have a JSON key file (`bigquery_credencials.json`) provided by Google for authentication. Place the JSON key file in the same directory as your script.

## Usage

Run the script using the following command:

```
python script_name.py
```

This will execute the script, querying the specified BigQuery database. The script will also verify user identity and send notifications to the users based on the retrieved data.

## Code Explanation

The script performs the following tasks:

1. Establishes a connection to Google BigQuery using the provided JSON key file.
2. Executes a SQL query on the specified database and retrieves the results.
3. Processes each record from the query result:
   - Extracts `phone` and `name` fields from the record.
   - Formats the phone number using the `format_phone_number` function.
   - Capitalizes the first name from the `name` field.
4. Calls the `verifyUserIdentity` function to validate user identity based on the formatted phone number.
5. Extracts the user identity from the response.
6. Sends a notification to the user using the `sendNotification` function, passing the namespace, template name, user identity, and formatted username.

Please ensure that you have the necessary permissions and access rights to run queries on the specified Google BigQuery database and send notifications using the provided WhatsApp functions.

## Warning

Do NOT verify many phones without send them a notification otherwise you will be banned from whatsapp!
