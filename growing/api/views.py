# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import tools
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import random

# Import models
from staff_requirements.models import StaffRequirement

# Import serializers
from serializers import StaffRequirementSerializer


class StaffRequirementView(APIView):
    """
        Viewset for StaffRequirement
    """
    def get(self, request):
        return Response([{'test': 'value'}])

    def post(self, request, *args, **kwargs):
        staff_requirement_serializer = StaffRequirementSerializer(data=request.data)
        if staff_requirement_serializer.is_valid():
            staff_requirement_serializer.save()
            return Response(staff_requirement_serializer.data, status=status.HTTP_201_CREATED)
        return Response(staff_requirement_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SelectedTeams(APIView):
    """
        Viewset for SelectedTeams
    """

    def get_object(self, pk):
        try:
            return StaffRequirement.objects.get(pk=pk)
        except StaffRequirement.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        staff_requirement = self.get_object(pk)
        serializer = StaffRequirementSerializer(staff_requirement)
        
        measure = [0.5,1]
        teams = [
            {
                'seniority':random.choice(measure),
                'analyst':random.choice(measure),
                'diplomat':random.choice(measure),
                'sentinel':random.choice(measure),
                'explorer':random.choice(measure),
            },
            {
                'seniority':random.choice(measure),
                'analyst':random.choice(measure),
                'diplomat':random.choice(measure),
                'sentinel':random.choice(measure),
                'explorer':random.choice(measure),
            },
            {
                'seniority':random.choice(measure),
                'analyst':random.choice(measure),
                'diplomat':random.choice(measure),
                'sentinel':random.choice(measure),
                'explorer':random.choice(measure),
            },
        ]
        
        return Response(teams)