import logging
import os

import pandas as pd
from django.conf import settings
from django.core.management import BaseCommand
from django.db import IntegrityError

from geo.models import Country, Continent


class Command(BaseCommand):
    help = ''
    log = logging.getLogger(__name__)

    def handle(self, *args, **options):
        self.main()

    def main(self):
        self.delete_old_records()
        records = self.get_countries_from_csv()
        countries_objects = self.create_countries_instances(records)
        self.update_countries_to_database(countries_objects)

    @staticmethod
    def delete_old_records():
        Country.objects.all().delete()

    @staticmethod
    def get_countries_from_csv() -> list:
        filename = 'geo/data/countries.csv'
        file_path = os.path.join(settings.PROJECT_ROOT_DIR, filename)
        columns = ['iso2', 'iso3', 'name', 'numeric_code', 'region']
        df_countries = pd.read_csv(file_path, sep=',', usecols=columns)
        df_countries = df_countries[df_countries['iso3'].str.len() <= 3]
        df_countries = df_countries[df_countries['iso2'].str.len() <= 2]

        return df_countries.to_dict('records')

    def create_countries_instances(self, records: list) -> list[Country]:
        continents_dict = self.get_continents_dict()
        countries_objects = []
        for record in records:
            continent = continents_dict.get(record['region'])
            if continent:
                country = Country(
                    code_iso2=record['iso2'],
                    code_iso3=record['iso3'],
                    name=record['name'],
                    num_code=record['numeric_code'],
                    continent=continent
                )
                countries_objects.append(country)
        return countries_objects

    @staticmethod
    def get_continents_dict():
        continents_dict = {
            continent.name: continent for continent in Continent.objects.all()
        }
        return continents_dict

    @staticmethod
    def update_countries_to_database(countries_objects: list):
        try:
            Country.objects.bulk_create(
                countries_objects, ignore_conflicts=True
            )
        except IntegrityError:
            pass
