from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NameForm
from .models import Order
from carts.models import Cartitem
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string



def payments(request):
    return render(request, 'orders/payments.html')

def place_orders(request, total=0, quantity=0,):
    current_user = request.user
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = Order()
            data.your_name   = form.cleaned_data['your_name']
            data.last_name   = form.cleaned_data['last_name']
            data.email       = form.cleaned_data['email']
            data.phone       = form.cleaned_data['phone']
            data.address1    = form.cleaned_data['address1']
            data.address2    = form.cleaned_data['address2']
            data.city        = form.cleaned_data['city']
            data.state       = form.cleaned_data['state']
            data.country     = form.cleaned_data['country']
            data.order_note  = form.cleaned_data['order_note']
            data.save()

            mail_subject = "Your shopping details"
            message = render_to_string('accounts/order_email.html',{
                'your_name'     : data.your_name,
                'order_note'    : data.order_note,
                # 'grand_total'   : grand_total,
            })
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [data.email]
            send_mail( mail_subject, message, email_from, recipient_list )

            yr  = int(datetime.date.today().strftime('%Y'))
            dt  = int(datetime.date.today().strftime('%d'))
            mt  = int(datetime.date.today().strftime('%m'))
            d   =datetime.date(yr,mt,dt)
            current_date    = d.strftime("%Y%m%d")
            order_number    = current_date + str(data.id)
            data.order_number  =  order_number
            data.save()

            order = Order.objects.get(order_number=order_number)
            context = {
              'order': order,
            }
            return render(request, 'orders/payments.html', context )
            # redirect to a new URL:
            return redirect('checkout')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

        return render(request, 'store/checkout.html', {'form': form})
    return render(request, 'store/checkout.html', {'form': form})
