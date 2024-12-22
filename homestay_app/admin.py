from django.contrib import admin
from .models import ContactList, Tag, TodoList, ComplainList, RepairList, ReplaceList, TaskList, SalesList


class ContactListAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "building", "phone")
    search_fields = ("name", "role", "building")
    list_filter = ("name", "role", "building")

class TodoListAdmin(admin.ModelAdmin):
    list_display = ("todo_item", "unit", "category", "status", "date", "day")
    search_fields = ("todo_item", "unit", "category", "status")
    list_filter = ("unit", "category", "status")

class ComplainListAdmin(admin.ModelAdmin):
    list_display = ("complain_item", "unit", "status", "reported_by")
    search_fields = ("complain_item", "unit" "status", "reported_by")
    list_filter = ("unit", "status", "reported_by")

class RepairListAdmin(admin.ModelAdmin):
    list_display = ("repair_item", "unit", "status")

class ReplaceListAdmin(admin.ModelAdmin):
    list_display = ("replace_item", "unit", "status", "day")

class TaskListAdmin(admin.ModelAdmin):
    list_display = ("task_item", "unit", "category", "status", "date", "day")
    search_fields = ("task_item", "unit", "category", "status")
    list_filter = ("unit", "category", "status")


admin.site.register(ContactList, ContactListAdmin)
admin.site.register(Tag)
admin.site.register(TodoList, TodoListAdmin)
admin.site.register(ComplainList, ComplainListAdmin)
admin.site.register(RepairList, RepairListAdmin)
admin.site.register(ReplaceList, ReplaceListAdmin)
admin.site.register(TaskList, TaskListAdmin)
admin.site.register(SalesList)
