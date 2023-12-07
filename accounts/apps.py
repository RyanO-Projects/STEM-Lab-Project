from django.apps import AppConfig


<<<<<<<< Updated upstream:STEM_Hours/StemLab/apps.py
class StemlabConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'StemLab'
========
class AccountCreationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
>>>>>>>> Stashed changes:accounts/apps.py
