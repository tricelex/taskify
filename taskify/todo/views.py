from django.views.generic import CreateView, ListView, DetailView

from taskify.todo.forms import CreateListForm
from taskify.todo.models import TaskList


class CreateTaskListView(CreateView):
    template_name = 'todo/createlist.html'
    form_class = CreateListForm


class DeleteListView():
    pass


class UpdateListView():
    pass


class ListDetailView():
    pass


class TasklistDetailView(DetailView):
    model = TaskList

    def get_object(self, queryset=None):
        return TaskList.objects.get(id=self.kwargs.get("id"))


class TaskListsListView(ListView):
    model = TaskList
    context_object_name = 'tasklists'
    template_name = 'todo/tasklist_list.html'
