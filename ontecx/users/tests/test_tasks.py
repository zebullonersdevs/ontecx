import pytest
from celery.result import EagerResult

from ontecx.users.tasks import get_users_count
from ontecx.users.tests.factories import UserFactory

