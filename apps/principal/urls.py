from django.conf.urls import url
from apps.principal.views import index

urlpatterns = [
    url(r'^$', index),
]
