from rest_framework.serializers import ModelSerializer # pip install?
from rest_framework.viewsets import ModelViewSet
from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')
