from django.shortcuts import render
from .models import product

# Create your views here.
#inside request.POST.get('name') method name should be same as tables in models and 
#same as used in html form
def index(request):
    if request.method == 'POST':
        #if request.POST.get('item') and requst.POST.get('price') and requst.POST.get('c_date'):
        pro = product()
        pro.item = request.POST.get('item')
        pro.price = request.POST.get('price')
        product.c_date = request.POST.get('c_date')
        pro.save()

        return render(request,'myapp/home.html')
    else:
        return render(request,'myapp/home.html')

def show(request):
    products = product.objects.all()
    #total_count = product.count()
    return render(request,'myapp/dashboard.html',{'list':products})


    
