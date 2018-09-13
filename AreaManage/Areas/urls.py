from django.conf.urls import url
from Areas import views

app_name = 'Areas'
urlpatterns = [
    url(r'^choose/province/$', views.choose_province),
    url(r'^choose/city/$', views.choose_city),
    url(r'^choose/area/$', views.choose_area),
]