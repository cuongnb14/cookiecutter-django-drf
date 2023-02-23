from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class MyUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):
    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name',)

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    # fieldsets = (
    #         ('User Profile', {'fields': ('name',)}),
    # ) + AuthUserAdmin.fieldsets
    list_display = ('id', 'username', 'email', 'date_joined', 'last_login')
    list_display_links = ('username',)
    search_fields = ['id', 'email']

    def get_search_results(self, request, queryset, search_term):
        try:
            search_term_as_int = int(search_term)
            queryset = self.model.objects.filter(pk=search_term_as_int)
            return queryset, False
        except ValueError:
            pass
        queryset, use_distinct = super(MyUserAdmin, self).get_search_results(request, queryset, search_term)
        return queryset, use_distinct

