from django import template
from django.conf import settings
from menus.utils import DefaultLanguageChanger


register = template.Library()


@register.filter(name="get_x_default_url")
def get_x_default_url(request):
    # sometimes request is juste an empty str ('')
    if type(request) != str:
        # get language list (only language code)
        languages = settings.CMS_LANGUAGES[request.site.id]
        languages_codes = [language["code"] for language in languages]

        # make sure "en" is first and "fr" is second if those languages exist in the settings
        first_languages_codes = []
        if "en" in languages_codes:
            languages_codes.remove("en")
            first_languages_codes.append("en")
        if "fr" in languages_codes:
            languages_codes.remove("fr")
            first_languages_codes.append("fr")
        languages_codes = first_languages_codes + languages_codes

        # return the first translated url that we can find (from en, fr, [and all the other languages])
        if request.current_page:
            for language_code in languages_codes:
                if request.current_page.title_set.filter(
                    publisher_is_draft=False, language=language_code
                ).exists():
                    return DefaultLanguageChanger(request)(language_code)

    return None
