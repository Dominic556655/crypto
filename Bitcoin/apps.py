from django.apps import AppConfig


class BitcoinConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Bitcoin'

# inside apps.py
def ready(self):
    import Bitcoin.signals
