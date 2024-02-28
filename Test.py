name = "yasmin"
age = 65
classification =""

if(age>40):
    classification = "old"
else:
    classification = "young" 



print(name + " is "+ classification) 

import json
import requests

# URL of the API endpoint
url = 'https://api.coincap.io/v2/assets'

try:
    # Sending a GET request to the API
    response = requests.get(url)

    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        # Printing the response content (JSON data in this example)
        data = response.json()

        # Saving the JSON response to a file named 'data.json'
        with open('data.json', 'w') as f:
            json.dump(data, f)
    else:
        # If the request was unsuccessful, printing the error status code
        print("Error:", response.status_code)

except Exception as e:
    # Handling any exceptions that might occur during the request
    print("An error occurred:", e)