from django.urls import path
from . import views
app_name="basicB"
urlpatterns = [
    path('templates/', views.basicC_template, name='basicC_template'),
    path('templates/basicC_form_show', views.basicC_form_show, name='basicC_form_show'),
    path('templates/basicC_form', views.basicC_form, name='basicC_form'),
    path('templates/basicC_form_show2', views.basicC_form_show2, name='basicC_form_show2'),
    path('templates/basicC_form2', views.basicC_form2, name='basicC_form2'),
    path('templates/basicC_form_show3', views.basicC_form_show3, name='basicC_form_show3'),
    path('templates/basicC_form_show4', views.basicC_form_show4, name='basicC_form_show4'),
    path('templates/basicC_form4', views.basicC_form4, name='basicC_form4'),
]