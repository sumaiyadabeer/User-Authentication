from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^success/$', views.success_page, name='success_page'),
    url(r'^not_valid/$', views.not_valid, name='not_valid'),
    url(r'^img_upload/$', views.img_upload, name='img_upload'), #img upload page page
    url(r'^img_select/$', views.img_select, name='img_select'), #img upload page page
    url(r'^enter_tag/$', views.enter_tag, name='enter_tag'), #img upload page page
   
    ]
