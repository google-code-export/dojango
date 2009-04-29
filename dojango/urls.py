import os

from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('dojango',
    (r'^test/$', 'views.test'),
    (r'^test/countries/$', 'views.test_countries'),
    (r'^test/states/$', 'views.test_states'),
    # Warning: Currently all models are exposed when this is uncommented
    #(r'^disp/(?P<app_name>.*)/(?P<model_name>.*)$','views.disp'),
)

if settings.DEBUG:
    # serving the media files for dojango / dojo (js/css/...)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.abspath(os.path.join(os.path.dirname(__file__), 'media'))}),
    )

