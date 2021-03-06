from django import forms 
from recipe2.models import Author, Recipe


# class AddAuthorForm(forms.Form):
#     name = forms.CharField(max_length=80)
#     bio = forms.CharField(widget=forms.Textarea)

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=80)
    time_required = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    instruction = forms.CharField(widget=forms.Textarea)
    # author = forms.ModelChoiceField(queryset=Author.objects.all())

class AddLoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)

class AddSignupForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


