def application(environ, start_response):
    status = '200 OK'
    output = environ['QUERY_STRING'].replace('/?', '').split('&')

    headers = [('Content-type', 'text/plain')]

    start_response(status, headers)
    return output
