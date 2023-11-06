# README 📘

This repository contains a Python script that interacts with Google BigQuery to fetch data from a database and sends delightful notifications via WhatsApp! 🚀

## Setup 🛠️

1. Create a `.env` file in the project directory and fill in the following details:

   ```
   CLIENT_ID=<YOUR_CLIENT_ID>
   TOKEN=<YOUR_TOKEN>
   NAMESPACE=<YOUR_NAMESPACE>
   ```
   Replace `<YOUR_TOKEN>` and `<YOUR_CLIENT_ID>` with your TakeBlip and Bot credentials. Also, set `NAMESPACE` to your desired WhatsApp namespace.

2. Update the `teamplate_name` variable in the script with your preferred template name `<YOUR_TEMPLATE_NAME>`.

3. Ensure you have a JSON key file (`bigquery_credentials.json`) provided by Google for authentication. Place this file in the project directory.

## Usage 🚀

Run the script with the following command:

```
python script_name.py
```

The script will query your BigQuery database, validate user identity, and send personalized notifications to your users.

## Code Explanation 💻

Here's a brief overview of what this script does:

1. **Connects to Google BigQuery:** Establishes a secure connection using the provided JSON key file.

2. **Executes SQL Query:** Runs a specified SQL query on the BigQuery database and fetches the results.

3. **Data Processing:**
   - Extracts `phone` and `name` fields from the query result.
   - Formats phone numbers using the `format_phone_number` function.
   - Capitalizes the first name from the `name` field for a friendly touch.

4. **User Identity Verification:** Calls the `verifyUserIdentity` function to validate user identity based on the formatted phone number.

5. **Notification Sending:** Sends a delightful notification using the `sendNotification` function. It includes the namespace, template name, user identity, and formatted username.

## Warning ⚠️

**Important:** Avoid verifying multiple phone numbers without sending notifications, as this might lead to a WhatsApp ban! Be thoughtful and considerate while using this script.

## Additional Resources 📚
For more details on sending notifications, check out the official Blip AI documentation.

Happy coding! 🎉
