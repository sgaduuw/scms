from flask import (
    render_template,
    request
)

from scms.routes.auth import auth, forms
from scms.models.auth import User


@auth.route('/register/', methods=["GET", "POST"])
def register():
    form = forms.RegisterForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user_info = {
                'user_name': form.user_name.data,
                'email': form.email.data,
                'first_name': form.first_name.data,
                'last_name': form.last_name.data
            }

            user_check = User.objects(user_name=form.user_name.data).first()
            if not user_check:
                new_user = User(**user_info)
                new_user.set_password(password=form.pass_word.data)
                new_user.save()

    context = {
        'form': form
    }

    return render_template('register.html', **context)
