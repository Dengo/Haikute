from collections import deque
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
    # if method == "GET":
    try:
        if path is None:
            raise NameError
        elif path is '':
            headers = [("Content-type", "text/html")]
            with open(("templates/haikute_page.html"), 'r') as infile:
                body = infile.read()
        elif path is 'haiku':
            headers[0] = ("Content-type", "text/json")
            body = json.dump(generate_haiku())
        elif path is 'haiqueue':
            headers[0] = ("Content-type", "text/json")
            body = json.dump(get_haiku_list())
        else:
            raise NameError
        status = "200 OK"
    except NameError:
        status = "404 Not Found"
        body = "<h1>Not Found</h1>"
    except:
        status = "500 Internal Server Error"
        body = "<h1>Internal Server Error</h1>"
    headers.append(('Content-length', str(len(body))))
    start_response(status, headers)


def generate_haiku():
    return {'haiku': 'I would be a haiku!'}


def get_haiku_list():
    return {'haiqueue': 'I would be a list of haikus!'}


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, model_app)
    srv.serve_forever()
