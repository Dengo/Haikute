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
    headers = [{"Content-type", "text/json"}]
    method = environ.get('REQUEST_METHOD')
    path = environ.get('PATH_INFO', None)
    if method == "GET":
        if path is None:
            raise NameError
        try:
            with open(("templates/haikute_page.html"), 'r') as infile:
                body = infile.read()
            status = '200 OK'
        except:
            pass
    elif method == 'POST':
        status = '200 OK'
        if path == 'generate':
            haiku = generate_haiku()
            body = json.load(haiku)
        elif path == 'api':
            haikulist = get_haiku_list()
            body = json.load(haikulist)
        else:
            raise Exception
    headers.append(('Content-length', str(len(body))))
    start_response(status, headers)


def generate_haiku():
    pass


def get_haiku_list():
    pass


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8000, model_app)
    srv.serve_forever()
