from django.apps import AppConfig


class SignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_app'

    def ready(self):
        import signal_app.signals
