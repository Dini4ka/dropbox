from functions import *

test = DropboxApp(login='boss.karelov@gmail.com', password='Denis_71265')
test.get_authorization_code()
test.get_access_token()
test.upload_file('upload/test.txt', '/test/check_class')

