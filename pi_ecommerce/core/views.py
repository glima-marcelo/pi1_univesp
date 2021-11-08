from django.shortcuts import render, get_object_or_404

from core.models import Item


def index(request):
    items = Item.objects.all()
    return render(request, 'core/index.html', {'items': items})


def detail(request, slug=None):
    item = get_object_or_404(Item, slug=slug)
    return render(request, 'core/detail.html', {'item': item})
