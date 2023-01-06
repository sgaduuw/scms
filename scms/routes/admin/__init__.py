from flask import Blueprint
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.mongoengine import ModelView
from flask_login import login_required

# from scms.extensions import login_manager
from scms.models import User, Group, Permission, Site, Content, Category, Tag


# Create a login-required decorator
def login_required_admin(view):
    @login_required
    def wrapper(*args, **kwargs):
        return view(*args, **kwargs)
    return wrapper


admin_bp = Blueprint(
    'admin',
    __name__
)


# Create a login-required AdminIndexView
class LoginRequiredAdminIndexView(AdminIndexView):
    @login_required_admin
    def index(self):
        return super(LoginRequiredAdminIndexView, self).index()


# Create a login-required ModelView
class LoginRequiredModelView(ModelView):
    @login_required_admin
    def is_accessible(self):
        return super(LoginRequiredModelView, self).is_accessible()


# Create an Admin instance
admin = Admin(admin_bp, template_mode='bootstrap4')

admin.add_view(LoginRequiredModelView(Site))
admin.add_view(LoginRequiredModelView(Content))
admin.add_view(LoginRequiredModelView(Category))
admin.add_view(LoginRequiredModelView(Tag))
admin.add_view(LoginRequiredModelView(User))
admin.add_view(LoginRequiredModelView(Group))
admin.add_view(LoginRequiredModelView(Permission))
