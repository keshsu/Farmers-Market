from itertools import product
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from cart.cart import Cart
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    items = list(reversed(Product.objects.filter(popular=True)))[:4]
    ltitems = list(reversed(Product.objects.filter()))[:4]
    category = Category.objects.all()
    popular_category = list(reversed(Category.objects.filter(featured=True)))
    try:
        ad = Advertisement.objects.first()
    except:
        ad = Advertisement.objects.all()
    customer = request.user
    if customer.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    indexpageabout = IndexPageAbout.objects.first()
    maincoverimage = MainCoverImage.objects.all()
    clients = Clients.objects.all()
    tms = Testimonial.objects.filter(display=True)
    return render(request, 'mainapp/index.html', {"clients": clients,
                                                  'items': items, 'ltitems': ltitems, 'category': category,
                                                  'a': ad, 'cartItems': cartItems, 'mci': maincoverimage,
                                                  'ipa': indexpageabout, "tms": tms,
                                                  "popular_category": popular_category})


def about(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    about = About.objects.all()
    tms = Testimonial.objects.filter(display=True)
    ci = CoverImage.objects.filter(source="About").first()
    return render(request, 'mainapp/about.html', {'abouts': about, 'cartItems': cartItems,  "tms": tms, "ci": ci})


def blogs(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    blogs = Blog.objects.filter(status=True)
    ci = CoverImage.objects.filter(source="Blog").first()

    return render(request, 'mainapp/blog.html', {'blogs': blogs, 'cartItems': cartItems, "ci": ci})


def blog(request, id):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    blog = Blog.objects.get(id=id)
    ci = CoverImage.objects.filter(source="Blog").first()
    return render(request, "mainapp/single-blog.html", {"blog": blog, "cartItems": cartItems, "ci": ci})


def contact(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(
            user=request.user, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        message = render_to_string('mainapp/contact-mail.html', {
            'user': name,
            'email': email,
            'message': message,
        })
        contact = Contact.objects.create(
            name=name, email=email, subject=subject, message=message)
        print(contact)
        contact.save()
        send_mail(
            subject,
            message,
            'nabincurioua@gmail.com',
            ['nabincurioua@gmail.com'],
            fail_silently=True,
        )
    ci = CoverImage.objects.filter(source="Contact").first()
    return render(request, 'mainapp/contact.html', {"cartItems": cartItems, "ci": ci})


def myorders(request):
    if request.user.is_authenticated:
        try:
            order = Order.objects.get(
                user=request.user, complete=False)
            cartItems = order.get_cart_items
        except:
            cartItems = 0
    else:
        cartItems = 0
    all_orders = Order.objects.filter(user=request.user, complete=True)

    return render(request, 'mainapp/orders.html', {'orders': all_orders, 'cartItems': cartItems})


def products(request):
    items = list(reversed(Product.objects.all()))

    vendor = Vendor.objects.all().order_by('name')
    category = Category.objects.all().order_by('category_name')

    paginator = Paginator(items, 12)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    ci = CoverImage.objects.filter(source="Product").first()
    return render(request, 'mainapp/menu.html', {'paginator': paginator, "page_obj": page_obj, "page_num": int(page_num),
                                                 'items': page_obj.object_list, "title": "Products", "vendors": vendor, 'category': category, "ci": ci})


def vendor(request, id):
    vs = Vendor.objects.all().order_by('name')
    category = Category.objects.all().order_by('category_name')
    products = Product.objects.filter(vendor=id)

    paginator = Paginator(products, 12)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    
    v= Vendor.objects.get(id=id)
    
    ci = CoverImage.objects.filter(source="Vendor").first()
    
    return render(request, "mainapp/vendor.html", {'paginator': paginator, "page_obj": page_obj, "page_num": int(page_num),
                                                 'items': page_obj.object_list, 'vendor': v, "vendors": vs, 'category': category,})


def category(request, id):
    products = Product.objects.filter(category=id)
    category_name = Category.objects.get(id=id)
    category = Category.objects.all()

    paginator = Paginator(products, 12)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)

    
    ci = CoverImage.objects.filter(source="Category").first()

    return render(request, "mainapp/category.html", {'paginator': paginator, "page_obj": page_obj, "page_num": int(page_num),
                                                     'items': page_obj.object_list,
                                                     "title": "Categories",
                                                     'category': category,
                                                     'vendor': category_name.category_name,
                                                     'cartItems': cartItems})


def cart_add(request, id, qut):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    for x in range(qut):
        cart.add(product=product)
    try:
        return JsonResponse({'cartitem': len(request.session['cart'])})
    except:
        return redirect("cart_detail")


def getCartDetail(request):
    return JsonResponse({"allcart": request.session['cart']})


@login_required
def checkout(request):
    category = Category.objects.order_by('name')
    context = {
        "category": category, 'user': request.user}

    return render(request, "site/checkout.html", context)


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return JsonResponse({"success": "success"})


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)

    cart.add(product=product)

    return JsonResponse({"success": "success"})


def item_decrement(request, id):
    try:
        cart = Cart(request)
        product = Product.objects.get(id=id)
        cart.decrement(product=product)
    finally:
        return JsonResponse({"success": "success"})


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    total = 0
    product = Product.objects.all()
    category = Category.objects.order_by('name')
    context = {"total": total,
               "product": product,
               "category": category, 'user': request.user}
    return render(request, 'mainapp/cart.html', context)


def filterproduct(request, type):
    if type == "vendors":
        vendor = Vendor.objects.all().order_by('name')
        category = Category.objects.all().order_by('category_name')
        product = Product.objects.all()

        ci = CoverImage.objects.filter(source="Product").first()
        context = {'vendors': vendor, 'products': product,
                   "title": "Vendors", "category": category, "ci": ci}
        return render(request, "mainapp/filterproduct.html", context)
    elif type == "category":
        vendor = Vendor.objects.all().order_by('name')
        category = Category.objects.all().order_by('category_name')
        product = Product.objects.all()
        ci = CoverImage.objects.filter(source="Product").first()

        context = {'vendors': vendor,
                   'products': product, "title": "Categories", "category": category, "ci": ci}
        return render(request, "mainapp/filterproduct.html", context)

    else:
        return redirect("products")


def confirm(request):
    delivery = request.POST['delivery']
    order = Order.objects.get(
        user=request.user, complete=False)
    items = order.orderitem_set.all()

    if delivery == "inside":
        finalAmount = order.get_cart_total + 100
    else:
        finalAmount = order.get_cart_total + 200

    user = request.user
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['number']
    address = request.POST['address']
    message = render_to_string('mainapp/order-mail.html', {
        'user': user, 'name': name,
        'email': email, 'phone': phone, 'items': items, 'address': address, 'finalAmount': finalAmount
    })
    send_mail(
        "New Order Placed",
        message,
        'nabincurioua@gmail.com',
        ['nabincurioua@gmail.com'],
        fail_silently=True,
    )
    order.item_length = len(OrderItem.objects.filter(order__id=order.id))
    order.complete = True
    order.phone = phone
    order.address = address
    order.delivery_charge = finalAmount - order.get_cart_total
    order.total = order.get_cart_total
    order.save()

    return render(request, "mainapp/success.html")


def deleteuserorder(request, id):
    try:
        Order.objects.get(id=id).delete()
    finally:
        return redirect("myorders")


def viewuserorder(request, id):
    try:
        cartItem = Order.objects.get(
            user=request.user, complete=False).get_cart_items
    except:
        cartItem = 0
    orderItem = OrderItem.objects.filter(order__id=id)
    order = Order.objects.get(id=id)
    finalTotal = order.total + order.delivery_charge
    return render(request, "mainapp/viewuserorder.html", {"ois": orderItem, "or": order, "ft": finalTotal, "cartItem": cartItem})
