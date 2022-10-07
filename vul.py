import requests;
domain='https://www.hackthissite.org'
headers = requests.get(domain).headers
if 'X-frame-options' in headers:
    pass
else:
    print (domain + "vulnerable")
