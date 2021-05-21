from os import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("post/<slug:slug>/", views.project_detail, name="project_detail"),

    path('createpost/', views.createpost, name='create_post'),
    path('updatepost/<slug:slug>/', views.updatepost, name='update_post'),
    path('delete/<slug:slug>/', views.delete, name='delete')

    # path('createpost/', views.createpost, name='create_post'),
    # path('updatepost/<slug:slug>/', views.updatepost, name='update_post'),
    # path('delete/<slug:slug>/', views.delete, name='delete'),
]
