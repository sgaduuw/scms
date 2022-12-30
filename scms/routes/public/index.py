from flask import render_template, request

from scms.models import Content, Site
from scms.routes.public import public


@public.route('/')
def index():
    # Quering the fqdns list in the Site model using fqdns__in
    # requires a list to be passed.
    host = request.host.rsplit(':', 1)[0]
    site = Site.objects(fqdns__in=[host]).first()
    # using site.id, we can determine our content query
    list_content = Content.objects(site=site)

    context = {
        'site': site,
        'list_content': list_content
    }

    return render_template('index.j2', **context)
