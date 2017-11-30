from django.conf.urls import url
from apage import views

urlpatterns = [
    #/apage/
    url(r'^$', views.index, name='index'),
    #/apage/quote_id/
    url(r'^(?P<quote_id>[0-9]+)/$', views.detail, name='detail'),
]