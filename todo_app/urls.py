from django.urls import path 
from todo_app.views import home,all_todos,edit_todos,delete_todos
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',home,name='home'),
    path('all_todos/',all_todos, name='all_todos'),
    path('edit_todos/<int:id>',edit_todos, name='edit_todos'),
    path('delete_todos/<int:id>',delete_todos, name='delete_todos')
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)