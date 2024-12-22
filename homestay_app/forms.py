from django import forms
from django.forms import ModelForm
from .models import TodoList, ContactList, ComplainList, RepairList, ReplaceList, TaskList

class TodoListForm(ModelForm):
    class Meta:
        model = TodoList
        fields = '__all__'

class ContactListForm(ModelForm):
    class Meta:
        model = ContactList
        fields = '__all__'

class ComplainListForm(ModelForm):
    class Meta:
        model = ComplainList
        fields = '__all__'

class RepairListForm(ModelForm):
    class Meta:
        model = RepairList
        fields = '__all__'

class ReplaceListForm(ModelForm):
    class Meta:
        model = ReplaceList
        fields = '__all__'

class TaskListForm(ModelForm):
    class Meta:
        model = TaskList
        fields = '__all__'
