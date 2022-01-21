from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from farmermarket_app.models import *

from datetime import date

import os


@login_required(login_url="/admin/login")
def index(request):
    if request.user.is_superuser:
        vendor = len(Vendor.objects.all())
        product = len(Product.objects.all())
        order = len(Order.objects.all())
        user = len(User.objects.all())
        item = Order.objects.filter(
            complete=True, ordered_date=date.today())
        context = {'v': vendor, 'p': product, 'o': order,
                   'u': user, 'all': item, 'today': date.today()}
        return render(request, "adminApp/index.html", context)
    else:
        return redirect("userLogin")


def userLogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Form submission successful')
            return redirect("adminindex")

    return render(request, "adminApp/login.html")


def allusers(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, "adminApp/allusers.html", {"users": users})
    return redirect("/")


def addblog(request):
    if request.user.is_superuser:
        if request.method == "POST":
            title = request.POST['title']
            description = request.POST['description']
            status = request.POST['status']
            image = request.FILES['img']
            blog = Blog.objects.create(
                title=title, description=description, status=status, image=image)
            blog.save()
            return redirect("allblog")
        return render(request, "adminApp/add_blog.html")
    else:
        return redirect("/")


def allblog(request):
    if request.user.is_superuser:
        blogs = Blog.objects.all()
        return render(request, "adminApp/all_blogs.html", {'blogs': blogs})
    else:
        return redirect("/")


def allvendors(request):
    if request.user.is_superuser:
        vendors = Vendor.objects.all()
        return render(request, "adminApp/allvendors.html", {'vendors': vendors})
    else:
        return redirect("/")


def allproducts(request):
    if request.user.is_superuser:
        products = Product.objects.all()
        return render(request, "adminApp/allproducts.html", {'products': products})
    else:
        return redirect("/")


def addproduct(request):
    if request.user.is_superuser:
        if request.method == "POST":
            dish_name = request.POST['d_name']
            vendor = Vendor.objects.get(name=request.POST['vendor_name'])
            price = request.POST['price']
            category = Category.objects.filter(
                category_name=request.POST['c']).first()
            image = request.FILES['img']
            description = request.POST['description']
            popular = request.POST['tag']
            if int(popular) == 0:
                popular = False
            else:
                popular = True
            productNew = Product.objects.create(
                dish_name=dish_name, vendor=vendor, price=price, category=category, description=description, popular=popular, image=image)
            productNew.save()
        vendor = Vendor.objects.all()
        category = Category.objects.all()
        return render(request, "adminApp/addproduct.html", {'vendor': vendor, 'category': category})
    else:
        return redirect("/")


def addcategory(request):
    if request.user.is_superuser:
        if request.method == "POST":
            category_name = request.POST['category_name']
            image = request.FILES['img']
            featured = request.POST['featured']
            category = Category.objects.create(
                category_name=category_name, image=image, featured=featured)
            category.save()
        categoryAll = Category.objects.all()
        return render(request, "adminApp/addcategory.html", {"category": categoryAll})
    else:
        return redirect("/")


def addvendor(request):
    if request.user.is_superuser:
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            # image = request.POST['file']

            address = request.POST['address']
            newVendor = Vendor.objects.create(
                name=name, email=email, phone=phone, address=address)
            newVendor.save()
        category = Category.objects.all()
        return render(request, "adminApp/addvendor.html", {"category": category})
    else:
        return redirect("/")


def allorders(request):
    if request.user.is_superuser:
        all_orders = Order.objects.filter(complete=True)
        # all_orders = Order.objects.filter(complete=True)
        return render(request, "adminApp/allorders.html", {'all': all_orders})
    else:
        return redirect("/")


def todaysorders(request):
    if request.user.is_superuser:
        temp = date.today()
        today = temp.strftime("%Y-%m-%d")
        print(type(today))
        all_orders = Order.objects.filter(
            complete=True, ordered_date=today)

        return render(request, "adminApp/todaysorder.html", {'today': today, 'all': all_orders})
    else:
        return redirect("/")


