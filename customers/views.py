from django.shortcuts import render
def customers(request):
    return render(request, 'customers.html')
def customers2(request):
    return render(request, 'customers2.html')