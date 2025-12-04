from django.contrib import admin
from django.apps import apps
from django.core.exceptions import ImproperlyConfigured
import logging

logger = logging.getLogger(__name__)

# Get all models from the 'home' app
home_models = apps.get_app_config('home').get_models()

for model in home_models:
    # Dynamically create a read-only admin for each model
    class ReadOnlyAdmin(admin.ModelAdmin):
        list_display = [f.name for f in model._meta.fields]      # show all fields
        readonly_fields = [f.name for f in model._meta.fields]   # all fields read-only

        def has_add_permission(self, request):
            return False

        def has_delete_permission(self, request, obj=None):
            return False

    # Register the model with the dynamically created admin.
    # Some auto-generated models use composite primary keys which Django admin
    # cannot handle; skip those and log a warning instead of crashing.
    try:
        admin.site.register(model, ReadOnlyAdmin)
    except ImproperlyConfigured:
        logger.warning("Skipping admin registration for %s: composite primary key or unsupported model", model.__name__)
    except Exception:
        # If other registration issues occur, log them but continue registering
        logger.exception("Failed to register model %s in admin", model.__name__)
