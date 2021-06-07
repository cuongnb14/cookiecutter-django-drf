"""{{cookiecutter.project_slug}} URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url="/dashboard/"), name='home'),
    path('admin/', admin.site.urls),

    path('dashboard/', include(('{{cookiecutter.project_slug}}.dashboard.urls', '{{cookiecutter.project_slug}}.dashboard'), namespace='dashboard')),

    path('v1/', include(('{{cookiecutter.project_slug}}.product.urls', '{{cookiecutter.project_slug}}.product'), namespace='product')),
    path('v1/', include(('{{cookiecutter.project_slug}}.auth.urls', '{{cookiecutter.project_slug}}.auth'), namespace='auth')),
    # APPEND_NEW_URL #
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = '{{cookiecutter.project_name}} Administration'


if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
            import debug_toolbar

            urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns