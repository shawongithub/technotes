
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.NoteList.as_view(), name='homepage'),
    path('account/', include('App_Login.urls')),
    path('notes/', include('App_Notes.urls')),
]
