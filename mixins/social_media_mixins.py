from contact.models import SocialMedia


class SMMixin(object):
    def get_context_data(self, **kwargs):
        context = super(SMMixin, self).get_context_data(**kwargs)
        context['medias'] = SocialMedia.objects.all()
        print(context)
        return context
