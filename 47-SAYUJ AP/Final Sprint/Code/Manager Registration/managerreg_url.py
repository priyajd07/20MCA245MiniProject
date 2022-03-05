from django.conf.urls import url
from manager_registration import views

urlpatterns = [
    url(r'^regmanagr/',views.mangr_reg),
    url(r'^editmangr/(?P<idd>\w+)',views.edit_mangr,name='edit'),
    url(r'^del_mn/(?P<idd>\w+)', views.delete, name='del_mn'),
    url(r'^managemanger/',views.manage_mangr),





]