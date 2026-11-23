from django.urls import path
from django.views.generic import TemplateView

from .views import StaticViews

urlpatterns = [
    path('', StaticViews, name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('products/', TemplateView.as_view(template_name='products.html'), name='products'),
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
