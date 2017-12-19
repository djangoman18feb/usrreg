from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import login, logout, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from django.core.urlresolvers import reverse
from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logged_out.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.editProfile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    #/account/reset-password/
    url(r'^reset-password/$', password_reset, {'template_name': 'accounts/reset_password.html','email_template_name': 'accounts/reset_password_email.html','post_reset_redirect': 'accounts:password_reset_done'}, name='reset_password'),

    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'accounts/reset_password_done.html'}, name='password_reset_done'),

    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm,{'current_app': 'accounts','template_name': 'accounts/reset_password_confirm.html'}, name='password_reset_confirm'),
    # url(r'^reset-password/complete/$', password_reset_complete,  name='password_reset_complete'),

]