import requests
import json
import paramiko
import re
import os.path

api_token = open(os.path.expanduser("~/.secret/api_key"), "r")  # text file with a string
api_token = api_token.readline().strip()

req=requests.get("https://masto.bike/api/v1/instance") # change the url

jsondata=json.loads(req.text)
users=jsondata['stats']['user_count']
posts=jsondata['stats']['status_count']

instance = requests.get("https://masto.bike/api/v2/instance")  # change the url
jsoninst = json.loads(instance.text)
active = jsoninst['usage']['users']['active_month']
mastoversion = jsoninst['version']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('masto.bike', username='YOUR_USER', key_filename='/path/to/.ssh/id_rsa', timeout=3) # change url, usr and key
stdin, stdout, stderr = ssh.exec_command('df -h|grep sda3') # modify after `grep` 
df = stdout.readlines()
df = re.sub(' +', ' ', df[0].strip())
df = df.replace(" ",",")
df = df.split(",")
stdin.close()


# add date !
data = {'status' :"""

User accounts: {}
User posts   : {}
Storage usage: {}
Active users : {}
#mastodotbikestatus""".format(users,posts,df[2],active)}  # this is the body of the message

toot_url = "https://masto.bike/api/v1/statuses" # change the url here, too.
post_toot = requests.post(toot_url,
            data = data,
            headers = {'Authorization': 'Bearer {}'.format(api_token)})
print(post_toot) # this will return 200 if everything went
