from django.forms import ModelForm
from django import forms
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {'title' : forms.TextInput(attrs={'class':'form-control form-control-sm', 'placeholder':'Enter task ...'}),
                   'complete': forms.CheckboxInput(attrs={'class':'form-control form-check-input'}),}

        