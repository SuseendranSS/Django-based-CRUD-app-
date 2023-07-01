from django.shortcuts import render, redirect
from crudapp.models import Student
from crudapp.forms import StudentForm
# Create your views here.


def retrieve_view(request):
    data = Student.objects.all()
    return render(request, 'crudapp/index.html', {'data': data})


def addstudent_view(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'crudapp/form.html', {'form': form})


def del_view(request, id):
    data = Student.objects.get(id=id)
    data.delete()
    return redirect('index')


def update_view(request, id):
    data = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=data)
    return render(request, 'crudapp/update.html', {'form': form})
