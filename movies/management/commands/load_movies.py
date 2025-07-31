# movies/management/commands/load_movies.py
from django.core.management.base import BaseCommand
from movies.models import Movie
from datetime import datetime

class Command(BaseCommand):
    help = 'Loads sample movie data'

    def handle(self, *args, **kwargs):
        movies = [
            {
                'name': 'The Shawshank Redemption',
                'release_date': '1994-09-23',
                'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'
            },
            {
                'name': 'The Godfather',
                'release_date': '1972-03-24',
                'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.'
            },
            {
                'name': 'The Dark Knight',
                'release_date': '2008-07-18',
                'description': 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.'
            },
            {
                'name': 'Pulp Fiction',
                'release_date': '1994-10-14',
                'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.'
            },
            {
                'name': 'Fight Club',
                'release_date': '1999-10-15',
                'description': 'An insomniac office worker and a devil-may-care soapmaker form an underground fight club that evolves into something much, much more.'
            },
            {
                'name': 'Inception',
                'release_date': '2010-07-16',
                'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.'
            },
            {
                'name': 'The Matrix',
                'release_date': '1999-03-31',
                'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'
            },
            {
                'name': 'Goodfellas',
                'release_date': '1990-09-19',
                'description': 'The story of Henry Hill and his life in the mob, covering his relationship with his wife Karen Hill and his mob partners Jimmy Conway and Tommy DeVito in the Italian-American crime syndicate.'
            },
            {
                'name': 'The Silence of the Lambs',
                'release_date': '1991-02-14',
                'description': 'A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.'
            },
            {
                'name': 'Interstellar',
                'release_date': '2014-11-07',
                'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.'
            }
        ]

        for movie_data in movies:
            Movie.objects.create(
                name=movie_data['name'],
                release_date=datetime.strptime(movie_data['release_date'], '%Y-%m-%d').date(),
                description=movie_data['description']
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded movie data'))