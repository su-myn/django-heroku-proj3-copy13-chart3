from django.shortcuts import render, redirect
from .forms import TodoListForm, ContactListForm, ComplainListForm, RepairListForm, ReplaceListForm,TaskListForm
from .models import TodoList, ContactList, ComplainList, RepairList, ReplaceList, TaskList, Tag
from django.contrib import messages
from django.db.models import Sum, Avg
from django.db.models import F, Count, Min
from .filters import *

# Create your views here.
def index(request):
	contact_list = ContactList.objects.all()
	todo_list = TodoList.objects.all()
	complain_list = ComplainList.objects.all()
	repair_list = RepairList.objects.all()
	replace_list = ReplaceList.objects.all()

	# Get the sort parameter from the URL
	sort_by = request.GET.get('sort', '')

	# Define valid sorting fields
	valid_sort_fields_contactlist = ['name', 'role', 'building', 'phone']
	valid_sort_fields_todolist = ['todo_item', 'remark', 'unit', 'category', 'status', 'created_at']

	# Check if the sort parameter is valid
	if sort_by in valid_sort_fields_contactlist:
		# Use F() to reference model fields
		contact_list = contact_list.order_by(F(sort_by).asc(nulls_last=True))

	if sort_by in valid_sort_fields_todolist:
		# Use F() to reference model fields
		todo_list =todo_list.order_by(F(sort_by).asc(nulls_last=True))

	return render(request, 'index.html', {'contact_list': contact_list, 'current_sort': sort_by, 'todo_list': todo_list, 'complain_list': complain_list, 'repair_list': repair_list, 'replace_list': replace_list})

def contactList(request):
	contact_list = ContactList.objects.all()

	# Get the sort parameter from the URL
	sort_by = request.GET.get('sort', '')

	# Define valid sorting fields
	valid_sort_fields_contactlist = ['name', 'role', 'building', 'phone']

	# Check if the sort parameter is valid
	if sort_by in valid_sort_fields_contactlist:
		# Use F() to reference model fields
		contact_list = contact_list.order_by(F(sort_by).asc(nulls_last=True))
	return render(request, 'table_contact_list.html', {'contact_list': contact_list, 'current_sort': sort_by})

def todoList(request):
    todo_list = TodoList.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', '')

    # Define valid sorting fields
    valid_sort_fields_todolist = ['todo_item', 'remark', 'unit', 'category', 'status', 'date', 'day', 'created_at']

    if sort_by in valid_sort_fields_todolist:
        # Use F() to reference model fields
        todo_list = todo_list.order_by(F(sort_by).asc(nulls_last=True))

    myFilter = TodoListFilter(request.GET, queryset=todo_list)  # Changed todo_item to todo_list
    todo_list = myFilter.qs  # Changed todo_item to todo_list
    context = {'current_sort': sort_by, 'todo_list': todo_list, 'myFilter': myFilter}
    return render(request, 'table_todo_list.html', context)


def complainList(request):
    complain_list = ComplainList.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', '')

    # Define valid sorting fields
    valid_sort_fields_complainlist = ['complain_item', 'remark', 'unit', 'status', 'date', 'reported_by', 'urgency',
                                      'importance', 'channel', 'outcome', 'created_at']

    if sort_by in valid_sort_fields_complainlist:
        # Use F() to reference model fields
        complain_list = complain_list.order_by(F(sort_by).asc(nulls_last=True))

    myFilterComplain = ComplainListFilter(request.GET, queryset=complain_list)
    complain_list = myFilterComplain.qs
    context = {
        'current_sort': sort_by,
        'complain_list': complain_list,
        'myFilterComplain': myFilterComplain,
        'messages': messages.get_messages(request)
    }

    return render(request, 'table_complain_list.html', context)


from django.db.models import F
from django.shortcuts import render


def repairList(request):
    repair_list = RepairList.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', '')

    # Define valid sorting fields
    valid_sort_fields_repairlist = ['repair_item', 'remark', 'unit']

    if sort_by in valid_sort_fields_repairlist:
        # Use F() to reference model fields
        repair_list = repair_list.order_by(F(sort_by).asc(nulls_last=True))

    myFilter = RepairListFilter(request.GET, queryset=repair_list)
    repair_list = myFilter.qs
    context = {
        'current_sort': sort_by,
        'repair_list': repair_list,
        'myFilter': myFilter
    }

    return render(request, 'table_repair_list.html', context)


