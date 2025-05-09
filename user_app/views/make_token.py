from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime, timedelta


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=600))
    refresh.access_token.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=600))

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
