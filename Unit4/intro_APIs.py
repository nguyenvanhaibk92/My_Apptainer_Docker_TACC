import requests

# make a request: typical format
# response = requests.<method>(url=some_url, data=some_message, <other options>)

# e.g. try:
response = requests.get(url='https://api.github.com/orgs/tacc')

# return the status code:
response.status_code

# return the raw content
response.content

# return a Python list or dictionary from the response message
response.json()

# response = requests.get(url='https://api.github.com/orgs/tacc/members')
# response = requests.get(url='https://api.github.com/orgs/tacc/repos')
# response.json()