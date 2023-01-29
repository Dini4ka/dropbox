from functions import *
import click


@click.command()
@click.argument('login')
@click.argument('password')
@click.argument('action')
@click.argument('src_path')
@click.argument('dst_path')
def main(login, password, action, src_path, dst_path):
    if action == 'put':
        test = DropboxApp(login=login, password=password)
        test.get_authorization_code()
        test.get_access_token()
        test.upload_file(src_path=str(src_path), dst_path=str(dst_path))
    elif action == 'get':
        test = DropboxApp(login=login, password=password)
        test.get_authorization_code()
        test.get_access_token()
        test.download_file(src_path=str(src_path), dst_path=str(dst_path))


if __name__ == "__main__":
    main()
