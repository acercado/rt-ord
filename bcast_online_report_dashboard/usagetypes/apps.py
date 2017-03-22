from django.apps import AppConfig


class UsagetypesConfig(AppConfig):
    name = 'bcast_online_report_dashboard.usagetypes'
    verbose_name = "Usagetypes"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass

