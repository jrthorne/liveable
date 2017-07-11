import os
import sys
# need both the surveys site directory
myPath      = '/www/built'
if myPath not in sys.path:
    sys.path.append(myPath)
# end if

# and the django application below
myPath      = '/www/built/besite'
if myPath not in sys.path:
    sys.path.append(myPath)
# end if

os.environ['DJANGO_SETTINGS_MODULE']    = 'besite.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()