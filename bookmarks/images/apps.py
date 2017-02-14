from django.apps import AppConfig


class ImagesConfig(AppConfig):
    # The name attribute defines the full Python path to the application.
    name = 'images'
    # The verbose_name attribute sets the human-readable name for this application. It's displayed in the
    # administration site.
    verbose_name = 'Image Bookmarks'

    def ready(self):
        # import signal handlers
        import images.signals
