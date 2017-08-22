from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^analysis$', TemplateView.as_view(template_name='info/analysis.html'), name='analysis'),
	url(r'^googleSheet$', views.post_list, name='post_list'),
]