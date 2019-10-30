from django.urls import path
from django.contrib import admin
from django.views.generic import TemplateView
from . import views
from .views import index , success
import loginform
urlpatterns = [
    path('form/',loginform.views.index,name='index' ),
    path('form/success',loginform.views.success,name='success')
]
