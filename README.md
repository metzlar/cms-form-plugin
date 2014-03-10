cms-form-plugin
===============

Django CMS Form plugin inspired by django.views.generic.edit.FormView

Installation
------------

- This project is in Beta, clone it directly from github or execute: `pip install -e git+https://github.com/metzlar/cms-form-plugin#egg=cms-form-plugin`
- Add `cms_form_plugin` to `INSTALLED_APPS`
- Specify `FORM_CLASSES` in settings.py a tuple of tuples to be used as `choices` attribute to the plugin's `form_class` field. For example:
  
  FORM_CLASSES = (
      (
          'django.contrib.auth.forms.AuthenticationForm', 
          'Login Form'
      ),
  )

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

Now add `MyForm` to `settings.FORM_CLASSES` and start adding it to tthose placeholders.

CMS Form Plugin to a placeholder with `form_class` set to `myapp.forms.MyForm`
More configuration
------------------

**form_class** - full path to the class to use as form. Must be an entry from `settings.FORM_CLASSES` to make the plugin easier to use by civilians (non-developers).

**success_url** - url to redirect to when the form got successfully validated.

**success_page** - page to redirect to when no `success_url` is specified and the form got successfully validated. If both `success_url` and `success_page` are undefined, the redirect uses the current page.

**submit_caption** - caption for the submit button. Defaults to 'Submit'
