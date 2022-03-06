from django.conf.urls import url
from payment import views

urlpatterns = [
    url(r'^viewpayment/',views.payment),
    url(r'^mm/(?P<idd>\w+) (?P<idi>\w+)', views.addpayment, name='pay'),
    # url(r'^payviw/',views.pay_view.as_view())
]