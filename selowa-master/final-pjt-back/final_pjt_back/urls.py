"""final_pjt_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
   openapi.Info(
        title='My API',
        default_version='v1',
        # 주석은 선택 인자입니다.
        # description="API 서비스입니다.",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="edujunho.hphk@gmail.com"),
        # license=openapi.License(name="SSAFY License"),
   ),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('community/', include('community.urls')),
    path('movies/', include('movies.urls')),
    path('swagger/', schema_view.with_ui('swagger')),
]
