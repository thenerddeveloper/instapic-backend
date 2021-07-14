from rest_framework import serializers

from insta.models import Posts


class PostsSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    class Meta:
        model = Posts
        fields = '__all__'
