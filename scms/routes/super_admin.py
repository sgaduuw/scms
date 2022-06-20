""" function for super admin """

from flask import redirect, render_template, session, url_for
from scms import app
from scms.models import Group, User, m_session
from scms.login_forms import CreateAdminForm


@app.route('/SA', strict_slashes=False)
def super_admin():
    """ function for displaying the super admin page """
    if User.query.find().count() == 0:
        try:
            session['sa_logged_in']

        except KeyError:
            return redirect(url_for('super_admin_login'))

        else:
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
