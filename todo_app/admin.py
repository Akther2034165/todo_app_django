from django.contrib import admin

# Register your models here.
from todo_app.models import TodoStoreModel

# admin.site.register(TodoStoreModel)

class TodoStoreModelAdmin(admin.ModelAdmin):
    list_display = ('id','todo','todate')

admin.site.register(TodoStoreModel,TodoStoreModelAdmin)