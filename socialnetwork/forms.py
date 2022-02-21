from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    """Create form to let user create new posts"""

    class Meta:
        """Get post model fields to add to form"""

        model = Post
        fields = ('title', 'body', 'post_picture')
