from django.urls import path
from rest_framework import routers

from .apis import NewsList, NewsRetrieveUpdateDelete
from .views import NewsHomeView, JobsHomeView, StoryHomeView, PollHomeView, ItemDetailView

app_name = 'news'

apipatterns = [
    path('api/', NewsList.as_view(), name='news'),
    path('api/detail/<int:id>', NewsRetrieveUpdateDelete.as_view(), name='news_detail'),
]

urlpatterns = [
    path('', NewsHomeView.as_view(), name='news_home'),
    path('jobs/', JobsHomeView.as_view(), name='news_job_home'),
    path('stories/', StoryHomeView.as_view(), name='news_story_home'),
    path('polls/', PollHomeView.as_view(), name='news_poll_home'),
    path('detail/<int:pk>', ItemDetailView.as_view(), name='news_item_detail'),
]+apipatterns
