from django.forms import ModelForm, widgets

class ProfileForm(ModelForm):
    class Meta:
        model = profile
        exclude = [ 'id', 'user' ]
        widgets = {
            'favorite_category': widgets.Select(attrs={'class': 'form-control'}),
            'profile_photo':widgets.TextInput(attrs={'class': 'form-control'})
        }