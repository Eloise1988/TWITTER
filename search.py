import requests
import base64
import json


# Set up your API keys and tokens
api_key="#######"
api_secret_key="####################"


# Set up the basic authentication credentials
credentials = f"{api_key}:{api_secret_key}"
credentials_encoded = base64.b64encode(credentials.encode("ascii")).decode("ascii")

# Set up the authentication headers
auth_headers = {
    "Authorization": f"Basic {credentials_encoded}",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
}

# Set up the authentication payload
auth_payload = {
    "grant_type": "client_credentials",
}

# Send the POST request to the /oauth2/token endpoint
response = requests.post(
    "https://api.twitter.com/oauth2/token",
    headers=auth_headers,
    data=auth_payload,
)

# Parse the response and get the access token
response_data = response.json()
access_token = response_data["access_token"]

# Use the access token to authenticate to the API
api_headers = {
    "Authorization": f"Bearer {access_token}",
}


query = '".eth"'
my_dictfinal=[]
for j in range(0,100):
    response = requests.get(
        "https://api.twitter.com/1.1/users/search.json",
        headers=api_headers,
        params = {
        "q": query,
        "page": j
    },
    )

    try:
        var=json.loads(response.content)

        for i in range(0,len(var)):
            if var[i]['name'][-4:].lower()==".eth":
                my_dict={}
                my_dict['name']=var[i]['name']
                my_dict['displayname']=var[i]['screen_name']
                my_dict['id']=var[i]['id']
                my_dict['followers']=var[i]['followers_count']
                my_dict['verified']=var[i]['verified']
                
                #print(my_dict)
                my_dictfinal.append(my_dict)
                #print(var[i])
    except:
        print(response.content)



print(my_dictfinal)
