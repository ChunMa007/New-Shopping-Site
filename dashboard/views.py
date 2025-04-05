from django.shortcuts import render
from item.models import Item, Category
from django.core.paginator import Paginator
from django.db.models import Q

def index(request):
    items = Item.objects.filter(is_Sold=False, created_by=request.user)
    term = request.GET.get('search', '')
    category_id = request.GET.get('category', 0)
    
    if term:
        items = items.filter(Q(name__icontains=term))
        
    if category_id and int(category_id) != 0:
        items = items.filter(Q(category_id=category_id))
        
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)
    
    return render(request, 'index.html', {
        'records': records,
        'category': Category.objects.all(),
        'term': term,
        'category_id': category_id,
    })