from django import forms
from myApp.models import ImageModel,Member,Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'contact', 'dateofbirth', 'course', 'profile_picture', 'location']