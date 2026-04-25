from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services_list, name='services_list'),
    path('services/<int:pk>/', views.service_detail, name='service_detail'),
    path('services/add/', views.add_service, name='add_service'),
    path('services/<int:pk>/edit/', views.edit_service, name='edit_service'),
    path('services/<int:pk>/delete/', views.delete_service, name='delete_service'),
    path('products/', views.products_list, name='products_list'),
    path('portfolio/', views.portfolio_list, name='portfolio_list'),  # keep for backward compat
    path('portfolio/<int:pk>/', views.project_detail, name='project_detail'),
    path('portfolio/<int:pk>/edit/', views.edit_project, name='edit_project'),
    path('portfolio/add/', views.add_project, name='add_project'),
    path('portfolio/<int:pk>/delete/', views.delete_project, name='delete_project'),
    path('team/', views.team, name='team'),
    path('team/add/', views.add_team_member, name='add_team_member'),
    path('team/<int:pk>/edit/', views.edit_team_member, name='edit_team_member'),
    path('team/<int:pk>/delete/', views.delete_team_member, name='delete_team_member'),
    path('contact/', views.contact, name='contact'),
]
