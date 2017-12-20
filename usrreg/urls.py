"""usrreg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth import views as auth_views
from apage import views
from accounts import views
from django.shortcuts import redirect
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^apage/', include('apage.urls')),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    #url(r'^home/', include('home.urls', namespace='home')),
    # url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm,{'post_reset_redirect': 'password_reset_complete', 'template_name': 'accounts/reset_password_confirm.html'}, name='password_reset_confirm'),
    # url(r'^reset-password/complete/$', auth_views.password_reset_complete, {'template_name': 'accounts/reset_password_complete.html'}, name='password_reset_complete'),
      ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

