geodata: A Django Package for Geographical Data
Overview
geodata is a Django package that provides models for regions, subregions, countries, states, and cities, populated with data from the countries-states-cities-database. It simplifies the integration of geographical data into Django projects, suitable for applications requiring location-based functionality.
credit of data goes to countries-states-cities-database[https://github.com/dr5hn/countries-states-cities-database.git]
Installation
Install the package using pip:
pip install geodata

Setup

Add 'geodata' to your INSTALLED_APPS in settings.py:INSTALLED_APPS = [
    # ...
    'geodata',
    # ...
]


Run migrations to create the database tables:python manage.py migrate



Loading Data
Populate the database with geographical data using the management command:
python manage.py load_geodata

This command loads regions, subregions, countries, states, and cities from JSON files included in the package.
Models
The package provides the following models:

Region: Represents a geographical region (e.g., Africa).
SubRegion: Represents a subregion within a region (e.g., Western Africa).
Country: Represents a country with details like ISO codes, capital, currency, etc.
State: Represents a state or province within a country.
City: Represents a city within a state and country, including latitude and longitude.

Each model includes fields as defined in the data source, with foreign key relationships to maintain the hierarchy.
Usage Examples
Querying Cities in a State
To retrieve all cities in a specific state:
from geodata.models import State, City

state = State.objects.get(name='California')
cities = City.objects.filter(state=state)
for city in cities:
    print(city.name)

Creating a Form with Country and City Fields
Use the models in a Django form:
from django import forms
from geodata.models import Country, City

class LocationForm(forms.Form):
    country = forms.ModelChoiceField(queryset=Country.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all())

Filtering Cities by Country
To get cities in a specific country:
from geodata.models import Country, City

country = Country.objects.get(name='United States')
cities = City.objects.filter(country=country)

Data Source and License
The data is sourced from the countries-states-cities-database, licensed under the Open Database License. Users must comply with the license terms and independently verify the data for critical applications.
Updating Data
The data is updated periodically (e.g., next update scheduled for April 8, 2025). To refresh the data:

Download the latest JSON files from the repository.
Replace the files in the geodata/data/ directory.
Re-run the load_geodata command:python manage.py load_geodata



Note: This will overwrite existing data, so back up your database if necessary.
Contributing
Contributions are welcome! Please see the CONTRIBUTING.md file in the data source repository for guidelines.
License
This package is licensed under the MIT License.
