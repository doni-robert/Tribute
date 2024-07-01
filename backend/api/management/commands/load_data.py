# your_app/management/commands/load_data.py

import csv
from django.core.management.base import BaseCommand
from api.models import County, Constituency, Ward, PollingStation

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            self.load_data(reader)

    def load_data(self, reader):
        for row in reader:
            # Only read and process the relevant columns
            county_name = row['COUNTY NAME']
            constituency_name = row['CONSTITUENCY NAME']
            ward_name = row['CAW_NAME']
            polling_station_name = row['REGISTRATION CENTRE NAME']
            
            # Create or get County
            county, created = County.objects.get_or_create(name=county_name)
            
            # Create or get Constituency
            constituency, created = Constituency.objects.get_or_create(
                name=constituency_name,
                county=county
            )
            
            # Create or get Ward
            ward, created = Ward.objects.get_or_create(
                name=ward_name,
                constituency=constituency
            )
            
            # Create or get Polling Station
            PollingStation.objects.get_or_create(
                name=polling_station_name,
                ward=ward
            )
        
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))