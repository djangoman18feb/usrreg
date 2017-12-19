from django.conf.urls import url
from apage import views

app_name = 'apage'

urlpatterns = [
    #/apage/
    url(r'^$', views.index, name='index'),
    #/apage/quote_id/
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
]