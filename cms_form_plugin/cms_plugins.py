from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import FormPlugin

from django.utils.translation import ugettext as _
from django.utils.module_loading import import_by_path
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponseRedirect

import base64
import pickle


class CMSFormPlugin(CMSPluginBase):
    model = FormPlugin
    name = _("Form")
    render_template = "form/form.html"

    @classmethod
    def form_post(cls, request, instance_id):
        '''
        Handles all POST requests from FormPlugin's form_class
        instances. If the form is valid, it calls the form's
        save method. If the form is not valid, it stores the
        form's pickled instance inside a cookie with name
        format invalid_form_%(instance_id) where instance_id
        is the id of the FormPlugin instance (to support multiple
        forms on one page)
        '''
        
        instance = get_object_or_404(
            FormPlugin, pk = int(instance_id))

        if not request.method == 'POST':
            raise Http404('Not found')

        form = import_by_path(instance.form_class)
        form = form(request.POST)
            
        if form.is_valid():
            if hasattr(form, 'save'):
                if hasattr(form.save, '__call__'):
                    form.save()
            response = HttpResponseRedirect(
                request.POST['success_url']
            )
            response.delete_cookie('invalid_form_%s' % instance_id )
            return response

        response = HttpResponseRedirect(
            request.POST['invalid_url']
        )
        # store the invalid form in a cookie
        response.set_cookie(
            'invalid_form_%s' % instance_id,
            base64.urlsafe_b64encode(
                pickle.dumps(form))
        )
        return response

    def render(self, context, instance, placeholder):
        '''
        Renders the plugin instance. If there is a pickled
        instance of the plugin's form_class in a cookie with name
        invalid_form_%(instance_id) we assume the form was
        submitted before but rendered invalid.
        '''
        form = None
        form_class = import_by_path(instance.form_class)
        request = context['request']
        if 'invalid_form_%s' % instance.id in request.COOKIES:
            try:
                form = pickle.loads(
                    base64.b64decode(
                        request.COOKIES.get(
                            'invalid_form_%s' % instance.id)))
                if not isinstance(form, form_class):
                    form = None
            except Exception:
                # a lot can go wrong here so just ignore
                pass
        if form is None:
            form = form_class()

        context['form'] = form
        
        context.update({
            'post_to_url': reverse(
                'form_post', args=(instance.id,)
            ),
            'success_url': instance.success_url,
            'submit_caption': instance.submit_caption,
        })
        return context

        
plugin_pool.register_plugin(CMSFormPlugin)