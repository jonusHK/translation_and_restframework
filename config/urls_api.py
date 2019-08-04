from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.authtoken.views import obtain_auth_token

schema_view = get_swagger_view(title='Dstagram API Document')
urlpatterns = [
    path('doc/', schema_view),
    path('get_token/', obtain_auth_token),
    path('photo/', include('photo.api_urls'))
]