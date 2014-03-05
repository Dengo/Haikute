from collections import deque
from haiku import Haiku
import json


haistorage = deque(maxlen=5)


# def application(environ, start_response):
#     headers = [("Content-type", "text/html")]
#     try:
#         path = environ.get('PATH_INFO', None)
#         if path is None:
#             raise NameError
#         with open("templates/haikute_page.html", 'r') as infile:
#             body = infile.read()
#         status = "200 OK"
#     except NameError:
#         status = "404 Not Found"
#         body = "<h1>Not Found</h1>"
#     except Exception:
#         status = "500 Internal Server Error"
#         body = "<h1>Internal Server Error</h1>"
#     finally:
#         headers.append(('Content-length', str(len(body))))
#         start_response(status, headers)
#         return [body]


def model_app(environ, start_response):
    # method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO', None)
    headers = []
    try:
        if path is None:
            raise NameError
        elif path == '/api/haiku':
            headers = [("Content-type", "application/json")]
            body = json.dumps(generate_haiku())
        elif path == '/api/haiqueue':
            headers = [("Content-type", "application/json")]
            body = json.dumps(get_haiku_list())
        else:
            raise NameError
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    finally:
        headers.append(('Content-length', str(len(body))))
        start_response(status, headers)
        return [body]


def generate_haiku():
    response = str(Haiku())
    haistorage.appendleft(response)
    return {'haiku': response}


def get_haiku_list():
    return {'haiqueue': list(haistorage)}

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, model_app)
    srv.serve_forever()
