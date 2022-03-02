from django.shortcuts import render,HttpResponse,redirect
from employee.form import EmployeeForm
from employee.models import Employee


# Create your views here.
def home(request):
    #obj=EmployeeForm()
    #return render(request,'index.html',{'form':obj})
    if request.method=='POST':

        form=EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('display')
            return render(request,'show.html')
        else:
            pass
    else:
        obj=EmployeeForm()  #for get request, empty form
        return render(request,'index.html',{'form':obj})


def display(request):
    emp_list=Employee.objects.all()
    return render(request,'show.html',{'emp_data':emp_list})

def update(request,id):
    emp_id=int(id)

    try:
        emp_selected=Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('display')

    emp_form=EmployeeForm(request.POST or None,instance=emp_selected)
    if emp_form.is_valid():
        emp_form.save()
        return redirect('display')
    return render(request,'index.html',{'form':emp_form})   


def delete(request,id):
    emp_id=int(id)
    try:
        emp_selected=Employee.objects.get(id=emp_id)
    except Employee.DoesNotExist:
        return redirect('display')
    emp_selected.delete()
    return redirect('display')