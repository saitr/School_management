from rest_framework import serializers
from .models import Admission_form

class AdmissionFormSerializer(serializers.ModelSerializer):
    signature = serializers.ImageField(read_only=False,required=False)
    photograph = serializers.ImageField(read_only=False,required=False)

    class Meta:
        model = Admission_form
        fields = '__all__'


class AdmissionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission_form
        fields= '__all__'