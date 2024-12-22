import django_filters

from .models import *

class TodoListFilter(django_filters.FilterSet):
    class Meta:
        model = TodoList
        fields = '__all__'
        exclude = ['todo_item', 'remark', 'unit', 'date', 'day', 'created_at', 'updated_at']

class ContactListFilter(django_filters.FilterSet):
    class Meta:
        model = ContactList
        fields = '__all__'
        exclude = ['name', 'phone', 'remark', 'created_at', 'updated_at']


class ComplainListFilter(django_filters.FilterSet):
    class Meta:
        model = ComplainList
        fields = '__all__'
        exclude = ['complain_item', 'remark', 'unit', 'date', 'day', 'importance', 'channel', 'outcome', 'created_at', 'updated_at']


class RepairListFilter(django_filters.FilterSet):
    class Meta:
        model = RepairList
        fields = '__all__'
        exclude = ['repair_item', 'remark', 'date', 'day', 'created_at', 'updated_at']


class ReplaceListFilter(django_filters.FilterSet):
    class Meta:
        model = ReplaceList
        fields = '__all__'
        exclude = ['replace_item', 'remark', 'date', 'day', 'created_at', 'updated_at']


class TaskListFilter(django_filters.FilterSet):
    class Meta:
        model = TaskList
        fields = '__all__'
        exclude = ['task_item', 'remark', 'unit', 'date', 'day', 'created_at', 'updated_at']