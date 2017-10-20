from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
        view_name='snippet-highlight',
        format='html'
    )

    class Meta:
        model = Snippet
        fields = (
            'url', 'id', 'highlight',
            'owner', 'title', 'code',
            'linenos', 'language', 'style',
        )


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='snippet_detail',
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username', 'snippets')
