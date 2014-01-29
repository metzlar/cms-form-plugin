from cms.models import CMSPlugin
from django.db import models


class FormPlugin(CMSPlugin):
    form_class = models.CharField(max_length = 200)
    success_url = models.URLField(null = True)
    submit_caption = models.CharField(
        default = 'Submit',
        max_length = 200)