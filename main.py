

import requests


result = requests.get("http://localhost:11090/management", auth=requests.auth.HTTPDigestAuth("eam", "eam"))

print(result.status_code)
print(result.text)