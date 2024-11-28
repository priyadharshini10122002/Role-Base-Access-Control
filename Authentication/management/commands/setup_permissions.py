from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from Management.models   import News  # Replace 'myapp' and 'MyModel' with your app and model

class Command(BaseCommand):
    help = 'Assign permissions to a group'

    def handle(self, *args, **kwargs):
        
        admin_group = Group.objects.get(name="Admin_User") 
        staff_group = Group.objects.get(name="Staff_User") 
        user_group = Group.objects.get(name="Basic_User") 
        content_type = ContentType.objects.get_for_model(News)

        # view_news = Permission.objects.get(codename='view_news')
        # change_news = Permission.objects.get(codename='change_news')
        # add_news = Permission.objects.get(codename='add_news')
        # delete_news = Permission.objects.get(codename='delete_news')

        # admin_group.permissions.set([view_news, change_news, add_news, delete_news])
        # staff_group.permissions.set([view_news, change_news, add_news])
        # user_group.permissions.set([view_news])


        admin_permissions = Permission.objects.filter(content_type=content_type, codename__in=[
            'add_news',
            'change_news',
            'delete_news',
            'view_news'
        ])
        staff_permissions = Permission.objects.filter(content_type=content_type, codename__in=[
            'add_news',
            'change_news',
            'view_news'
        ])
        user_permissions = Permission.objects.filter(content_type=content_type, codename__in=[
            'view_news'
        ])
        admin_group.permissions.set(admin_permissions)
        admin_group.save()
        staff_group.permissions.set(staff_permissions)
        staff_group.save()
        user_group.permissions.set(user_permissions)
        user_group.save()
        self.stdout.write(self.style.SUCCESS('Permissions set for groups: Admin_User, Staff_User, Basic_User'))

# from django.core.management.base import BaseCommand
# from django.contrib.auth.models import Group, Permission

# class Command(BaseCommand):
#     help = 'Set up groups and permissions'

#     def handle(self, *args, **kwargs):

#         view_student = Permission.objects.get(codename='view_student')
#         change_student = Permission.objects.get(codename='change_student')
#         add_student = Permission.objects.get(codename='add_student')
#         change_staff = Permission.objects.get(codename='change_staff')

#         staff_group, _ = Group.objects.get_or_create(name='Staff')
#         student_group, _ = Group.objects.get_or_create(name='Users')

#         staff_group.permissions.set([view_student, change_student, add_student, change_staff])
#         student_group.permissions.set([view_student, change_student])

#         self.stdout.write(self.style.SUCCESS("Groups and permissions have been set up successfully."))
