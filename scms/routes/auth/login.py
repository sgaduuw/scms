from flask import (
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_user

from scms.extensions import login_manager
from scms.routes.auth import auth, forms
from scms.models import User


@login_manager.user_loader
def load_user(user_id):

    return User.objects(pk=user_id).first()


@auth.route('/login/', methods=["GET", "POST"])
def login():
    form = forms.LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            # load user object by finding user_name
            obj_user = User.objects(user_name=form.user_name.data).first()
            # user exists
            if obj_user is not None:
                # check user pass against known hash
                if obj_user.check_password(form.pass_word.data):
                    login_user(obj_user)
                    # obj_user.save()

                    redirect_url = request.args.get("next") \
                        or url_for("admin.admin_page")
                    # return redirect('/admin/')
                    return redirect(redirect_url)

            return redirect('/login/')

    context = {
        'form': form
    }

    return render_template('login.html', **context)
