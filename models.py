from django.db import models


class Region(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    wikiDataId = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "Region"
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


class SubRegion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='subregions')
    wikiDataId = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "SubRegion"
        verbose_name_plural = "SubRegions"

    def __str__(self):
        return self.name


class Country(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    iso3 = models.CharField(max_length=3)
    iso2 = models.CharField(max_length=2)
    numeric_code = models.CharField(max_length=3)
    phonecode = models.CharField(max_length=10)
    capital = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    currency_name = models.CharField(max_length=255)
    currency_symbol = models.CharField(max_length=255)
    tld = models.CharField(max_length=255)
    native = models.CharField(max_length=255)
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, related_name='countries')
    subregion = models.ForeignKey(
        SubRegion, on_delete=models.CASCADE, related_name='countries')
    nationality = models.CharField(max_length=255)
    timezones = models.TextField()

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='states')
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=255)
    state_code = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class City(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey(
        State, on_delete=models.CASCADE, related_name='cities')
    state_code = models.CharField(max_length=255, blank=True, null=True)
    state_name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name='cities')
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    wikiDataId = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
