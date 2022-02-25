from django import forms
from .models import Post, Comment


class CreatePostForm(forms.ModelForm):
    """Create form to let user create new posts"""

    class Meta:
        """Get post model fields to add to form"""

        model = Post
        fields = ('title', 'body', 'post_picture')

class CommentsForm(forms.ModelForm):
    """Create new comments in comment section"""

    class Meta:
        """Add comments"""

        model = Comment
        fields = ('body',)
