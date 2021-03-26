from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken


class UserOrAnonymousJWTAuthentication(JWTAuthentication):
    """
    Auth by JWT token or session ID for anonymous user
    """
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise InvalidToken()

        if header.decode().upper().startswith("SID"):
            request.anonymous_id = self.get_raw_token(header).decode()
            return None
        else:
            raw_token = self.get_raw_token(header)
            if raw_token is None:
                raise InvalidToken()

            validated_token = self.get_validated_token(raw_token)

            return self.get_user(validated_token), validated_token


class UserJWTAuthentication(JWTAuthentication):
    """
    Auth by JWT token or session ID for anonymous user
    """
    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            raise InvalidToken()

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise InvalidToken()

        validated_token = self.get_validated_token(raw_token)

        return self.get_user(validated_token), validated_token
