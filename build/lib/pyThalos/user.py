import requests

def remotecreateuser(remote, uname, email, password):
    payload = {'email':email, 'username':uname, 'password': password }

    print("[+] Creating user "+uname+" for "+ email)

    s = requests.Session()
    r = s.post(remote, params=payload)

    #debug
    print(r.text)