def replaceList(request):
    replace_list = ReplaceList.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', '')

    # Define valid sorting fields
    valid_sort_fields_replacelist = ['replace_item', 'remark', 'unit']

    if sort_by in valid_sort_fields_replacelist:
        # Use F() to reference model fields
        replace_list = replace_list.order_by(F(sort_by).asc(nulls_last=True))

    myFilter = ReplaceListFilter(request.GET, queryset=replace_list)
    replace_list = myFilter.qs

    context = {
        'current_sort': sort_by,
        'replace_list': replace_list,
        'myFilter': myFilter
    }

    return render(request, 'table_replace_list.html', context)


#--------------------------
#-----------------
def taskList(request):
    task_list = TaskList.objects.all()

    # Get the sort parameter from the URL
    sort_by = request.GET.get('sort', '')

    # Define valid sorting fields
    valid_sort_fields_tasklist = ['task_item', 'remark', 'unit', 'category', 'status', 'date', 'day', 'created_at']

    if sort_by in valid_sort_fields_tasklist:
        # Use F() to reference model fields
        task_list = task_list.order_by(F(sort_by).asc(nulls_last=True))

    myFilter = TaskListFilter(request.GET, queryset=task_list)
    task_list = myFilter.qs

    context = {
        'current_sort': sort_by,
        'task_list': task_list,
        'myFilter': myFilter
    }

    return render(request, 'table_task_list.html', context)
#---------------------------
#-------------------------------
#-------------------------------
def formTaskList(request):

    if request.method == "POST":
        form = TaskListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully!!")
            return redirect('/table_task_list/')
    else:
        form = TaskListForm()

    context = {'form':form}
    return render(request, "form_task_list.html", context)
#-------------------------------

