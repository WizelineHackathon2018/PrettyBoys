# -*- coding: utf-8 -*-
from rest_framework import serializers

# Import models
from staff_requirements.models import StaffRequirement

class StaffRequirementSerializer(serializers.ModelSerializer):
    """
        StaffRequirement serializer all fields
    """
    class Meta:
        model = StaffRequirement
        fields = '__all__'