from rest_framework import serializers
from repos.models import Repo


class RepoSerializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only=True)
    title       = serializers.CharField(required=False, allow_blank=True, max_length=100)
    url         = serializers.CharField(required=False, allow_blank=True, max_length=100)
    user_name   = serializers.CharField(required=False, allow_blank=True, max_length=100)
    repo_name   = serializers.CharField(required=False, allow_blank=True, max_length=100)
    branch      = serializers.CharField(required=False, allow_blank=True, max_length=100)

    
    
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('language', instance.language)
        instance.save()
        return instance
