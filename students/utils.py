import html

from django.http import HttpResponse


def render_list(list_of_object, extra_data="", no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_object:
        string_rows.append(str(obj))

    message = "\n".join(string_rows)
    if not message:
        message = no_data_message

    response = HttpResponse(message)
    response.headers['Content-Type'] = 'text/plain'
    return response


def render_list_html(list_of_object, extra_data="",
                     no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_object:
        string_rows.append(html.escape(str(obj)))

    message = "<br>".join(string_rows)

    if not list_of_object:
        message += '<br>' + html.escape(no_data_message)

    response = HttpResponse(message)
    return response


def render_students_list_html(list_of_object, extra_data="",
                              no_data_message="<No Records>"):
    string_rows = []
    if extra_data:
        string_rows.append(extra_data)

    for obj in list_of_object:
        string_rows.append(
            html.escape(str(obj)) + ' ' +
            f'<a href="/students/update/{obj.id}">Edit</a>'
        )

    message = "<br>".join(string_rows)

    if not list_of_object:
        message += '<br>' + html.escape(no_data_message)

    response = HttpResponse('<body>%s</body>' % message)
    return response
