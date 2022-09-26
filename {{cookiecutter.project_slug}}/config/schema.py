from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object


class UserJWTAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = 'nftbooks.core.authentication.auth.UserJWTAuthentication'
    name = 'JWTAuth'

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(header_name='AUTHORIZATION',
                                                   token_prefix='Bearer',
                                                   bearer_format='JWT')


def custom_postprocessing_hook(result, generator, request, public):
    for path, value in result['paths'].items():
        for method, ops in value.items():
            if 'summary' not in ops:
                pieces = ops['operationId'].split('_')
                ops['summary'] = f'{pieces[-1]} {" ".join(pieces[:-1])}'
    return result
