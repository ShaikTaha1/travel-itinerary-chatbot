import requests

# Replace with your Weaviate instance URL
weaviate_url = 'http://localhost:8080'

# Define your schema
schema = {
    "classes": [
        {
            "class": "Activity",
            "description": "Represents activities",
            "properties": [
                {
                    "name": "activityName",
                    "dataType": ["string"]
                },
                {
                    "name": "description",
                    "dataType": ["text"]
                },
                {
                    "name": "tags",
                    "dataType": ["string"]
                }
            ]
        }
    ]
}

# API endpoint for schema setup
endpoint = f"{weaviate_url}/v1/schema"

# Send POST request to set schema
response = requests.post(endpoint, json=schema)

if response.status_code == 200:
    print("Schema setup successful!")
else:
    print(f"Failed to setup schema: {response.status_code} - {response.json()}")
