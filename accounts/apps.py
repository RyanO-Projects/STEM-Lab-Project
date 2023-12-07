from django.apps import AppConfig


class StemlabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StemLab'

class AccountCreationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
