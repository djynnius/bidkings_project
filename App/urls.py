from django.conf.urls import url
from . import views

app_name = 'App'

urlpatterns = [
    # url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^$', views.IndexViewBids.as_view(),name='index'),
    url(r'^base$', views.BaseView.as_view(),name='base'),


]