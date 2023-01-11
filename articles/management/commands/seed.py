from django.core.management.base import BaseCommand
from articles.models import Article
import random

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    Article.objects.all().delete()


def create_article(i):
    article_names = ["Cips", "Cokolada", "Smoki",
                     "Plazma", "Jafa", "Musmule", "Gomboce", "Bajadera"]
    article_name = random.choice(article_names)
    article = Article(
        name=f"{article_name} - {i}",
        description=f"description - {i}",
        serial=random.randint(11111111, 99999999),
        weight=random.randint(10, 9999)
    )

    article.save()

    return article


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 500 addresses
    for i in range(500):
        create_article(i)
