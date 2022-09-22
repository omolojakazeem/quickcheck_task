from django.core.paginator import Paginator
from django.db.models import QuerySet, Q
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import ListView, DetailView

from news.models import News


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


class NewsHomeView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news/index.html'
    queryset = News.objects.all()

    def get_queryset(self):
        self.get_copy = self.request.GET.copy()
        self.search = self.get_copy.get("search", None)
        self.news_type = self.get_copy.get("type", None)

        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset.filter(Q(type="JOB") | Q(type="STORY") | Q(type="POLL"))
        if isinstance(queryset, QuerySet):
            if self.search:
                queryset = queryset.filter(text__icontains=self.search)
            if self.news_type:
                if self.news_type == 'all':
                    queryset = queryset
                else:
                    queryset = queryset.filter(type=self.news_type.upper())
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):

        parameters = self.get_copy.pop('page', True) and self.get_copy.urlencode()
        context = super(NewsHomeView, self).get_context_data(object_list=None, **kwargs)
        context['parameters'] = parameters
        if self.search:
            context['search'] = self.search
        if self.news_type:
            context['story'] = context['job'] = context['poll'] = False
            context['all'] = True
            if self.news_type == 'job':
                context['job'] = True
                context['all'] = False
            elif self.news_type == 'story':
                context['story'] = True
                context['all'] = False
            elif self.news_type == 'poll':
                context['poll'] = True
                context['all'] = False
        return context


class JobsHomeView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news/jobs.html'
    queryset = News.objects.all()

    def get_queryset(self):
        get_copy = self.request.GET.copy()
        self.search = get_copy.get("search", None)

        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            if self.search:
                queryset = queryset.filter(type="JOB", text__icontains=self.search)
            else:
                queryset = queryset.filter(type="JOB")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        get_copy = self.request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context = super(JobsHomeView, self).get_context_data(object_list=None, **kwargs)
        context['parameters'] = parameters
        if self.search:
            context['search'] = self.search

        return context


class PollHomeView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news/polls.html'
    queryset = News.objects.all()

    def get_queryset(self):
        get_copy = self.request.GET.copy()
        self.search = get_copy.get("search", None)

        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            if self.search:
                queryset = queryset.filter(type="POLL", text__icontains=self.search)
            else:
                queryset = queryset.filter(type="POLL")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        get_copy = self.request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context = super(PollHomeView, self).get_context_data(object_list=None, **kwargs)
        context['parameters'] = parameters
        if self.search:
            context['search'] = self.search

        return context


class StoryHomeView(ListView):
    paginate_by = 10
    model = News
    template_name = 'news/story.html'
    queryset = News.objects.all()

    def get_queryset(self):
        get_copy = self.request.GET.copy()
        self.search = get_copy.get("search", None)
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            if self.search:
                queryset = queryset.filter(type="STORY", text__icontains=self.search)
            else:
                queryset = queryset.filter(type="STORY")
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        get_copy = self.request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()
        context = super(StoryHomeView, self).get_context_data(object_list=None, **kwargs)
        context['parameters'] = parameters
        if self.search:
            context['search'] = self.search

        return context


class ItemDetailView(DetailView):
    template_name = 'news/detail.html'
    model = News

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ItemDetailView, self).get_context_data(object_list=None, **kwargs)

        comments = News.objects.filter(type="COMMENT", parent=str(self.get_object().s_n))
        context['comments'] = comments

        return context
