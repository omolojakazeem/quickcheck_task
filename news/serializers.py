from rest_framework import serializers
from .models import News


class NewsCreateSerializer(serializers.ModelSerializer):
    s_n = serializers.CharField(required=False)

    class Meta:
        model = News
        fields = [
            'id', 's_n', 'deleted', 'type', 'by', 'time', 'dead', 'kids', 'parts', 'descendants', 'parent', 'score',
            'title', 'text', 'url',
        ]
