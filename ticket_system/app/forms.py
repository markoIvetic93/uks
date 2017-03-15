from django import forms
from django.forms import ModelForm
from .models import Issue


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class IssueForm(ModelForm):

    class Meta:
        model = Issue
        fields = ['title', 'endDate', 'createdBy', 'assignedTo', 'project', 'status', 'priority', 'description', 'spentTime', 'donePercentage']
        widgets = {
            'startDate': DateInput(),
            'endDate': DateInput(),
            'spentTime': TimeInput(),
        }
