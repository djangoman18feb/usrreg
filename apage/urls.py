from django.conf.urls import url
from apage import views


app_name = 'apage'

urlpatterns = [
    #/apage/
    url(r'^$', views.Index.as_view(), name='index'),
    #/apage/quote_id/
    url(r'^(?P<pk>[0-9]+)/$', views.Detail.as_view(), name='detail'),
]