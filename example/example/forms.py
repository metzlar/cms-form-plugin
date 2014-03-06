from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()

    def clean(self):
        data = super(ExampleForm, self).clean()

        # check validity of data['name']
        # do something with data['..']

        raise forms.ValidationError('Invalid')

        return data