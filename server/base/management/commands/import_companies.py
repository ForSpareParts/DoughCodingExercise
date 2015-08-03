from csv import DictReader
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from base.models import Company

class Command(BaseCommand):
    help = "Import companies from CSV files (each representing an exchange)"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--csvdir',
            dest='csv_dir',
            default=os.path.join(settings.BASE_DIR, 'companies'),
            help=('The directory containing CSV files representing exchanges. '
                + 'By default, uses the data included with the project.'))


    def handle(self, *args, **options):
        csv_dir = options['csv_dir']
        exchange_paths = []

        for path in os.listdir(csv_dir):
            full_path = os.path.join(csv_dir, path)
            if os.path.isfile(full_path) and path.endswith('.csv'):
                exchange_paths.append(path)

        for exchange_path in exchange_paths:
            exchange_name = exchange_path.rstrip('.csv')
            full_path = os.path.join(csv_dir, exchange_path)

            self.stdout.write('importing data from ' + full_path)

            with open(full_path, 'rU') as exchage_file:
                reader = DictReader(exchage_file)

                for row in reader:
                    Company.objects.get_or_create(
                        name=row['Name'],
                        symbol=row['Symbol'],
                        exchange=exchange_name)

        self.stdout.write('Successfully imported company data.')
