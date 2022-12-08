#python manage.py shell

from products.models import Product
qs = Product.objects.all()
qs
mouse = qs.first()
mouse.title
mouse.description
mouse.tag
mouse.tags

mouse.tag_set.all()

mouse.tag_set.filter(title__iexact='rgb')