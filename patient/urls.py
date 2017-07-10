from django.conf.urls import url
from . import views

app_name = 'patient'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^login/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),    

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
