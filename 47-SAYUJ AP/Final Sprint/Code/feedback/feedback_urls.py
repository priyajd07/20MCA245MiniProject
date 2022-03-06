from django.conf.urls import url
from feedback import views

urlpatterns = [
    url(r'^viewfeed/',views.feedback),
    url(r'^replyfeed/(?P<idd>\w+)',views.feedbackreplay,name='reply'),
    # url(r'^feedbck/',views.feed_view.as_view()),
    url(r'^feedbackk/',views.feedbackp),
]