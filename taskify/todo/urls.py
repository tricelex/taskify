from django.urls import path

from taskify.todo.views import CreateTaskListView, TasklistDetailView, TaskListsListView

app_name = "todos"
urlpatterns = [
    path("lists/", view=TaskListsListView.as_view(), name="task_lists"),
    path("create-list/", view=CreateTaskListView.as_view(), name="create_task_list"),
    path(
        "tasklist/<uuid:uuid>",
        view=TasklistDetailView.as_view(),
        name="task_list_detail",
    ),
]
