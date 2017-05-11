from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^treatment$', views.test_treatment, name='test_treatment'),
]
