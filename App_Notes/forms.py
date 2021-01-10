from django import forms
from App_Notes.models import Notes


class NoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'body')
