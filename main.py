import requests

#'https://api.dropbox.com/1/token?email='+login+'&password='+pass+'&locale=en'
login = 'boss.karelov@gmail.com'
password = 'Denis_71265'


url = f'https://www.dropbox.com/oauth2/authorize'


print(requests.get(url).text)