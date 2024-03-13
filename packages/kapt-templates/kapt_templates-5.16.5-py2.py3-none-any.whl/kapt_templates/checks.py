import copy
import os

from django.conf import settings
from django.core.checks import Error, Tags, Warning, register
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template


E001 = Warning(
    "Template {} does not extend any base template.",
    hint="It must extend `_base.html` and should redefine as few template blocks as possible.",
    id="kapt_templates.E001",
)

E002 = Error(
    "Template {} must not extend `base.html`.",
    hint="It must extend `_base.html` and should redefine as few template blocks as possible.",
    id="kapt_templates.E002",
)

E003 = Warning(
    "Template {} must not extend `_base.html`.",
    hint="It should extend `base.html`.",
    id="kapt_templates.E003",
)

E004 = Warning(
    "Template {} must extend `{}`.",
    id="kapt_templates.E004",
)


@register(Tags.templates)
def check_base_template_must_extend(app_configs, **kwargs):
    """
    The project `base.html` template must extend kapt-templates
    `_base.html` template.
    """
    errors = []
    filename = "base.html"
    template = get_template(filename)
    source = template.template.source
    if 'extends "_base.html"' not in source and "extends '_base.html'" not in source:
        error = copy.copy(E001)
        error.msg = error.msg.format(filename)
        errors.append(error)

    return errors


@register(Tags.templates)
def check_extends_base_template(app_configs, **kwargs):
    """
    The `base.html` templates must not extend directly the project's `base.html`.
    Instead they must extend the proper kapt-templates' `_base.html` templates
    to avoid losing informations (e.g. meta tags).
    """
    errors = []
    template_files = [
        "aldryn_newsblog/base.html",
        "base.html",
        "cms/base.html",
        "djangocms_blog/base.html",
    ]

    for filename in template_files:
        template = get_template(filename)
        source = template.template.source
        if 'extends "base.html"' in source or "extends 'base.html'" in source:
            error = copy.copy(E002)
            error.msg = error.msg.format(filename)
            errors.append(error)

    return errors


@register(Tags.templates)
def check_prohibited_base_extend(app_configs, **kwargs):
    """
    Only `base.html` templates are allowed to extend `_base.html` templates.
    Other templates have to extend `base.html` templates.
    """
    errors = []
    for template_dir in settings.TEMPLATES[0]["DIRS"]:
        for dir, dirnames, filenames in os.walk(template_dir):
            for filename in filenames:
                if filename != "base.html" and not filename.startswith("."):
                    template_file = os.path.join(dir, filename)
                    with open(template_file) as f:
                        first_line = f.readline()
                        if (
                            '"_base.html"' in first_line
                            or "'_base.html'" in first_line
                            or "/_base.html" in first_line
                        ):
                            error = copy.copy(E003)
                            error.msg = error.msg.format(
                                os.path.normpath(template_file)
                            )
                            errors.append(error)

    return errors


@register(Tags.templates)
def check_prohibited_extend(app_configs, **kwargs):
    """
    Some templates must absolutely extend the kapt-templates' template:
    - djangocms_blog/post_detail.html
    - cms/page_content.html
    - cms/page_index.html
    - cms/page_results_list.html
    """
    errors = []
    template_files = [
        ("djangocms_blog/post_detail.html", "djangocms_blog/_post_detail.html"),
        ("djangocms_blog/post_list.html", "djangocms_blog/_post_list.html"),
        ("cms/page_content.html", "cms/base.html"),
        ("cms/page_index.html", "cms/base.html"),
        ("cms/page_results_list.html", "cms/base.html"),
    ]

    for filename, required_extend in template_files:
        try:
            template = get_template(filename)
        except TemplateDoesNotExist:
            template = None

        if template is not None:
            source = template.template.source
            if (
                f'extends "{required_extend}"' not in source
                and f"extends '{required_extend}'" not in source
            ):
                error = copy.copy(E004)
                error.msg = error.msg.format(filename, required_extend)
                errors.append(error)

    return errors
