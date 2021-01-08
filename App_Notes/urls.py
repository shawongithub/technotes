from django.urls import path
from . import views

app_name = 'App_Notes'

urlpatterns = [
    path('create/', views.CreateNote, name='create'),
    path('detail/<int:pk>/', views.NoteDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateNote.as_view(), name='update'),
]
