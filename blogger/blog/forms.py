from django import forms
from .models import Blog, Comments

class CreateEditBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'status', 'body')
        widgets = {
            'body' : forms.Textarea(attrs={'cols':80, 'rows':8}),
            # 'status': forms.Select(attrs={'onChange':'mystatus(this)'}),
        }

class CommentsForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Comment here (login is required)', 'rows':2}))
    class Meta:
        model = Comments
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={'rows':4})
        }
class ShareBlogForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder':'email@example.com'}))
    comment = forms.CharField(label='', required=False, widget=forms.Textarea(attrs={'placeholder':'message for your friend !!', 'rows':4}))
