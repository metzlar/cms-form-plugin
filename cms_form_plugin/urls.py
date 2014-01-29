from django.conf.urls import patterns, url

from cms_plugins import CMSFormPlugin

urlpatterns = patterns(
    '',
    url(
        '^form_post/(\d+)/?$',
        CMSFormPlugin.form_post,
        name='form_post'
    )
)