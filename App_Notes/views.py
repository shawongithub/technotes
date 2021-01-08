from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy


from django.db.models import Q  # this should be import for performing search

from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView
from . models import Notes

# here function based view is used as we will be able to design form in the forms.py. class based view can be used as well.

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . forms import NoteForm


@login_required
def CreateNote(request):
    form = NoteForm()
    context = {'form': form}
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'App_Notes/notecreation.html', context)


class NoteDetail(LoginRequiredMixin, DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'App_Notes/notedetail.html'


class UpdateNote(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = ('title', 'body')
    template_name = 'App_Notes/updatenote.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Notes:detail', kwargs={'pk': self.object.pk})
