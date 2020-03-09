import pytest
from django.test import RequestFactory

from ontecx.users.models import User
from ontecx.users.views import UserRedirectView, UserUpdateView

pytestmark = pytest.mark.django_db


