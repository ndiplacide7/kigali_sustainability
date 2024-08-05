from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('districts/', views.DistrictListView.as_view(), name='district_list'),
    path('districts/<int:pk>/', views.DistrictDetailView.as_view(), name='district_detail'),
    path('districts/create/', views.DistrictCreateView.as_view(), name='district_create'),
    path('districts/<int:pk>/update/', views.DistrictUpdateView.as_view(), name='district_update'),
    path('districts/<int:pk>/delete/', views.DistrictDeleteView.as_view(), name='district_delete'),

    path('sectors/', views.SectorListView.as_view(), name='sector_list'),
    path('sectors/<int:pk>/', views.SectorDetailView.as_view(), name='sector_detail'),
    path('sectors/create/', views.SectorCreateView.as_view(), name='sector_create'),
    path('sectors/<int:pk>/update/', views.SectorUpdateView.as_view(), name='sector_update'),
    path('sectors/<int:pk>/delete/', views.SectorDeleteView.as_view(), name='sector_delete'),

# Add similar URL patterns for other models
]
