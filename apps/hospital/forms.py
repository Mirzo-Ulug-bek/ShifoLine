from django import forms
from .models import Region, Hospital, ImageHospital, Department, Doctor

class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields = '__all__'

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class ImageHospitalForm(forms.ModelForm):
    class Meta:
        model = ImageHospital
        fields = '__all__'

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'