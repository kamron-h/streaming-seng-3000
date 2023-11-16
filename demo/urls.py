"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from streaming import views as stream_views

urlpatterns = [
    path('', include(('streaming.urls', 'streaming'), namespace='streaming')),
    # path('', include('streaming.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # This includes Django auth URLs
    path('api/', stream_views.api_index, name='api_index'),
    path('members/', include(('members.urls', 'members'), namespace='members')),
    # path('member/', include('django.contrib.auth.urls')),  # Gaining Access to Auth Sys.
]

# path('', views.index, name='index'),
# path('streaming/', include('streaming.urls')),
