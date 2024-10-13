from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


def assert_response(response, *, status_code=None, results_length=None, data_include=None, data_exclude=None):
    if status_code:
        assert response.status_code == status_code
    if results_length is not None:
        assert len(response.data['results']) == results_length
    if data_include:
        assert set(data_include).issubset(response.data), f'{data_include} is not issubset of {response.data}'
    if data_exclude:
        assert set(data_exclude).intersection(response.data), f'{data_exclude} is not intersection of {response.data}'


class ExtAPIClient(APIClient):

    def call(self, method, url_name, url_params=None, **kwargs):
        path = reverse(url_name, kwargs=url_params)
        request = getattr(self, method)
        response = request(path=path, **kwargs)
        return response

    def set_credentials(self, user=None):
        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            self.credentials(HTTP_AUTHORIZATION=f'Token {access_token}')
        else:
            self.credentials(HTTP_AUTHORIZATION=None)
