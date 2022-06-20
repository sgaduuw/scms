""" routes for scms app """
import random
from datetime import datetime
from urllib.parse import urlparse

import lorem
from flask import redirect, render_template, request, session, url_for

from scms import app
from scms.models import Content, Group, Permission, Site, User, m_session


@app.route('/')
def index():
    """ function for displaying the index page """
    # keep adding a page to the site, simply because we can and we eventually
    # will start hitting some scaling stuff.

    # select one random site to insert lorem into
    rnd_site = Site.query.find({'name': random.choice(['test01', 'test02', 'test03'])}).first()
    new_page = Content(
        title=lorem.get_sentence(),
        site_id=rnd_site._id,
        create_date=datetime.now(),
        body=lorem.get_paragraph(
            count=3,
            comma=(0, 2),
            word_range=(4, 8),
            sentence_range=(5, 10)
        )
    )
    m_session.flush_all()
    return render_template('index.html', payload=new_page, site=rnd_site)

@app.route('/list')
def list_pages():
    """ function for listing all pages on all sites """

    req_host = urlparse(request.base_url).hostname
    site = Site.query.find({"fqdns": req_host }).first()

    if site is not None:
        return render_template('list.html', site=site)

    return render_template('error.html', payload=req_host), 404

@app.route('/SA', methods=['GET', 'POST'], strict_slashes=False)
def super_admin():
    """ function for displaying the super admin page """
    if User.query.find().count() == 0:
        try:
            session['sa_logged_in']

        except KeyError:
            return redirect(url_for('super_admin_login'))

        else:
            from scms.scms.login_forms import CreateAdminForm
            form = CreateAdminForm()

            if form.validate_on_submit():
                new_group = Group.query.find_and_modify(
                    query={'group_name': 'admins'},
                    update={'$set': {'group_name': 'admins'}},
                    upsert=True,
                    new=True
                )
                print(f"New group: {new_group._id}")
                new_user = User(
                    first_name=form.new_first_name.data,
                    last_name=form.new_last_name.data,
                    username=form.new_username.data,
                    password=form.new_password.data,
                    groups=[new_group]
                )
                print(new_user)
                m_session.flush()

                session.pop('sa_logged_in', None)
                return redirect(url_for('super_admin'))

            return render_template('admin_super.html', form=form)

    return redirect(url_for('index'))

@app.route('/SA/login', methods=['GET', 'POST'], strict_slashes=False)
def super_admin_login():
    """ function for logging in to the superadmin page """
    if User.query.find().count() == 0:
        import os
        from scms.login_forms import SALoginForm

        form = SALoginForm()
        if os.getenv('SUPERADMIN_PASSWORD') is None:
            raise Exception('SUPERADMIN_PASSWORD environment variable not set')

        if form.validate_on_submit():
            if form.password.data == os.getenv('SUPERADMIN_PASSWORD'):
                session['sa_logged_in'] = True
                return redirect(url_for('super_admin'))

        return render_template('admin_super_login.html', form=form)

    return render_template('error.html'), 401


@app.route('/admin', methods=['GET', 'POST'], strict_slashes=False)
def normal_admin():
    """ function for displaying the super admin page """
    try:
        session['admin_logged_in']

    except KeyError:
        return render_template('admin_normal.html', active_admin=False), 401

    else:
        return render_template('admin_normal.html', active_admin=True)


@app.route('/admin/login', methods=['GET', 'POST'], strict_slashes=False)
def normal_admin_login():
    """ function for logging in to the normal admin page """
    from scms.login_forms import AdminLoginForm

    form = AdminLoginForm()

    if form.validate_on_submit():
        if form.username.data:
            user = User.query.find({ 'username': form.username.data }).first()
            print(f"user: {user}")
            validate = user.validate_password(form.password.data)
            print(f"validate: {validate}")
            if validate:
                session['admin_logged_in'] = True
                return redirect(url_for('normal_admin'))

    return render_template('admin_login.html', form=form)
