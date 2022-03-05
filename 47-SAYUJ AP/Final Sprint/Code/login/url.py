from django.conf.urls import url
from login import views

urlpatterns = [
    url(r'^login/',views.login),
    # url(r"^android/",views.log_view.as_view()),
    # url(r"^android2/", views.forg.as_view())

]