def formTodoList(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully!")
            return redirect('/table_todo_list/')
    else:
        form = TodoListForm()

    context = {'form': form}
    return render(request, "form_todo_list.html", context)


def formContactList(request):
    if request.method == "POST":
        form = ContactListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully!!")
            return redirect('/table_contact_list/')
    else:
        form = ContactListForm()

    context = {'form': form}
    return render(request, "form_contact_list.html", context)


def formComplainList(request):
    if request.method == "POST":
        form = ComplainListForm(request.POST)
        if form.is_valid():

            complain_item = form.cleaned_data["complain_item"]
            remark = form.cleaned_data["remark"]
            unit = form.cleaned_data["unit"]
            status = form.cleaned_data["status"]
            date = form.cleaned_data["date"]
            day = form.cleaned_data["day"]
            reported_by = form.cleaned_data["reported_by"]
            urgency = form.cleaned_data["urgency"]
            importance = form.cleaned_data["importance"]
            channel = form.cleaned_data["channel"]
            outcome = form.cleaned_data["outcome"]
            #date_created = form.cleaned_data["date_created"]

            # Create the ContactList instance without tags
            new_item = ComplainList.objects.create(
                complain_item=complain_item,
                remark=remark,
                unit=unit,
				status=status,
				date=date,
                day=day,
                reported_by=reported_by,
                urgency=urgency,
                importance=importance,
                channel=channel,
                outcome=outcome
            )

            messages.success(request, "Form Submitted Successfully!!!")
#    return render(request, "form_complain_list.html")
            return redirect('/table_complain_list/')  # Replace 'some_success_url' with your actual URL name
    else:
        form = ComplainListForm()

    return render(request, "form_complain_list.html", {'form': form})

def formRepairList(request):
    if request.method == "POST":
        form = RepairListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully!")
            return redirect('/table_repair_list/')
    else:
        form = RepairListForm()

    context = {'form': form}
    return render(request, "form_repair_list.html", context)

def formReplaceList(request):
    if request.method == "POST":
        form = ReplaceListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form Submitted Successfully!")
            return redirect('/table_repair_list/')
        else:
            form = RepairListForm()

    context = {'form': form}
    return render(request, "form_replace_list.html", context)

#---------
#---------
def updateTaskList(request, pk):
    task_list = TaskList.objects.get(id=pk)
    form = TaskListForm(instance=task_list)

    if request.method == "POST":
        form = TaskListForm(request.POST, instance=task_list)
        if form.is_valid():
            form.save()
            return redirect('/table_task_list/')

    context = {'form':form}
    return render(request, "form_task_list.html", context)

#------------
def deleteTaskList(request, pk):
    task_list = TaskList.objects.get(id=pk)
    if request.method == "POST":
        task_list.delete()
        return redirect('/table_task_list/')

    context = {'item':task_list}
    return render(request, "delete_task_list.html", context)

#------------
def updateTodoList(request, pk):
    todo_list = TodoList.objects.get(id=pk)
    form = TodoListForm(instance=todo_list)

    if request.method == "POST":
        form = TodoListForm(request.POST, instance=todo_list)
        if form.is_valid():
            form.save()
            return redirect('/table_todo_list/')

    context = {'form':form, 'todo_item': todo_list}
    return render(request, "form_todo_list.html", context)
#------------
def deleteTodoList(request, pk):
    todo_list = TodoList.objects.get(id=pk)
    if request.method == "POST":
        todo_list.delete()
        return redirect('/table_todo_list/')

    context = {'item':todo_list}
    return render(request, "delete_todo_list.html", context)

#------------
def updateContactList(request, pk):
    contact_list = ContactList.objects.get(id=pk)
    form = ContactListForm(instance=contact_list)

    if request.method == "POST":
        form = ContactListForm(request.POST, instance=contact_list)
        if form.is_valid():
            form.save()
            return redirect('/table_contact_list/')

    context = {'form':form, 'contact_item': contact_list}
    return render(request, "form_contact_list.html", context)
#------------
def deleteContactList(request, pk):
    contact_list = ContactList.objects.get(id=pk)
    if request.method == "POST":
        contact_list.delete()
        return redirect('/table_contact_list/')

    context = {'item':contact_list}
    return render(request, "delete_contact_list.html", context)

#------------
def updateComplainList(request, pk):
    complain_list = ComplainList.objects.get(id=pk)
    form = ComplainListForm(instance=complain_list)

    if request.method == "POST":
        form = ComplainListForm(request.POST, instance=complain_list)
        if form.is_valid():
            form.save()
            return redirect('/table_complain_list/')

    context = {'form':form, 'complain_item':complain_list}
    return render(request, "form_complain_list.html", context)
#------------
def deleteComplainList(request, pk):
    complain_list = ComplainList.objects.get(id=pk)
    if request.method == "POST":
        complain_list.delete()
        return redirect('/table_complain_list/')

    context = {'item':complain_list}
    return render(request, "delete_complain_list.html", context)

#------------
def updateRepairList(request, pk):
    repair_list = RepairList.objects.get(id=pk)
    form = RepairListForm(instance=repair_list)

    if request.method == "POST":
        form = RepairListForm(request.POST, instance=repair_list)
        if form.is_valid():
            form.save()
            return redirect('/table_repair_list/')

    context = {'form':form, 'repair_list':repair_list}
    return render(request, "form_repair_list.html", context)
#------------
def deleteRepairList(request, pk):
    repair_list = RepairList.objects.get(id=pk)
    if request.method == "POST":
        repair_list.delete()
        return redirect('/table_repair_list/')

    context = {'item':repair_list}
    return render(request, "delete_repair_list.html", context)

#------------
def updateReplaceList(request, pk):
    replace_list = ReplaceList.objects.get(id=pk)
    form = ReplaceListForm(instance=replace_list)

    if request.method == "POST":
        form = ReplaceListForm(request.POST, instance=replace_list)
        if form.is_valid():
            form.save()
            return redirect('/table_replace_list/')

    context = {'form':form, 'replace_list':replace_list}
    return render(request, "form_replace_list.html", context)
#------------
def deleteReplaceList(request, pk):
    replace_list = ReplaceList.objects.get(id=pk)
    if request.method == "POST":
        replace_list.delete()
        return redirect('/table_replace_list/')

    context = {'item':replace_list}
    return render(request, "delete_replace_list.html", context)

#chart----
from .models import SalesList
from django.db.models import Sum
from django.db.models.functions import TruncMonth

def sales_chart(request):
    # Group sales by month and sum the sales amount
    sales_data = SalesList.objects.annotate(month=TruncMonth('date')) \
                          .values('month') \
                          .annotate(total_sales=Sum('sales_amount')) \
                          .order_by('month')

    # Prepare data for the chart
    labels = [item['month'].strftime("%b %Y") for item in sales_data]
    series = [float(item['total_sales']) for item in sales_data]

    context = {
        'labels': labels,
        'series': series,
    }
    return render(request, 'sales.html', context)

