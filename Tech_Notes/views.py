from django.shortcuts import render
from django.views.generic import ListView

from django.contrib.auth.decorators import login_required

from App_Notes.models import Notes


# class NoteList(ListView):
#     context_object_name = 'notes'
#     model = Notes
#     template_name = 'App_Notes/notelist.html'


@ login_required
def MyPost(request):
    notes = Notes.objects.filter(shared=True)
    context = {'notes': notes}
    print(notes)
    return render(request, 'App_Notes/notelist.html', context)
