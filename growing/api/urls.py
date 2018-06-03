# -*- coding: utf-8 -*-
from django.conf.urls import url

# Import views
from views import StaffRequirementView, SelectedTeams

urlpatterns = [
    url(r'^staff-requirements/$', StaffRequirementView.as_view(), name='StaffRequirement'),
    url(r'^staff-requirements/(?P<pk>[0-9]+)/teams$', SelectedTeams.as_view(), name='StaffRequirementTeams'),
]