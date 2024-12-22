from django.db import models
from django.db.models import Count

class Tag(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class TodoList(models.Model):
    CATEGORY = (
        ("Not Chosen", "Not Chosen"),
        ("Todo", "Todo"),
        ("Personal Growth", "Personal Growth"),
        ("Money Matter", "Money Matter"),
        ("Health", "Health"),
        ("Opportunity", "Opportunity"),
        ("Homestay", "Homestay"),
        ("Stock Market", "Stock Market"),
        ("Ecommerce", "Ecommerce"),
        ("HouseKeeping", "HouseKeeping")
    )

    STATUS = (
        ("Not Chosen", "Not Chosen"),
        ("Today", "Today"),
        ("Tomorrow", "Tomorrow"),
        ("Pending", "Pending"),
        ("Done", "Done"),
        ("This Week", "This Week"),
        ("This Month", "This Month"),
        ("This Year", "This Year"),
        ("After Europe", "After Europe"),
    )

    todo_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True, choices=CATEGORY)
    status =  models.CharField(max_length=30, blank=True, null=True, choices=STATUS)
    date = models.CharField(max_length=30, null=True, blank=True)
    day = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.todo_item

class ContactList(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    role = models.CharField(max_length=30, null=True, blank=True)
    building = models.CharField(max_length=30, null=True, blank=True)
    phone =  models.CharField(max_length=30, blank=True, null=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

class ComplainList(models.Model):

    STATUS = (
        ("Pending", "Pending"),
        ("Done", "Done"),
    )

    URGENCY = (
        ("5-Extreme", "5-Extreme"),
        ("4-Very", "4-Very"),
        ("3-Normal", "3-Normal"),
        ("2-Less", "2-Less"),
        ("1-Not", "1-Not"),
    )

    IMPORTANCE = (
        ("5-Extreme", "5-Extreme"),
        ("4-Very", "4-Very"),
        ("3-Normal", "3-Normal"),
        ("2-Less", "2-Less"),
        ("1-Not", "1-Not"),
    )


    complain_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    status =  models.CharField(max_length=30, blank=True, null=True, choices=STATUS)
    date = models.CharField(max_length=200, null=True, blank=True)
    day = models.CharField(max_length=200, null=True, blank=True)
    reported_by = models.CharField(max_length=200, null=True, blank=True)
    urgency = models.CharField(max_length=30, blank=True, null=True, choices=URGENCY)
    importance = models.CharField(max_length=30, blank=True, null=True, choices=IMPORTANCE)
    channel = models.CharField(max_length=200, null=True, blank=True)
    outcome = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.complain_item} ---- {self.unit}"

class RepairList(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Done", "Done"),
    )
    repair_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, blank=True, null=True, choices=STATUS)
    repair_by = models.CharField(max_length=30, blank=True, null=True)
    date = models.CharField(max_length=30, null=True, blank=True)
    day = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.repair_item} ---- {self.unit}"

class ReplaceList(models.Model):
    STATUS = (
        ("Pending", "Pending"),
        ("Done", "Done"),
    )

    replace_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    status = models.CharField(max_length=30, blank=True, null=True, choices=STATUS)
    date = models.CharField(max_length=30, null=True, blank=True)
    day = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.replace_item} ---- {self.unit}"

class TaskList(models.Model):
    CATEGORY = (
        ("Not Chosen", "Not Chosen"),
        ("Todo", "Todo"),
        ("Personal Growth", "Personal Growth"),
        ("Money Matter", "Money Matter"),
        ("Health", "Health"),
        ("Opportunity", "Opportunity"),
        ("Homestay", "Homestay"),
        ("Stock Market", "Stock Market"),
        ("Ecommerce", "Ecommerce"),
        ("HouseKeeping", "HouseKeeping")
    )

    STATUS = (
        ("Not Chosen", "Not Chosen"),
        ("Today", "Today"),
        ("Tomorrow", "Tomorrow"),
        ("Pending", "Pending"),
        ("Done", "Done"),
        ("This Week", "This Week"),
        ("This Month", "This Month"),
        ("This Year", "This Year"),
        ("After Europe", "After Europe"),
    )

    task_item = models.CharField(max_length=200, null=True, blank=True)
    remark = models.CharField(max_length=200, null=True, blank=True)
    unit = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=30, null=True, blank=True, choices=CATEGORY)
    status =  models.CharField(max_length=30, blank=True, null=True, choices=STATUS)
    date = models.CharField(max_length=30, null=True, blank=True)
    day = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.task_item

from django.db import models

class SalesList(models.Model):
    date = models.DateField()
    sales_amount = models.DecimalField(max_digits=10, decimal_places=2)
    homestay_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.homestay_name} - {self.date}"