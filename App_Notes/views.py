from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect, HttpResponse
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


class DeleteNote(LoginRequiredMixin, DeleteView):
    model = Notes
    template_name = 'App_Notes/confirm_delete.html'
    success_url = reverse_lazy('homepage')


class SearchResultsView(ListView):
    model = Notes
    template_name = 'App_Notes/searchresult.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')
        object_list = Notes.objects.filter(
            # search will be performed according to title and body
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list  # object_list will be returned to searchresult.html template


@ login_required
def Share(request, pk):
    print(request.user)
    note = Notes.objects.get(pk=pk)
    if request.user == note.author:
        note.shared = not note.shared
        note.save()
    return HttpResponseRedirect(reverse('App_Notes:public'))


@ login_required
def SharedPost(request):
    notes = Notes.objects.filter(shared=True)
    context = {'notes': notes}
    print(notes)
    return render(request, 'App_Notes/sharedpost.html', context)


@ login_required
def MyNotes(request):
    notes = Notes.objects.filter(author=request.user)
    context = {'notes': notes}

    return render(request, 'App_Notes/mynotes.html', context)
