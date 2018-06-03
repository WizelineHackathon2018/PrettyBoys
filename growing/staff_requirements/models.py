# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class StaffRequirement(models.Model):
    class Meta:
        verbose_name = "Staff Requirement"
        verbose_name_plural = "Staff Requirements"
        ordering = ("created",)
    
    def __str__(self):
        return '{}'.format(self.hard_skills)
    
    created = models.DateTimeField(auto_now_add=True)

    hard_skills = models.TextField()
    team_members = models.IntegerField()
    budget = models.IntegerField()
    range_start_date = models.DateField()
    deadline_project = models.DateField()
    email_notification = models.EmailField()

