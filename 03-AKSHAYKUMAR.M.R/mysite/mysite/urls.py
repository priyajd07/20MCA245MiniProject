from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('account.urls')),
    path("dashboard/", views.home, name = 'home'),
    path("get-sentiments/", views.getSentiments, name = 'get-sentiments'),
]
