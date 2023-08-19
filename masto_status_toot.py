import requests
import json
import os.path

api_token = open(os.path.expanduser(".secret/api_key"), "r")  # text file with a string
api_token = api_token.readline().strip()

req=requests.get("https://3615.computer/api/v1/instance") # change the url
jsondata=json.loads(req.text)
users=jsondata['stats']['user_count']
posts=jsondata['stats']['status_count']
domains=jsondata['stats']['domain_count']

instance = requests.get("https://3615.computer/api/v2/instance")  # change the url
jsoninst = json.loads(instance.text)
active = jsoninst['usage']['users']['active_month']
mastoversion = jsoninst['version']

# add date !
data = {
    'visibility' : "public",
    'status' :"""

User accounts: {}
User posts   : {}
Active users : {}
Domains : {}        

#3615computerstatus""".format(users,posts,active,domains)}  # this is the body of the message

toot_url = "https://3615.computer/api/v1/statuses" # change the url here, too.
post_toot = requests.post(toot_url,
            data = data,
            headers = {'Authorization': 'Bearer {}'.format(api_token)})
print(post_toot) # this will return 200 if everything went
