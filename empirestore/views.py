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
from django.utils.translation import gettext as _
from django.utils import translation
from django.db.models import Count
from chartjs.views.lines import BaseLineChartView



def home_page(request):
    context = {
                    "title": _("Página de início"),
                    "content": _("Bem vindo a Pagina Inicial"),
              }
    lang = translation.get_language()
    context['lang'] = lang
    translation.activate(lang)
    if request.user.is_authenticated:
        context["premium_content"] = _("Você é um usuário Premium")
        lang = translation.get_language()
        context['lang'] = lang
        translation.activate(lang)
    return render(request, "home_page.html", context)
    

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
                    "title": _("Como podemos te ajudar?"),
                    "content": _("Ou envie-nos um e-mail"),
                    "form": contact_form	
              }
    lang = translation.get_language()
    context['lang'] = lang
    translation.activate(lang)
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


class RelatorioProdutosView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        produtos = Product.objects.all()

        html_string = render_to_string('relatorio-produtos.html', {'produtos': produtos})

        html = HTML(string=html_string, base_url=request.build_absolute_uri()
        )
        html.write_pdf(target='/tmp/relatorio-produtos.pdf')
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio-produtos.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="relatorio-produtos.pdf"'
        return response

