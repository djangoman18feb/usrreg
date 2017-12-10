from django.conf.urls import url
from apage import views


app_name = 'apage'

urlpatterns = [

    #/apage/
    url(r'^$', views.Index.as_view(), name='index'),

    # /apage/register/
    #url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /apage/logout/
    #url(r'^logout/$', views.logout, name='logout'),

    #/apage/quote_id/
    url(r'^(?P<pk>[0-9]+)/$', views.Detail.as_view(), name='detail'),

    #/apage/quote/add/
    url(r'^quote/add/$', views.QuoteCreate.as_view(), name='add_quote'),

    #/apage/quote/pk_id/
    url(r'^quote/(?P<pk>[0-9]+)/$', views.QuoteUpdate.as_view(), name='update_quote'),#for future  use (Not adding buttons)

    #/apage/quote/pk_id/
    #url(r'^quote/logout/$', views.logout_view, name='logout_view'),#for future  use (Not adding buttons)

    #/apage/quote/pk_id/delete
    #url(r'^quote/(?P<pk>[0-9]+)/delete/$', views.QuoteDelete.as_view(), name='delete_quote'),#for future  use (Not adding buttons)
]