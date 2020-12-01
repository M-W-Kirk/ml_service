
#---START----------------------------------------

"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

# backend/server/server/urls.py file
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.endpoints.urls import urlpatterns as endpoints_urlpatterns

# URL pattern controls:
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += endpoints_urlpatterns

# add custom iParametrics styling:
admin.site.site_header = "iParametrics ML Service Admin"
admin.site.site_title = "iParametrics ML Service Admin Portal"
admin.site.index_title = "Welcome to iParametrics ML Service Admin Portal"

#---END------------------------------------------