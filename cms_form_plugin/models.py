from cms.models import CMSPlugin
from django.db import models
from django.conf import settings


class FormPlugin(CMSPlugin):
    form_class = models.CharField(
        max_length = 200,
        choices=settings.FORM_CLASSES
    )
    success_url = models.URLField(null = True)
    submit_caption = models.CharField(
        default = 'Submit',
        max_length = 200)