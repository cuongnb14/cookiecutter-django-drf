import re
from django import forms

REGEX = {
    "EMAIL": "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$",
    "USERNAME": "^[a-zA-Z0-9_]+$",
    "PASSWORD": "^.{8,}$",
}


def validate_email(email):
    if not re.match(REGEX["EMAIL"], email):
        raise forms.ValidationError("Email already exists")
    return email
