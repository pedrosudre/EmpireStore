from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import render, redirect
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView
from products.models import Product
from .forms import ContactForm
from django_weasyprint import WeasyTemplateView
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML



def home_page(request):
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
    if request.user.is_authenticated:
        context["premium_content"] = "Você é um usuário Premium"
    return render(request, "home_page.html", context)
    

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": "Como podemos te ajudar?",
                    "content": "Ou envie-nos um e-mail",
                    "form": contact_form	
              }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def productGraphic(BaseLineChartView):
    def get_labels(self):
        labels = []
        queryset = Product.objects.order_by('id')
        for curso in queryset:
            labels.append(curso.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        queryset = Product.objects.order_by('id').annotate(total=Count('type'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado

class RelatorioProdutosView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        alunos = Product.objects.order_by('title').all()

        html_string = render_to_string('relatorio-alunos.html', {'alunos': alunos})

        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        html.write_pdf(target='/tmp/relatorio-alunos.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-alunos.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-alunos.pdf"'
        return response
