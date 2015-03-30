from werkzeug.serving import run_simple
import os, sys

# for running things in wsgi container; use
# wsgi.py from the rootdir

def create_app():
    
    opath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    if opath not in sys.path:
        sys.path.insert(0, opath)
    
    from adsgut_service import views
    reload(views) # don't want singletons
    return views.app

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, create_app(), use_reloader=False, use_debugger=False)