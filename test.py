import os

import bottle
from threading import Thread
from time import sleep


ROOT = os.path.dirname(os.path.abspath(__file__))
APP = bottle.Bottle()


def continuous_build(should_run):
    """

    :type should_run: Event
    """
    import build

    while should_run['now']:
        build.main()
        sleep(1)


@APP.get('/:path#.*#')
def static(path):
    print path, '->',
    if path == '' or os.path.isdir(path):
        path += '/index.html'
    elif os.path.isfile(path):
        pass
    elif not path.endswith('.html'):
        path += '.html'
    print path
    return bottle.static_file(path, ROOT)

if __name__ == "__main__":
    running = {'now': True}
    builder = Thread(target=continuous_build, args=(running,))
    builder.start()

    try:
        APP.run(reloader=True)
    except:
        running['now'] = False
        raise
