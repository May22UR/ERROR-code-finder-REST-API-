
from django.contrib import admin
from django.urls import path
from ecfapp.views import home, ErrorCodeList, ErrorCodeMeaning, error_code_meaning

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("error_codes/", ErrorCodeList.as_view(), name="ErrorCodeList"),
    path("error_codes/<int:pk>/", ErrorCodeMeaning.as_view(), name="ErrorCodeMeaning"),
    path("error_code_meaning/<int:code>/", error_code_meaning, name="error_code_meaning"),
]
