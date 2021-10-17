

import requests

result=requests.get('https://w3-services1.w3-969.ibm.com/myw3/unified-profile/v2/profiles?emails=dyachama@in.ibm.com&format=custom&user_profile=notesEmail')

print(result.status_code)

print(result.text)

print(result.json)

