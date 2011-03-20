from django.conf.urls.defaults import *

urlpatterns = patterns('test_app.views',
    url('^$', 'contact')
)
