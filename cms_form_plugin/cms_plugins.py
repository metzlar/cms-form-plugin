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
        
        instance = get_object_or_404(
            FormPlugin, pk = int(instance_id))

        if not request.method == 'POST':
            raise Http404('Not found')

        form = import_by_path(instance.form_class)
        form = form(request.POST)
            
        if form.is_valid():
            response = HttpResponseRedirect(
                request.POST['success_url']
            )
            response.delete_cookie('invalid_form')
            return response

        response = HttpResponseRedirect(
            request.POST['invalid_url']
        )
        # store the invalid form in a cookie
        response.set_cookie(
            'invalid_form',
            base64.urlsafe_b64encode(
                pickle.dumps(form))
        )
        return response

    def render(self, context, instance, placeholder):
        request = context['request']
        if 'invalid_form' in request.COOKIES:
            context['form'] = pickle.loads(
                base64.b64decode(
                    request.COOKIES.get('invalid_form')))
        else:
            form = import_by_path(instance.form_class)
            context['form'] = form()
        
        context.update({
            'post_to_url': reverse(
                'form_post', args=(instance.id,)
            ),
            'success_url': instance.success_url,
            'submit_caption': instance.submit_caption,
        })
        return context

        
plugin_pool.register_plugin(CMSFormPlugin)