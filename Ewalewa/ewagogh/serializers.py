from rest_framework import serializers

from .models import Peeps

class PeepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Peeps
        fields = ('name', 'prompt')