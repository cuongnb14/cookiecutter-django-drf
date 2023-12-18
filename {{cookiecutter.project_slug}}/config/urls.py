from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/'), name='admin'),
    path('admin/', admin.site.urls),

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