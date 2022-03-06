from django.conf.urls import url
from booking import views

urlpatterns = [
    url(r'^book/',views.booking),
    url(r'^todaybook/',views.tdybooking),
    url(r'^del_book/(?P<idd>\w+)', views.delete, name='del_book'),
    url(r'^bapprove/(?P<idd>\w+)', views.bapprove, name='bapprove'),
    # url(r'^bookingg/',views.book_view.as_view()),
    # url(r'^bookingg2/', views.book_view_2.as_view()),
    url(r'^bookstatus/',views.bookstatuss),
    url(r'^mm/(?P<idd>\w+)', views.book, name='mm'),
]