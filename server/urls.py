"""server URL Configuration

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
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("api/v1/", include([
        path("auth/", include("rest_auth.urls")),
        path("", include("users.api.v1.urls"))
    ]))
]
if settings.DEBUG:
    # swagger
    api_info = openapi.Info(
        title="Rough Smoke API",
        default_version="v1",
        description="API documentation for Rough Smoke App",
    )

    schema_view = get_schema_view(
        api_info,
        public=True,
        permission_classes=(permissions.IsAuthenticated,),
    )

    urlpatterns += [
        path("api-docs/", schema_view.with_ui("swagger", cache_timeout=0), name="api_docs")
    ]
    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
