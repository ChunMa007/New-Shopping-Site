from django.shortcuts import render, get_object_or_404,redirect
from item.models import Item
from .models import Cart, CartItem

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    cart_items = CartItem.objects.filter(cart__in=cart)
    
    grouped_items = {}
    
    for cart_item in cart_items:
        seller = cart_item.item.created_by
        if seller not in grouped_items:
            grouped_items[seller] = []
        grouped_items[seller].append(cart_item)
    
    return render(request, 'cart.html', {
        'cart': cart,
        'grouped_items': grouped_items
    })

def add(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('item:detail', pk=item_pk)  