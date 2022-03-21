import json
import re
import requests

resp = requests.get('https://www.dolarsi.com/api/api.php?type=valoresprincipales')
data= resp.json()
print (data)
