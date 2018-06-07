import os, sys 

sys.path.append('/home/c/cl184131/gradient/public_html/gradient') 
sys.path.append('/home/c/cl184131/.env/lib/python2.7/site-packages') 

os.environ['DJANGO_SETTINGS_MODULE'] = 'gradient.settings' 

import django
django.setup()
  
import django.core.handlers.wsgi 
application = django.core.handlers.wsgi.WSGIHandler()