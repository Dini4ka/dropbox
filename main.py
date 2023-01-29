from functions import *

test = DropboxApp(login='Pasha71265@yandex.ru', password='Denis_71265')
# test.get_authorization_code()
# test.get_access_token()
test.upload_file('tests/upload/tet.txt', '/test/check_class')

