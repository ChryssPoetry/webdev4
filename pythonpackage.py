#python package index
#pipenv => equivalent of npm managers => combines pip and virtual env (env)

import requests

response = requests.get("https://google.com")
print(response)
#   keeping track of the dependencies of our project => pipfile and pipfile.lock
#managing dependencies
