from django.apps import AppConfig


class KaptTemplatesConfig(AppConfig):
    name = "kapt_templates"
    verbose_name = "Kapt templates"

    def ready(self):
        from .checks import check_extends_base_template  # noqa
