from rest_framework import serializers
from documents.models import *

class Embedding_serializer(serializers.ModelSerializer):
    class Meta:
        model=Embedding
        fields="__all__"