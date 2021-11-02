from django import forms

from taskify.todo.models import TaskList


class CreateListForm(forms.ModelForm):
    class Meta:
        model = TaskList
        fields = ['title']
