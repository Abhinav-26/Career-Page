from rest_framework.serializers import ModelSerializer
from carrer import models

class JobSerializer(ModelSerializer):
    class Meta:
        model=models.Jobs
        fields="__all__"