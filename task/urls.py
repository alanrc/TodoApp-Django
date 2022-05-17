from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),        
    path('edit/<int:id>',views.editTask, name='editTask'),
    path('delete/<int:id>',views.deleteTask, name='deleteTask'),
        
 ]
