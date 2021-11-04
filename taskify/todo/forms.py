from django import forms

from taskify.todo.models import TaskList


class CreateListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """Grants access to the request object."""
        self.request = kwargs.pop("request")
        super(CreateListForm, self).__init__(*args, **kwargs)

    class Meta:
        model = TaskList
        fields = ["title", "description"]

    def save(self, commit: bool = True):
        instance = super().save(commit=False)
        instance.user = self.request.user
        instance.save()
        return instance
