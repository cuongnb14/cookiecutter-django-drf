import re
import requests
import urllib.parse as urlparse
from urllib.parse import urlencode
from time import time
import math
from django.conf import settings


def get_param(request, key, default_value):
    result = request.GET.get(key, None)
    if result:
        return result
    return default_value


def post_param(request, key, default_value):
    result = request.POST.get(key, None)
    if result:
        return result
    return default_value


def get_page(request):
    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1

        per_page = int(request.GET.get('per_page', 90))
        if per_page < 0:
            per_page = 90

        return page, per_page
    except Exception:
        return 1, 90


def get_limit_offset(request):
    page, limit = get_page(request)
    offset = (page - 1) * limit
    return limit, offset


def append_params_url(url, params):
    url_parts = list(urlparse.urlparse(url))
    query = dict(urlparse.parse_qsl(url_parts[4]))
    query.update(params)
    url_parts[4] = urlencode(query)
    return urlparse.urlunparse(url_parts)


def get_age(creation_tsz):
    return math.ceil((time() - creation_tsz) / 86400)


def get_prev_next_link(request):
    current_path = request.get_full_path()
    current_page = int(request.GET.get('page', 1))
    next_page = append_params_url(current_path, {'page': current_page + 1})
    if current_page - 1 < 1:
        prev_page = "#"
    else:
        prev_page = append_params_url(current_path, {'page': current_page - 1})
    return current_page, prev_page, next_page


def standardize_keyword(keyword):
    return keyword.strip().lower()


def verify_recaptcha(g_recaptcha_response):
    if not settings.IS_ENABLE_RECAPTCHA:
        return True

    querystring = {
        "secret": settings.RECAPTCHA_SECRET_KEY,
        "response": g_recaptcha_response
    }
    # TODO: remove it
    # return g_recaptcha_response
    response = requests.post(
        "https://google.com/recaptcha/api/siteverify", params=querystring)
    data = response.json()
    if not (response.status_code == 200 and data["success"]):
        return False
    return True


def standardize_email(email):
    email = email.lower().strip()

    if email.find('@gmail.com') > 0:
        first_part = email.split('@gmail.com')[0]

        first_part = re.sub(r'\.', '', first_part)
        first_part = re.sub(r'\+\w+$', '', first_part)

        email = '{}@gmail.com'.format(first_part)

    return email


def errors_to_str(errors):
    try:
        result = ""
        for key, value in errors.items():
            result += "{} - {}<br/>".format(key, value[0])
        return result
    except Exception:
        return "Invalidate input"
