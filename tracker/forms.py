from datetime import datetime
from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']

    deadline_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    deadline_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    def clean(self):
        cleaned_data = super().clean()
        deadline_date = cleaned_data.get('deadline_date')
        deadline_time = cleaned_data.get('deadline_time')

        if deadline_date and deadline_time:
            deadline = datetime.combine(deadline_date, deadline_time)
            cleaned_data['deadline'] = deadline

        return cleaned_data