import requests

url = "https://docs.docker.com/desktop/setup/install/windows-install/"
get_response = requests.get(url)

print(get_response.text)