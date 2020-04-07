import requests

#Make an api call and store the response
url='https://api.github.com/search/repositories?q=languages:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

#Store api response in a variable
response_dict = r.json()

#Process results
print(response_dict.keys())