def deleteBlog(request, id):
    if request.user.is_superuser:
        try:
            Blog.objects.get(id=id).delete()
        finally:
            return redirect("allblog")
    else:
        return redirect("/")


def deleteCategory(request, id):
    if request.user.is_superuser:
        try:
            Category.objects.get(id=id).delete()
        finally:
            return redirect("addcategory")
    else:
        return redirect("/")


def deleteVendor(request, id):
    if request.user.is_superuser:
        try:
            Vendor.objects.get(id=id).delete()
        finally:
            return redirect("allvendors")
    else:
        return redirect("/")


def deleteProduct(request, id):
    if request.user.is_superuser:
        try:
            Product.objects.get(id=id).delete()
        finally:
            return redirect("allproducts")
    else:
        return redirect("/")


def updateBlog(request, id):
    if request.user.is_superuser:
        if request.method == "POST":
            title = request.POST['title']
            description = request.POST['description']
            status = request.POST['status']

            Blog.objects.filter(id=id).update(
                title=title, description=description, status=status)
            b = Blog.objects.get(id=id)
            try:

                ig = request.FILES['img']
                if ig:
                    os.remove(b.image.path)
                    b.image = ig

                b.save()
            except:
                print('ph')

            return redirect("allblog")
        context = {"blog": Blog.objects.get(id=id)}
        return render(request, "adminApp/update/update_blog.html", context)
    else:
        return redirect("/")


def updateCategory(request, id):
    if request.user.is_superuser:

        if request.method == "POST":
            category_name = request.POST['category_name']
            featured = request.POST['featured']
            Category.objects.filter(id=id).update(
                category_name=category_name, featured=featured)
            cat = Category.objects.get(id=id)
            try:
                ig = request.FILES.get('img', False)
                if ig:
                    if cat.image:
                        os.remove(cat.image.path)
                    cat.image = ig
                cat.save()
            except:
                print('ph')

            return redirect("addcategory")

        context = {"category": Category.objects.get(
            id=id), "category_all": Category.objects.all()}

        return render(request, "adminApp/update/updatecategory.html", context)
    else:
        return redirect("/")


def updateVendor(request, id):
    if request.user.is_superuser:
        context = {"vendor": Vendor.objects.get(id=id)}
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            Vendor.objects.filter(id=id).update(
                name=name, email=email, phone=phone, address=address)
            v = Vendor.objects.get(id=id)
            try:

                ig = request.FILES['img']
                if ig:
                    if v.image:
                        os.remove(v.image.path)
                    v.image = ig
                v.save()
            except:
                print("ph")

            return redirect("allvendors")

        return render(request, "adminApp/update/updatevendor.html", context)
    else:
        return redirect("/")


def updateProduct(request, id):
    if request.user.is_superuser:
        if request.method == "POST":
            dish_name = request.POST['d_name']
            vendor = Vendor.objects.get(name=request.POST['vendor_name'])
            price = request.POST['price']

            category = Category.objects.get(category_name=request.POST['c'])

            description = request.POST['description']
            popular = request.POST['tag']
            if int(popular) == 0:
                popular = False
            else:
                popular = True

            Product.objects.filter(id=id).update(
                dish_name=dish_name, vendor=vendor, price=price, category=category, description=description, popular=popular, outofstock=request.POST['ots'])
            prod = Product.objects.get(id=id)

            try:
                ig = request.FILES['img']
                if ig:
                    if prod.image:
                        os.remove(prod.image.path)
                    prod.image = ig
                prod.save()

            except:
                print('ph')
            return redirect("allproducts")

        context = {'p': Product.objects.get(
            id=id), 'vendor': Vendor.objects.all(), 'category': Category.objects.all()}
        return render(request, "adminApp/update/updateproduct.html", context)
    else:
        return redirect("/")


def deleteOrder(request, id):
    if request.user.is_superuser:
        try:
            Order.objects.get(id=id).delete()
        finally:
            return redirect("allorders")
    else:
        return redirect("/")


