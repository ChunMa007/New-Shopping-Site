from django.shortcuts import render, redirect
from .models import Item, Category
from .forms import AddItemForm
from django.contrib.auth.decorators import login_required

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
    categories = Category.objects.all()
    
    return render(request, 'home.html', {
        'items': items,
        'categories': categories,
    })