#python manage.py shell

from tags.models import Tag
Tag.objects.all()
azul = Tag.objects.last()
azul.title
azul.slug
azul.products
azul.products.all()

from products.models import Product
qs = Product.objects.all()
qs
mouse = qs.first()
mouse.title
mouse.description
mouse.tag
mouse.tags

#mas podemos usar tag_set
#que é um gerenciador many to many
mouse.tag_set.all()

mouse.tag_set.filter(title__iexact='rgb')