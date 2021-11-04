from typing import Any, Dict

from django.views.generic import CreateView, DetailView, ListView

from taskify.todo.forms import CreateListForm
from taskify.todo.models import TaskList


class CreateTaskListView(CreateView):
    template_name = "todo/createlist.html"
    form_class = CreateListForm

    def get_form_kwargs(self) -> Dict[str, Any]:
        """Passes the request object to the form class."""
        kwargs = super(CreateTaskListView, self).get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs


class DeleteListView:
    pass


class UpdateListView:
    pass


class ListDetailView:
    pass


class TasklistDetailView(DetailView):
    model = TaskList

    def get_object(self, queryset=None):
        return TaskList.objects.get(id=self.kwargs.get("uuid"))


class TaskListsListView(ListView):
    model = TaskList
    context_object_name = "tasklists"
    template_name = "todo/tasklist_list.html"
