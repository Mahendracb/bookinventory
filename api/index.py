import os
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')

if os.environ.get('VERCEL'):
    os.environ.setdefault('DATABASE_PATH', '/tmp/db.sqlite3')

import django
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

django.setup()
call_command('migrate', run_syncdb=True, verbosity=0)

application = get_wsgi_application()
app = application
