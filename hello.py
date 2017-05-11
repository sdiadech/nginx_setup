def application(environ, start_response):
    status = '200 OK'
    output = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

    headers = [('Content-Type', 'text/plain')]

    start_response(status, headers)
    return output
