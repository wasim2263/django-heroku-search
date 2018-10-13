from django.contrib.auth.models import User, Group
from rest_framework import serializers
from developersearch.models import Developer, ProgrammingLanguage, Language


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = (['code'])

class ProgrammingLanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = (['name'])


class DeveloperSerializer(serializers.HyperlinkedModelSerializer):
    languages = LanguageSerializer(read_only=True, many=True)
    programming_languages = ProgrammingLanguageSerializer(read_only=True, many=True)

    class Meta:
        model = Developer
        fields = (['id', 'email', 'languages', 'programming_languages'])

