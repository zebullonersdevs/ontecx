import pytest
from django.urls import resolve, reverse

from ontecx.users.models import User

pytestmark = pytest.mark.django_db

