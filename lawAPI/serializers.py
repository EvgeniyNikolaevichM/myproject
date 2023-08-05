from rest_framework import serializers
from systemStewartPlatform.models import *


class systemSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault()) # Автоматическое заоплнение автора

    class Meta:
        model = system_stewart_platform
        fields = '__all__'

class platformSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault()) # Автоматическое заоплнение автора

    class Meta:
        model = stewart_platform
        fields = '__all__'

class lawSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default = serializers.CurrentUserDefault()) # Автоматическое заоплнение автора

    class Meta:
        model = law_for_platform
        fields = '__all__'