from django.contrib import admin
from django.shortcuts import render
from django.urls import path


class CustomFormPageAdmin(admin.ModelAdmin):
    title = ''
    model = None
    form_class = None

    def get_urls(self):
        view_name = '{}_{}_changelist'.format(self.model._meta.app_label, self.model._meta.model_name)
        return [
            path('', self.custom_view, name=view_name),
        ]

    def process_form(self, request, form, *args, **kwargs):
        raise NotImplementedError()

    def custom_view(self, request, *args, **kwargs):
        context = {
            **admin.site.each_context(request),
            'title': self.title,
        }
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                self.process_form(request, form, *args, **kwargs)

        context["form"] = self.form_class()
        return render(request, 'admin/custom/custom_form.html', context)
