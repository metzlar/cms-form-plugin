cms-form-plugin
===============

Django CMS Form plugin inspired by django.views.generic.edit.FormView

Installation
------------

- `pip install cms-form-plugin`
- Add `cms_form_plugin` to `INSTALLED_APPS`
- Include `cms_form_plugin.urls` in your `urlpatterns`
- Run `manage.py migrate cms_form_plugin`


Usage
-----

Add CMS Form Plugin to any placeholder. It requires `form_class` to be configured per plugin instance. `form_class` points to the full path of the Django Form subclass you want to include.

Consider the following form in `myapp.forms` :

    class MyForm(forms.Form):
        name = forms.CharField()
        category = forms.CharField()

        def clean(self):
            data = super(MyForm, self).clean()
   
            # check validity of data['name']
            # do something with data['..']

            if not_valid:
                raise forms.ValidationError('Invalid')

Now add CMS Form Plugin to a placeholder with `form_class` set to `myapp.forms.MyForm`

More configuration
------------------

**form_class** - full path to the class to use as form

**success_url** - url to redirect to when the form got successfully validated. Defaults to the current url of the page containing the placeholder.

**submit_caption** - caption for the submit button. Defaults to 'Submit'