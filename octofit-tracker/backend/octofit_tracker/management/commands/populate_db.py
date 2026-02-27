from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create Users (team is a CharField, not FK)
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='Marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='Marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='DC')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='DC')

        # Create Activities (activity_type, duration, date)
        Activity.objects.create(user=tony, activity_type='Run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, activity_type='Swim', duration=45, date=timezone.now().date())
        Activity.objects.create(user=bruce, activity_type='Bike', duration=60, date=timezone.now().date())
        Activity.objects.create(user=clark, activity_type='Yoga', duration=20, date=timezone.now().date())

        # Create Workouts (name, description, difficulty)
        Workout.objects.create(name='Avengers HIIT', description='High intensity workout for Marvel heroes', difficulty='Hard')
        Workout.objects.create(name='Justice League Strength', description='Strength training for DC heroes', difficulty='Medium')

        # Create Leaderboard (user, score, rank)
        Leaderboard.objects.create(user=tony, score=1000, rank=1)
        Leaderboard.objects.create(user=steve, score=900, rank=3)
        Leaderboard.objects.create(user=bruce, score=950, rank=4)
        Leaderboard.objects.create(user=clark, score=980, rank=2)

        # Ensure unique index on email for users (MongoDB level)
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.user.create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
