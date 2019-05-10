from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.UserCreate.as_view(), name='account-create'),
]