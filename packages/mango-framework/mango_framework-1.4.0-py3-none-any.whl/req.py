from mango import *

@route('/')
def index():
    return 'Hello, World!'

run(host='localhost', port=8080)