def updateOrder(request, id):
    if request.user.is_superuser:
        orderItem = Order.objects.get(id=id)
        if request.method == "POST":
            orderItem.status = request.POST['status']
            orderItem.remarks = request.POST['remarks']
            orderItem.save()
            return redirect("allorders")
        return render(request, "adminApp/update/updateorder.html", {'o': orderItem})
    else:
        return redirect("/")


def viewOrder(request, id):
    if request.user.is_superuser:
        orderItem = OrderItem.objects.filter(order__id=id)

        order = Order.objects.get(id=id)
        finalTotal = order.total + order.delivery_charge
        return render(request, "adminApp/vieworders.html", {"ois": orderItem, "or": order, "ft": finalTotal})

    else:
        return redirect("/")


def allusers(request):
    if request.user.is_superuser:
        users = User.objects.all()
        return render(request, "adminApp/allusers.html", {'users': users})
    else:
        return redirect("/")


def updateuser(request, id):

    custom_user = User.objects.get(id=id)
    if request.user.is_superuser:
        if request.method == "POST":
            username = request.POST['uname']
            email = request.POST['email']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            User.objects.filter(id=id).update(
                username=username, first_name=first_name, last_name=last_name, email=email)
            return redirect("allusers")
        return render(request, "adminApp/update/updateuser.html", {'user': custom_user})
    else:
        return redirect("/")


def adduser(request):
    if request.user.is_superuser:
        if request.method == "POST":
            username = request.POST['uname']
            email = request.POST['email']
            first_name = request.POST['fname']
            last_name = request.POST['lname']
            User.objects.create(
                username=username, first_name=first_name, last_name=last_name, email=email, password=request.POST['pswd'])
            return redirect("allusers")
        return render(request, "adminApp/add_users.html")
    else:
        return redirect("/")


def showcontact(request):
    if request.user.is_superuser:
        contacts = Contact.objects.all()
        return render(request, "adminApp/showcontact.html", {"contacts": contacts})
    else:
        return redirect("/")


def deleteContact(request, id):
    if request.user.is_superuser:
        try:
            Contact.objects.get(id=id).delete()
            return redirect("showcontact")
        except:
            return redirect("showcontact")
    else:
        return redirect("/")


def viewContact(request, id):
    if request.user.is_superuser:
        contact = Contact.objects.get(id=id)
        return render(request, "adminApp/viewcontact.html", {"contact": contact})
    else:
        return redirect("/")


def addadvertisement(request):
    if request.user.is_superuser:
        ad = Advertisement.objects.all()
        if request.method == "POST":
            link = request.POST['d_name']
            img = request.FILES['img']
            newad = Advertisement.objects.create(adlink=link, image=img)
            newad.save()
        return render(request, "adminApp/addadvertisement.html", {"ads": ad})
    else:
        return redirect("/")


def deleteAd(request, id):
    if request.user.is_superuser:
        try:
            ads = Advertisement.objects.get(id=id)
            if ads:
                os.remove(ads.img.path)
                ads.delete()
            return redirect("addadvertisement")
        except:
            return redirect("addadvertisement")
    else:
        return redirect('/')


def addabout(request):
    if request.user.is_superuser:
        abouts = About.objects.all()
        if request.method == "POST":
            title = request.POST['title']
            description = request.POST['description']
            image = request.FILES['img']
            newad = About.objects.create(
                title=title, descripttion=description, image=image)
            newad.save()
        return render(request, "adminApp/addabout.html", {'abouts': abouts})


def deleteAbout(request, id):
    if request.user.is_superuser:
        try:
            about = About.objects.get(id=id)
            if about:
                os.remove(about.image.path)
                about.delete().delete()
        finally:
            return redirect("addabout")
    else:
        return redirect("/")


def updateAbout(request, id):
    if request.user.is_superuser:
        about = About.objects.get(id=id)
        if request.method == "POST":
            About.objects.filter(id=id).update(
                title=request.POST['title'], descripttion=request.POST['description'])
            a = About.objects.get(id=id)
            try:
                if a.image:
                    os.remove(a.image.path)
                a.image = request.FILES['img']
                a.save()
            except:
                print('ph')

            return redirect("addabout")
        return render(request, "adminApp/update/updateabout.html", {"about": about})
    else:
        return redirect("/")


