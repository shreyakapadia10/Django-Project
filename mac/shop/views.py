import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Contact, Order, OrderTracker
from math import ceil
# for paytm exempting csrf
from django.views.decorators.csrf import csrf_exempt
from PayTM import Checksum

MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

# Create your views here.

def index(request):
    """As we'll show 4 images in one carousel
    Doing int division of total_products by 4 and then adding the remaining products
    that is suppose I have 6 products
    then 6//4 = 1
    ceil(6/4) = 2
    - total_products//4 = 1
    1 + (2 - 1) = 2 slides"""
    # my_products = Product.objects.all()
    # total_products = len(my_products)
    # total_slides = total_products // 4 + (ceil(total_products / 4) - total_products // 4)

    # products = {"product": my_products, "range": range(1, total_slides, "no_of_slides": total_slides )}

    # allProducts = [[my_products, range(1, total_slides), total_slides],
    #                [my_products, range(1, total_slides), total_slides]]

    allProducts = []

    # Fetching all product categories
    prod_categories = Product.objects.values('product_category', 'id')

    # adding unique product categories in set - categories
    categories = {item['product_category'] for item in prod_categories}

    # Iterating through each category and appending to allProdcuts
    for category in categories:
        product = Product.objects.filter(product_category=category)
        total_products = len(product)
        total_slides = total_products // 4 + (ceil(total_products / 4) - total_products // 4)
        allProducts.append([product, range(1, total_slides), total_slides])

    products = {'allProducts': allProducts}

    return render(request=request, template_name="shop/index.html", context=products)


def about(request):
    return render(request=request, template_name="shop/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')

        contact = Contact(contact_name=name, contact_email=email, contact_phone=phone, contact_description=query)
        contact.save()
        success = True
        return render(request=request, template_name="shop/contact.html", context={'success': success})

    return render(request=request, template_name="shop/contact.html")


def tracker(request):
    if request.method == "POST":
        order_id = request.POST.get('orderId', '')
        email = request.POST.get('email', '')

        try:
            # If such order exists
            order = Order.objects.filter(order_id=order_id, order_email=email)
            if len(order) > 0:
                # Get the updates
                order_update = OrderTracker.objects.filter(order_id=order_id)
                updates = []

                # Appends updates and return the response in JSON form
                for item in order_update:
                    updates.append({'desc': item.track_desc, 'time': item.track_timestamp.strftime("%d %B, %Y")})
                    response = json.dumps([updates, order[0].order_items], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')

        except Exception as e:
            return HttpResponse('{}')
    return render(request=request, template_name="shop/tracker.html")


def search(request):
    return render(request=request, template_name="shop/search.html")


def viewproduct(request, vid):
    product = Product.objects.filter(id=vid)
    return render(request=request, template_name="shop/viewproduct.html", context={'product': product[0]})


def checkout(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        add = request.POST.get('add1', '') + " " + request.POST.get('add2', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pincode = request.POST.get('pincode', '')
        items = request.POST.get('jsonItems', '')
        amount = request.POST.get('amount', '')

        order = Order(order_name=name, order_email=email, order_add=add, order_phone=phone,
                      order_city=city, order_state=state, order_pincode=pincode, order_items=items, order_amount=amount)
        order.save()
        oid = order.order_id
        order_status = True

        track = OrderTracker(order_id=oid, track_desc="The order has been placed successfully!")
        track.save()
        # return render(request=request, template_name="shop/checkout.html",
        #               context={'order_status': order_status, 'id': oid})

        # Request paytm to transfer amount to your account after user pays it

        param_dict = {
            'MID': 'WorldP64425807474247',
            'ORDER_ID': str(order.order_id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/shop/handlerequest/',
        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)

        return render(request, 'shop/paytm.html', {'param_dict': param_dict})

    return render(request=request, template_name="shop/checkout.html")


@csrf_exempt
def handlerequest(request):
    # paytm will send us request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Order Successful')
        else:
            print('Order was not successful because ' + response_dict['RESPMSG'])
    return render(request, 'shop/paymentstatus.html', {'response': response_dict})
