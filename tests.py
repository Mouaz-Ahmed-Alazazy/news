import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import Client


def test_example():
    assert 1 + 1 == 2