from devpi.main import hookimpl

@hookimpl
def devpiclient_get_password(url, username):
    return input()
