from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name='Test User', email='test@example.com', team='marvel')
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, 'marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='marvel', description='Marvel Team')
        self.assertEqual(team.name, 'marvel')
        self.assertEqual(team.description, 'Marvel Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(name='Test User', email='test2@example.com', team='dc')
        activity = Activity.objects.create(user=user, activity_type='run', duration=30, date='2023-01-01')
        self.assertEqual(activity.user, user)
        self.assertEqual(activity.activity_type, 'run')
        self.assertEqual(activity.duration, 30)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = User.objects.create(name='Test User', email='test3@example.com', team='marvel')
        leaderboard = Leaderboard.objects.create(user=user, score=100, rank=1)
        self.assertEqual(leaderboard.user, user)
        self.assertEqual(leaderboard.score, 100)
        self.assertEqual(leaderboard.rank, 1)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='easy')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.difficulty, 'easy')
