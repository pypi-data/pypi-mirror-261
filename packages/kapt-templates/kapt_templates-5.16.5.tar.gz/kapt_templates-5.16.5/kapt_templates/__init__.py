# Standard Library
import os


__version__ = "5.16.5"

KAPT_TEMPLATES_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "templates/"
)

default_app_config = "kapt_templates.apps.KaptTemplatesConfig"
