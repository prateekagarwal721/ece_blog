from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bi)oo!(=%(-&z(_4d-!)a0+#^wdko=zp8$-i%ebtl_g(2zx)83'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

PUPUT_COMMENTS_PROVIDER = 'puput.comments.DisqusCommentsProvider'




try:
    from .local import *
except ImportError:
    pass
