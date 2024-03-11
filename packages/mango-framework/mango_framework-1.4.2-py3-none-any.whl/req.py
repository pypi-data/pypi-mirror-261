from mango import *

@route('/hiya')
def hiya():
    return 'Hello World!'



run(debug_mode=True)