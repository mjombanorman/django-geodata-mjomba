import json
from django.core.management.base import BaseCommand
from geodata.models import Region, SubRegion, Country, State, City
import os


class Command(BaseCommand):
    help = 'Load geographical data from JSON files'

    def handle(self, *args, **options):
        # Define paths to JSON files (adjust based on your package structure)
        base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data')
        regions_file = os.path.join(base_path, 'regions.json')
        subregions_file = os.path.join(base_path, 'subregions.json')
        countries_file = os.path.join(base_path, 'countries.json')
        states_file = os.path.join(base_path, 'states.json')
        cities_file = os.path.join(base_path, 'cities.json')

        # Load regions
        with open(regions_file, encoding='utf-8') as f:
            regions_data = json.load(f)
            for region_data in regions_data:
                Region.objects.get_or_create(
                    id=region_data['id'],
                    defaults={
                        'name': region_data['name'],
                        'wikiDataId': region_data.get('wikiDataId')
                    }
                )

        # Load subregions
        with open(subregions_file, encoding='utf-8') as f:
            subregions_data = json.load(f)
            for subregion_data in subregions_data:
                region = Region.objects.get(id=subregion_data['region_id'])
                SubRegion.objects.get_or_create(
                    id=subregion_data['id'],
                    defaults={
                        'name': subregion_data['name'],
                        'region': region,
                        'wikiDataId': subregion_data.get('wikiDataId')
                    }
                )

        # Load countries
        with open(countries_file, encoding='utf-8') as f:
            countries_data = json.load(f)
            for country_data in countries_data:
                region = Region.objects.get(id=country_data['region_id'])
                subregion = SubRegion.objects.get(
                    id=country_data['subregion_id'])
                Country.objects.get_or_create(
                    id=country_data['id'],
                    defaults={
                        'name': country_data['name'],
                        'iso3': country_data['iso3'],
                        'iso2': country_data['iso2'],
                        'numeric_code': country_data['numeric_code'],
                        'phonecode': country_data['phonecode'],
                        'capital': country_data['capital'],
                        'currency': country_data['currency'],
                        'currency_name': country_data['currency_name'],
                        'currency_symbol': country_data['currency_symbol'],
                        'tld': country_data['tld'],
                        'native': country_data['native'],
                        'nationality': country_data['nationality'],
                        'timezones': json.dumps(country_data['timezones']),
                        'region': region,
                        'subregion': subregion
                    }
                )

        # Load states
        with open(states_file, encoding='utf-8') as f:
            states_data = json.load(f)
            for state_data in states_data:
                country = Country.objects.get(id=state_data['country_id'])
                State.objects.get_or_create(
                    id=state_data['id'],
                    defaults={
                        'name': state_data['name'],
                        'country': country,
                        'country_code': state_data['country_code'],
                        'country_name': state_data['country_name'],
                        'state_code': state_data.get('state_code'),
                        'type': state_data['type'],
                        'latitude': state_data['latitude'],
                        'longitude': state_data['longitude']
                    }
                )

        # Load cities
        with open(cities_file, encoding='utf-8') as f:
            cities_data = json.load(f)
            for city_data in cities_data:
                state = State.objects.get(id=city_data['state_id'])
                country = Country.objects.get(id=city_data['country_id'])
                City.objects.get_or_create(
                    id=city_data['id'],
                    defaults={
                        'name': city_data['name'],
                        'state': state,
                        'state_code': city_data.get('state_code'),
                        'state_name': city_data['state_name'],
                        'country': country,
                        'country_code': city_data['country_code'],
                        'country_name': city_data['country_name'],
                        'latitude': city_data['latitude'],
                        'longitude': city_data['longitude'],
                        'wikiDataId': city_data.get('wikiDataId')
                    }
                )

        self.stdout.write(self.style.SUCCESS(
            'Geographical data loaded successfully'))
