from .models import Vote


def reset_vote_model():
    """
    Cron function wich delete records in Vote model at the end of the day.
    See cron settings in settings.py
    """
    Vote.objects.all().delete()
