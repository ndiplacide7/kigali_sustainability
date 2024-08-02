from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    area_sqkm = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Sector(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.district.name})"

class EnergyConsumption(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    date = models.DateField()
    electricity_kwh = models.DecimalField(max_digits=12, decimal_places=2)
    renewable_percentage = models.DecimalField(max_digits=5, decimal_places=2)

class WasteManagement(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    date = models.DateField()
    total_waste_tons = models.DecimalField(max_digits=10, decimal_places=2)
    recycled_percentage = models.DecimalField(max_digits=5, decimal_places=2)

class GreenSpace(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    area_sqm = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=50)

class PublicTransportation(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=50)
    total_vehicles = models.IntegerField()
    electric_vehicles = models.IntegerField()

class AirQualityStation(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class AirQualityReading(models.Model):
    station = models.ForeignKey(AirQualityStation, on_delete=models.CASCADE)
    date = models.DateField()
    pm25_level = models.DecimalField(max_digits=5, decimal_places=2)
    o3_level = models.DecimalField(max_digits=5, decimal_places=2)
    no2_level = models.DecimalField(max_digits=5, decimal_places=2)

class CitizenInitiative(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    participants = models.IntegerField()
    initiative_type = models.CharField(max_length=50)
