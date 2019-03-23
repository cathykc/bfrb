from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware

from api import create_api_app
from client import create_frontend_app

app = create_api_app()

if __name__ == '__main__':
    frontend_app = create_frontend_app()
    application = DispatcherMiddleware(frontend_app, {'/api': app})
    run_simple(
        'localhost',
        5100,
        application,
        use_reloader=True,
        use_debugger=True,
        threaded=True,
    )
