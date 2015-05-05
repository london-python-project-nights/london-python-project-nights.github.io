import os

import bottle


ROOT = os.path.dirname(os.path.abspath(__file__))
APP = bottle.Bottle()


@APP.get('/')
def root():
    return bottle.static_file('index.html', ROOT)


@APP.get('/:path#.*#')
def static(path):
    print path
    return bottle.static_file(path, ROOT)

if __name__ == "__main__":
    APP.run(reloader=True)
