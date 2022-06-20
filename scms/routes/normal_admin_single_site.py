""" admin function for modifying a single site """

from flask import render_template, session
from scms import app
from scms.admin_forms import SiteInfoForm
from scms.models import Site, m_session


@app.route('/admin/site/<string:site_name>', methods=['GET', 'POST'], strict_slashes=False)
def normal_admin_single_site(site_name):
    """ function for displaying the super admin page """
    try:
        session['admin_logged_in']

    except KeyError:
        return render_template('admin_normal_single_site.html', active_admin=False), 401

    else:
        site = Site.query.get(name=site_name)
        # this feels pretty perly, i like it!
        form = SiteInfoForm() if site is None else SiteInfoForm(
            name=site.name,
            title=site.title,
            tagline=site.tagline,
            description=site.description,
            copyright=site.copyright,
            fqdns=str(",".join(site.fqdns))
        )

        if form.validate_on_submit():
            site_name = form.name.data
            site_fqdns = form.fqdns.data.split(',')
            site_title = form.title.data
            site_tagline = form.tagline.data
            site_description = form.description.data
            site_copyright = form.copyright.data

            site = Site.query.find_and_modify(
                query={'name': site_name},
                update={
                    '$set': {
                        'name': site_name,
                        'fqdns': site_fqdns,
                        'title': site_title,
                        'tagline': site_tagline,
                        'description': site_description,
                        'copyright': site_copyright
                    }
                },
                upsert=True,
                new=True
            )
            m_session.flush()

        else:
            print(f"NOT submitted.")
            print(f"ERORS: {form.errors}")

        return render_template('admin_normal_single_site.html', active_admin=True, site=site, form=form)
