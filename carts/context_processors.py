from .models import Cart, Cartitem
from .views import _cart_id


# function for count product quantity
def counter(request):
    cart_count = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = Cartitem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExixt:
            cart_count = 0

        return dict(cart_count=cart_count)
