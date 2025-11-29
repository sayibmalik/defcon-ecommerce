from django.contrib import admin
from django.apps import apps

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

    # Register the model with the dynamically created admin
    admin.site.register(model, ReadOnlyAdmin)
