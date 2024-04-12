import logging
import os

import pandas as pd
from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from geo.models import City, Country


class Command(BaseCommand):
    help = ''
    log = logging.getLogger(__name__)

    def handle(self, *args, **options):
        self.main()

    def main(self):
        self.delete_old_records()
        records = self.get_cities_from_csv()
        cities_instances = self.create_cities_instances(records)
        self.update_cities_to_database(cities_instances)

    @staticmethod
    def delete_old_records():
        City.objects.all().delete()

    @staticmethod
    def get_cities_from_csv() -> list:
        file_path = os.path.join(settings.PROJECT_ROOT_DIR, 'geo/data/cities.csv')
        df_cities = pd.read_csv(file_path, sep=',')
        df_cities = df_cities[df_cities['country_code'].str.len() <= 2]
        return df_cities.to_dict('records')

    def create_cities_instances(self, records: list) -> list[City]:
        cities_objects = []
        countries_dict = self.get_countries_dict()
        for record in records:
            country_object = countries_dict.get(record['country_code'])
            city = City(
                id=record['id'],
                name=record['name'],
                longitude=record['longitude'],
                latitude=record['latitude'],
                country=country_object
            )
            cities_objects.append(city)
        return cities_objects

    @staticmethod
    def get_countries_dict():
        countries_dict = {
            country.code_iso2: country for country in Country.objects.all()
        }
        return countries_dict

    @staticmethod
    def update_cities_to_database(cities_instances: list):
        try:
            City.objects.bulk_create(
                cities_instances, ignore_conflicts=True
            )
        except IntegrityError:
            pass