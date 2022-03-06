from django.conf.urls import url

from user import views

urlpatterns=[
    url("user_reg/",views.usrreg)
]