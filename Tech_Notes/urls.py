
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage, name='homepage'),
    path('account/', include('App_Login.urls')),
]
