from django import forms
from .models import Remember


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class RememberForm(forms.ModelForm):
    class Meta:
        model = Remember
        fields = ['title', 'start_day', 'end_day', 'time']
        widgets = {
            'start_day': DateInput(),
            'end_day': DateInput(),
            'time': TimeInput(),
        }
