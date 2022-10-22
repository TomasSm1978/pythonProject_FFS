from django.contrib.auth.forms import UserCreationForm
from .models import User, Note, Category
from django import forms

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'image')


class NewNoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Note title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Note text'}))
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'image']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(NewNoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=self.request.user)


class UpdateNoteForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Note title'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'placeholder': 'Note text'}))
    class Meta:
        model = Note
        fields = ['title', 'text', 'category', 'image']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(UpdateNoteForm, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=self.request.user)