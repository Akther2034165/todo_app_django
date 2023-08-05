from django import forms 
from todo_app.models import TodoStoreModel
class TodoStoreForm(forms.ModelForm):
    class Meta:
        model = TodoStoreModel
        fields = ['id','todo']
        labels = {
            'id' : 'Serial',
            'todo' : 'Todo',
            'todate': 'Date'
        }