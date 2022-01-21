from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    # basic pages
    path('', views.index, name='index'),
    path('products', views.products, name="products"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
    path('blog/<int:id>', views.blog, name="singleblog"),
    path('contact', views.contact, name="contact"),
    path('myorders', views.myorders, name="myorders"),
    path('vendor/<int:id>', views.vendor, name="vendor"),
    path('category/<int:id>', views.category, name="category"),

    path('cart/add/<int:id>/<int:qut>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/cartdetail/',views.getCartDetail,name='getcartdetail'),
    path('cart/checkout/',views.checkout,name='checkout'),

    path('products/<str:type>', views.filterproduct, name="filterproduct"),
    path('confirm', views.confirm, name="confirm"),
    path('deleteuserorder/<int:id>', views.deleteuserorder, name="deleteuserorder"),
    path('viewuserorder/<int:id>', views.viewuserorder, name="viewuserorder"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
