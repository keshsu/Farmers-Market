
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('farmermarket_app.urls'), name="farmermarket"),
    path('admin/', include('adminApp.urls'), name="adminApp")

]
