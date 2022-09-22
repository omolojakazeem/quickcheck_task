import pytest

from .models import News
from django.urls import reverse


@pytest.mark.django_db
def test_news_create():
    News.objects.create(type="JOB")
    assert News.objects.count() == 1


@pytest.mark.django_db
def test_home_view(client):
    """
        This test checks for index page view
    :param client:
    :return:
    """
    url = reverse('news:news_home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.fixture
def api_client():
    """
        Creating an API Client for API tests
    :return:
    """
    from rest_framework.test import APIClient
    return APIClient()


@pytest.mark.django_db
def test_authorized_request(api_client):
    """
        This test checks for successful deletion of manually create news item
        :param api_client:
    """
    manually_created = News.objects.create(type="JOB")
    delete_manual_request = reverse('news:news_detail', kwargs={"id": manually_created.pk})
    response = api_client.delete(delete_manual_request)
    assert response.status_code == 204


@pytest.mark.django_db
def test_unauthorized_request(api_client):
    """
        This test checks for forbidden operation for deleting a synced news item
        :param api_client:
    """
    sync_created = News.objects.create(type="JOB", synced=True)
    delete_sync_request = reverse('news:news_detail', kwargs={"id": sync_created.pk})
    response = api_client.delete(delete_sync_request)
    assert response.status_code == 403
