from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy as __
# Create your views here.
from django.utils import translation


def index(request):
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del(request.session[translation.LANGUAGE_SESSION_KEY])
    # translation.activate('en')

    # request.session[translation.LANGUAGE_SESSION_KEY] = 'en'
    #
    # msg = _("안녕하세요 조누스님")  # _(message) --> 언어별 message를 번역하겠다.
    # return HttpResponse(msg)
    msg = _("안녕하세요 조누스님")
    msg2 = __("구어", "안녕 조누스")
    msg3 = f"{msg} {msg2}"
    return HttpResponse(msg3)


def sample(request):
    return render(request, 'sample/index.html')

from django.conf import settings
# 언어 코드를 변경하는 뷰를 만들어 보자
# 1) url named group 을 통해 language code 받기
def change_language(request, code):
    # 지원하는 언어 코드 목록을 만듦
    languages = [language[0] for language in settings.LANGUAGES]
    # 기본 언어 설정 가져오기
    default_language = settings.LANGUAGE_CODE[:2] # LANGUAGE_CODE = 'ko-KR'

    if translation.LANGUAGE_SESSION_KEY in request.session:
        del(request.session[translation.LANGUAGE_SESSION_KEY])
    # code가 지원하는 언어코드이고, 기본 언어 설정이 아닌 경우
    if code in languages and code != default_language:
        translation.activate(code)
        request.session[translation.LANGUAGE_SESSION_KEY] = code
    else:
        request.session[translation.LANGUAGE_SESSION_KEY] = default_language
        code = default_language

    return HttpResponse("Language Change to "+code)

# 2) 쿼리 스트링으로 language code 받기
def change_language2(request):
    code = request.GET.get('code')
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del(request.session[translation.LANGUAGE_SESSION_KEY])
    translation.activate(code)

    request.session[translation.LANGUAGE_SESSION_KEY] = code

    return HttpResponse("Language Change to "+code)


# Todo : LanguageForm으로 받은 데이터를 가지고
# 언어 변경하고
# 다시 원래 뷰로 돌아가는 뷰
from django.shortcuts import redirect
from .forms import LanguageForm
def change_language3(request):
    language_form = LanguageForm(request.POST)
    if language_form.is_valid():
        language = language_form.cleaned_data['code']
        languages = [language[0] for language in settings.LANGUAGES]
        if translation.LANGUAGE_SESSION_KEY in request.session:
            if language in languages:
                del (request.session[translation.LANGUAGE_SESSION_KEY])
                translation.activate(language)
                request.session[translation.LANGUAGE_SESSION_KEY] = language
    url = request.META['HTTP_REFERER']
    return redirect(url)