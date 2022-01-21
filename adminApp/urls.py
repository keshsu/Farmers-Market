from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    # basic pages
    path('', views.index, name='adminindex'),
    path('login', views.userLogin, name="userLogin"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("allusers/", views.allusers, name="allusers"),
    path('addblog', views.addblog, name="addblog"),
    path('allblog', views.allblog, name="allblog"),
    path('allvendors', views.allvendors, name="allvendors"),
    path('allproducts', views.allproducts, name="allproducts"),
    path('addproduct', views.addproduct, name="addproduct"),
    path("addvendor", views.addvendor, name="addvendor"),
    path("addcategory", views.addcategory, name="addcategory"),
    path("allorders", views.allorders, name="allorders"),
    path("todaysorders", views.todaysorders, name="todaysorders"),
    path("deleteBlog/<int:id>", views.deleteBlog, name="deleteBlog"),
    path("deleteCategory/<int:id>", views.deleteCategory, name="deleteCategory"),
    path("deleteVendor/<int:id>", views.deleteVendor, name="deleteVendor"),
    path("deleteProduct/<int:id>", views.deleteProduct, name="deleteProduct"),
    path("updateBlog/<int:id>", views.updateBlog, name="updateBlog"),
    path("updateCategory/<int:id>", views.updateCategory, name="updateCategory"),
    path("updateVendor/<int:id>", views.updateVendor, name="updateVendor"),
    path("updateProduct/<int:id>", views.updateProduct, name="updateProduct"),
    path('deleteOrder/<int:id>', views.deleteOrder, name="deleteOrder"),
    path('updateOrder/<int:id>', views.updateOrder, name="updateOrder"),
    path('viewOrder/<int:id>', views.viewOrder, name="viewOrder"),
    path('allusers', views.allusers, name="allusers"),
    path("updateuser/<int:id>", views.updateuser, name="updateuser"),
    path("adduser", views.adduser, name="adduser"),
    path("showcontact", views.showcontact, name="showcontact"),
    path("deleteContact/<int:id>", views.deleteContact, name="deleteContact"),
    path("viewContact/<int:id>", views.viewContact, name="viewContact"),
    path('addadvertisement', views.addadvertisement, name="addadvertisement"),
    path('deleteAd/<int:id>', views.deleteAd, name="deleteAd"),
    path('addabout', views.addabout, name="addabout"),
    path('deleteAbout/<int:id>', views.deleteAbout, name="deleteAbout"),
    path('updateAbout/<int:id>', views.updateAbout, name="updateAbout"),
    path('deleteuser/<int:id>',views.deleteuser,name="deleteuser"),
    path("addbanner",views.addbanner,name="addbanner"),
    path("deletebanner/<int:id>",views.deletebanner,name="deletebanner"),
    path("addmainbanner",views.addmainbanner,name="addmainbanner"),
    path('deletemainbanner/<int:id>',views.deletemainbanner,name="deletemainbanner"),
    path('indexpageabout',views.indexpageabout,name="indexpageabout"),
    path('deleteindexpageabout/<int:id>',views.deleteindexpageabout,name="deleteindexpageabout"),
    path("addclient",views.addclient,name="addclient"),
    path("deleteclient/<int:id>",views.deleteclient,name="deleteclient"),
    path('testimonial',views.testimonial,name="testimonial"),
    path('deltestimonial/<int:id>',views.deltestimonial,name="deltestimonial"),
    path('updatetestimonial/<int:id>',views.updatetestimonial,name="updatetestimonial")


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