def deleteuser(request, id):
    if request.user.is_superuser:
        try:
            User.objects.get(id=id).delete()
        finally:
            return redirect("allusers")
    else:
        return redirect("/")


def addbanner(request):
    if request.method == "POST":
        source = request.POST['banner_name']
        image = request.FILES['img']
        c = CoverImage.objects.create(source=source, image=image)
        c.save()
    context = {"all": CoverImage.objects.all()}
    return render(request, "adminApp/addbanner.html", context)


def deletebanner(request, id):
    c = CoverImage.objects.get(id=id)
    if c:
        if c.image:
            os.remove(c.image.path)
        c.delete()
    return redirect("addbanner")


def addclient(request):
    if request.method == "POST":
        image = request.FILES['img']
        c = Clients.objects.create(image=image)
        c.save()
    context = {"all": Clients.objects.all()}
    return render(request, "adminApp/addclient.html", context)


def deleteclient(request, id):
    c = Clients.objects.get(id=id)
    if c:
        os.remove(c.image.path)
        c.delete()
    return redirect("addclient")


def deletemainbanner(request, id):
    try:
        c = MainCoverImage.objects.get(id=id)
        if c:
            if c.image:
                os.remove(c.image.path)
            c.delete()
    except:
        return redirect("addmainbanner")
    return redirect("addmainbanner")


def addmainbanner(request):
    if request.method == "POST":
        heading = request.POST['heading']
        subheading = request.POST['subheading']
        image = request.FILES['img']
        c = MainCoverImage.objects.create(
            image=image, heading=heading, subheading=subheading)
        c.save()
    context = {"all": MainCoverImage.objects.all()}
    return render(request, "adminApp/addmainbanner.html", context)


def indexpageabout(request):
    if request.method == "POST":
        try:
            bigimage = request.FILES['img']
        except:
            bigimage = None
        try:
            smallimage = request.FILES['img2']
        except:
            smallimage = None
        heading = request.POST['heading']
        par_one = request.POST['par_one']
        par_two = request.POST['par_two']
        c = IndexPageAbout.objects.create(
            bigimage=bigimage, smallimage=smallimage, heading=heading, par_one=par_one, par_two=par_two)
        try:
            c.save()
        except:
            return redirect("/")

    context = {"all": IndexPageAbout.objects.all()}
    return render(request, "adminApp/indexpageabout.html", context)


def deleteindexpageabout(request, id):
    try:
        ipd = IndexPageAbout.objects.get(id=id)
        if ipd:
            if ipd.bigimage:
                os.remove(ipd.bigimage.path)
            if ipd.smallimage:
                os.remove(ipd.smallimage.path)
            ipd.delete()
    finally:
        return redirect("indexpageabout")


def testimonial(request):
    t = Testimonial.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        designation = request.POST['des']
        content = request.POST['description']
        image = request.FILES['img']
        popular = request.POST['tag']
        if int(popular) == 0:
            display = False
        else:
            display = True

        Testimonial.objects.create(
            name=name, designation=designation, content=content, image=image, display=display)

    return render(request, "adminApp/testimonial.html", {"t": t})


def deltestimonial(request, id):
    c = Testimonial.objects.get(id=id)
    if c:
        if c.image:
            os.remove(c.image.path)
        c.delete()
    return redirect("testimonial")


def updatetestimonial(request, id):
    t = Testimonial.objects.get(id=id)
    if request.method == "POST":
        t.name = request.POST['name']
        t.designation = request.POST['des']
        t.content = request.POST['description']
        try:
            if t.image:
                os.remove(t.image.path)
            t.image = request.FILES['img']
        except:
            print('no image')
        popular = request.POST['tag']
        if int(popular) == 0:
            t.display = False
        else:
            t.display = True
        if request.user.is_superuser:
            t.save()
        return redirect("testimonial")
    return render(request, "adminApp/update/updatetestimonial.html", {"t": t})
