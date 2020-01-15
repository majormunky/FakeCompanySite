from rest_framework import serializers
from core import models


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Widget
        exclude = []
