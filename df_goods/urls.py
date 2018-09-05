from django.conf.urls import url
from django.template.context_processors import static
from . import views
from django.conf import settings


urlpatterns=[
	url(r'^$',views.index),
	url(r'^list(\d+)_(\d+)_(\d+)/$',views.list),
	url(r'^(\d+)/$',views.detail),

	]


