from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import District, Sector, EnergyConsumption, WasteManagement, GreenSpace, PublicTransportation, \
    AirQualityStation, AirQualityReading, CitizenInitiative


def home(request):
    return render(request, 'sustainability/home.html')


# District views
class DistrictListView(ListView):
    model = District
    template_name = 'sustainability/district/district_list.html'
    context_object_name = 'districts'


class DistrictDetailView(DetailView):
    model = District
    template_name = 'sustainability/district/district_detail.html'


class DistrictCreateView(CreateView):
    model = District
    template_name = 'sustainability/district/district_form.html'
    fields = ['name', 'population', 'area_sqkm']
    success_url = reverse_lazy('district_list')


class DistrictUpdateView(UpdateView):
    model = District
    template_name = 'sustainability/district/district_form.html'
    fields = ['name', 'population', 'area_sqkm']
    success_url = reverse_lazy('district_list')


class DistrictDeleteView(DeleteView):
    model = District
    template_name = 'sustainability/district/district_confirm_delete.html'
    success_url = reverse_lazy('district_list')


# Sector views
class SectorListView(ListView):
    model = Sector
    template_name = 'sustainability/sector/sector_list.html'
    context_object_name = 'sectors'


class SectorDetailView(DetailView):
    model = Sector
    template_name = 'sustainability/sector/sector_detail.html'


class SectorCreateView(CreateView):
    model = Sector
    template_name = 'sustainability/sector/sector_form.html'
    fields = ['district', 'name']
    success_url = reverse_lazy('sector_list')


class SectorUpdateView(UpdateView):
    model = Sector
    template_name = 'sustainability/sector/sector_form.html'
    fields = ['district', 'name']
    success_url = reverse_lazy('sector_list')


class SectorDeleteView(DeleteView):
    model = Sector
    template_name = 'sustainability/sector/sector_confirm_delete.html'
    success_url = reverse_lazy('sector_list')
