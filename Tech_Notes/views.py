from django.shortcuts import render
from django.views.generic import ListView

from App_Notes.models import Notes


class NoteList(ListView):
    context_object_name = 'notes'
    model = Notes
    template_name = 'App_Notes/notelist.html'
