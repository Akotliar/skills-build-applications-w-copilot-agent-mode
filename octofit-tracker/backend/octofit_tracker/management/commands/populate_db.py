from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create workouts
        workouts = [
            Workout(name='Hero HIIT', description='High intensity for heroes', difficulty='Hard'),
            Workout(name='Power Yoga', description='Flexibility and strength', difficulty='Medium'),
        ]
        for workout in workouts:
            workout.save()

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30, calories=300, date='2025-09-19'),
            Activity(user=users[1], type='Cycling', duration=45, calories=450, date='2025-09-18'),
            Activity(user=users[2], type='Swimming', duration=60, calories=600, date='2025-09-17'),
            Activity(user=users[3], type='Boxing', duration=40, calories=400, date='2025-09-16'),
        ]
        for activity in activities:
            activity.save()

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750)
        Leaderboard.objects.create(team=dc, points=1000)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
