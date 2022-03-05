from django.conf.urls import url
from complaint import views

urlpatterns = [
    url(r'^viwcomp/',views.ad_view_complaint),
    url(r'^repcomp/(?P<idd>\w+)',views.post_reply,name='reply1'),
    # url(r'^complainn/',views.complin_view.as_view()),
    # url(r'^android/',views.complin_view_2.as_view()),
    url(r'^complaint/',views.postcom),
    url(r'^reply/',views.vrep)

]