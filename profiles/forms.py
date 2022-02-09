from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    """User profile form to allow users to update their profile fields"""
    class Meta:
        """Get user data"""
        model = UserProfile
        fields = ('first_name', 'last_name', 'email', 'bio', 'favourite_game', 'user_picture')
