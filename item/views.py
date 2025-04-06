from django.shortcuts import render, redirect, get_object_or_404
from .models import Item, Category
from .forms import AddItemForm, EditItemForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def add_item(request):
    if request.method == "POST":
        form = AddItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            form.save()
            return redirect('item:home')
    else:
        form = AddItemForm()
    
    return render(request, 'add_item.html', {
        'form': form
    })

@login_required
def home(request):
    items = Item.objects.filter(is_Sold=False)
    term = request.GET.get('search', '')
    category_id = request.GET.get('category', 0)

    if term:
        items = items.filter(Q(name__icontains=term))
        
    if category_id and int(category_id) != 0:
        items = items.filter(Q(category_id=category_id))
        
    paginator = Paginator(items, 20)
    page_number = request.GET.get('page')
    records = paginator.get_page(page_number)

    
    return render(request, 'home.html', {
        'categories': Category.objects.all(),
        'term': term,
        'category_id': category_id,
        'records': records,
    })

@login_required
def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category).exclude(id=item.id).order_by('?')[:8]
    
    return render(request, 'detail.html', {
        'item': item,
        'related_items': related_items,
    })

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    
    if request.method == "POST":
        form = EditItemForm(request.POST or None, request.FILES or None, instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=pk)
    else:
        form = EditItemForm(instance=item)
    
    return render(request, 'edit_item.html', {
        'form': form
    })

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('item:home')