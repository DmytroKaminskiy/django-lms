def students_list():
    return 'Students List'

def students_create():
    return 'Students Create'

def foo():
    return 'FOO'


urlpatterns = {
    '/students/list/': students_list,  # <--
    '/students/create/': students_create,
    '/students/foo/': foo,
}


def application(environ, start_response):
    path_info = environ['PATH_INFO']  # '/students/list/'
    view_func = urlpatterns.get(path_info)  # students_list  FUNCTION obj

    if view_func:
        data = view_func().encode()
        start_response(
            "200 OK",
            [
                ("Content-Type", "text/plain"),
                ("Content-Length", str(len(data)))
            ])
    else:
        data = b'Not Found'
        start_response(
            "404 Not Found",
            [
                ("Content-Type", "text/plain"),
                ("Content-Length", str(len(data)))
            ])

    return iter([data])
