from .forms import LanguageForm
from django.utils import translation
def language(request):
    language_form = LanguageForm()
    if translation.LANGUAGE_SESSION_KEY in request.session:
        current_language = request.session[translation.LANGUAGE_SESSION_KEY]
        language_form = LanguageForm(initial={'code':current_language})

    return {'language_form':language_form}
