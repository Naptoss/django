from django.shortcuts import render

def metodo(request):
    return render(request,'produto/template/produto/index.html')
