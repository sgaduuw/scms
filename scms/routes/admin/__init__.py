from flask import Blueprint
# from scms.extensions import login_manager

from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

from scms.models import User, Group, Permission, Site, Content, Category, Tag

admin_bp = Blueprint(
    'admin',
    __name__
)
admin = Admin(admin_bp, template_mode='bootstrap4')

# @login_manager.user_loader
# def load_user(user_id):

#     return User.objects(pk=user_id).first()

# from scms.routes.admin import index # noqa
# from scms.routes.admin import sites # noqa
admin.add_view(ModelView(Site))
admin.add_view(ModelView(Content))
admin.add_view(ModelView(Category))
admin.add_view(ModelView(Tag))
admin.add_view(ModelView(User))
admin.add_view(ModelView(Group))
admin.add_view(ModelView(Permission))
