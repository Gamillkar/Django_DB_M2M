import json

from django.core.management.base import BaseCommand

from school.models import Teacher


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):


        with open('school.json', encoding='utf-8') as json_file:
            data_file = json.load(json_file)
            for item in data_file:
                if 'subject' in item['fields']:
                    Teacher.objects.create(
                        name=item['fields']['name'],
                        subject=item['fields']['subject'],
                        )
                else:
                    Teacher.objects.create(
                        name=item['fields']['name'],
                    )