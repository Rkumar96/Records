from django.shortcuts import render,redirect
from . forms import CustomerForm

# Create your views here.

def index(request):
	form = CustomerForm()

	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/customer')

	context = {'form':form}
	return render(request,'myform/index.html',context)

