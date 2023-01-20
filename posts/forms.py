from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': "form-control"}))


class AccountForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Password', required=False, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    confirm_password = forms.CharField(label='Confirm Password', required=False, widget=forms.PasswordInput(attrs={'class': "form-control"}))
    role = forms.ChoiceField(label='Role', choices=(('admin', 'admin'), ('editor', 'editor'), ('author', 'author'),), widget=forms.Select(attrs={'class': "form-select"}))

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords do not match')


class PostForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class': "form-control"}))
    publish_date = forms.DateField(label='Publish Date', widget=forms.DateInput(attrs={'class': "form-control"}))

