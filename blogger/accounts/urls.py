from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.userLogin, name='login'),
    url(r'^logout/$', views.userLogout, name='logout'),
    url(r'^register/$', views.userRegister, name='signup'),
    url(r'^profile/$', views.userProfile, name='userprofile'),
    url(r'^editprofile/$', views.userProfileEdit, name='editprofile'),
    url(r'^deleteaccount/$', views.deleteUserAccount, name='deleteaccount'),
]
