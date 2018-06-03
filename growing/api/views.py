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
        # return Response(serializer.data)
        # return Response(serializer.data['hard_skills'].split(','))
        teams = [
            {
                'team': {
                    'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                },
                'members':[
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                ]
            },
            {
                'team': {
                    'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                },
                'members':[
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                ]
            },
            {
                'team': {
                    'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                },
                'members':[
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                ]
            },
            {
                'team': {
                    'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                },
                'members':[
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                    {
                        'name': 'hello my name is',
                        'chart': [
                            {
                                "axis": "Work Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Technical Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Charisma",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Grit/Determination",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Teaching Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Hustle Ability",
                                "value": round(random.uniform(0,1),2)
                            },
                            {
                                "axis": "Honesty & Sincerity",
                                "value": round(random.uniform(0,1),2)
                            }
                        ]
                    },
                ]
            },
        ]
        
        return Response(teams)