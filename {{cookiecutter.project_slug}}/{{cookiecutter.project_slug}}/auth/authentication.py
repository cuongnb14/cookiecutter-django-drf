from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from {{cookiecutter.project_slug}}.auth.exceptions import InvalidTokenError, AuthenticationError


class UserJWTOrSIDAuthentication(JWTAuthentication):
    """
    Auth by JWT token or session ID for anonymous user
    """
    def authenticate(self, request):
        try:
            header = self.get_header(request)
            if header is None:
                return None

            if header.decode().upper().startswith("SID"):
                request.anonymous_id = self.get_raw_token(header).decode()
                return None
            else:
                raw_token = self.get_raw_token(header)
                if raw_token is None:
                    return None

                validated_token = self.get_validated_token(raw_token)

                return self.get_user(validated_token), validated_token

        except InvalidToken as e:  # Convert to standard exceptions
            raise InvalidTokenError(e.detail["detail"])
        except AuthenticationFailed as e:
            raise AuthenticationError(e.detail["detail"])


class UserJWTAuthentication(JWTAuthentication):
    """
    Auth by JWT token or session ID for anonymous user
    """
    def authenticate(self, request):
        try:
            return super().authenticate(request)
        except InvalidToken as e:  # Convert to standard exceptions
            raise InvalidTokenError(e.detail["detail"])
        except AuthenticationFailed as e:
            raise AuthenticationError(e.detail["detail"])
