"""
WSGI config for techsense project.

It exposes the WSGI callable as a module-level variable named `app`.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techsense.settings")

# Vercel looks for this variable `app`
app = get_wsgi_application()

# Keep this line too (optional but safe)
application = app
