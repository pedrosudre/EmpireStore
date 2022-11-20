from django.shortcuts import render, redirect

def requests(request):
    context = {
        "title": "Página de pedidos",
        "content": "Acompanhe seus pedidos"
    }
    return render(request, "requests.html", context)