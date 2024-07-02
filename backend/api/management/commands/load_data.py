import csv
from django.core.management.base import BaseCommand
from api.models import County, Constituency, Ward, PollingStation

class Command(BaseCommand):
    """A Django management command to load data from CSV file into the database."""

    help = 'Load data from CSV file into the database'

    def add_arguments(self, parser):
        """Add command line arguments."""
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        """Handle command execution."""
        csv_file = kwargs['csv_file']  # Path to the CSV file from command line arguments
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)  # Read CSV file as a dictionary
            self.load_data(reader)  # Call method to load data into database

    def load_data(self, reader):
        """Load data into database from CSV reader."""
        for row in reader:
            # Extract data from CSV columns
            county_name = row['COUNTY NAME']
            constituency_name = row['CONSTITUENCY NAME']
            ward_name = row['CAW_NAME']
            polling_station_name = row['REGISTRATION CENTRE NAME']
            
            # Create or get County object
            county, created = County.objects.get_or_create(name=county_name)
            
            # Create or get Constituency object related to County
            constituency, created = Constituency.objects.get_or_create(
                name=constituency_name,
                county=county
            )
            
            # Create or get Ward object related to Constituency
            ward, created = Ward.objects.get_or_create(
                name=ward_name,
                constituency=constituency
            )
            
            # Create or get Polling Station object related to Ward
            PollingStation.objects.get_or_create(
                name=polling_station_name,
                ward=ward
            )
        
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))