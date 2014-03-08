from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField()
    category = forms.CharField()

    def clean(self):
        data = super(ExampleForm, self).clean()

        # check validity of data['name']
        # do something with data['..']

        for k,v in data.iteritems():
            if v != 'valid':
                raise forms.ValidationError('Invalid')

        return data