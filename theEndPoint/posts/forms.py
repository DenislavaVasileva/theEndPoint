from django import forms

from theEndPoint.posts.models import Post, Comment


class BasePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'post_image']

        labels = {
            'title': 'Title:',
            'content': "Content:",
            'category': "Category:",
            'post_image': "Image:",
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'content': forms.Textarea(attrs={
                'class': 'form-control'
            }),

            'author': forms.Select(attrs={
                'class': 'form-control',
            }),

            'category': forms.Select(attrs={
                'class': 'form-control',
            }),

            'post_image': forms.FileInput(attrs={
                'class': 'form-control',
            })
        }


class AddPostForm(BasePostForm):
    class Meta(BasePostForm.Meta):
        widgets = {
            **BasePostForm.Meta.widgets,
            'title': forms.TextInput(attrs={
                'placeholder': 'Add a title for your post',
                'class': 'form-control'
            }),

            'content': forms.Textarea(attrs={
                'placeholder': "Share your adventures or ask a question",
                'class': 'form-control'
            })
        }


class EditPostForm(BasePostForm):
    pass


class BaseDeleteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = []


class DeletePostForm(BaseDeleteForm):
    pass


class SearchForm(forms.Form):
    search = forms.CharField(
        label='',
        required=False,
        max_length=100,

        widget=forms.TextInput(attrs={
            'placeholder': 'Search for a post...',
            'class': 'form-control'
            }),
    )


class BaseCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        labels = {
            'content': "Content:",
        }

        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': "Write a comment",
                'class': 'form-control'
            }),
        }


class AddCommentForm(BaseCommentForm):
    pass


class EditCommentForm(BaseCommentForm):
    pass


class DeleteCommentForm(BaseDeleteForm):
    pass
