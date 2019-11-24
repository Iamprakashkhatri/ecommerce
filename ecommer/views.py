from django.shortcuts import render,reverse,redirect
from .forms import LoginForm
from django.views.generic.edit import FormView
from .models import Member
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User,Group

from .models import Task,Site,Post

from rolepermissions.decorators import has_role_decorator
from guardian.shortcuts import assign_perm

from rolepermissions.mixins import HasRoleMixin

class DashboardView(HasRoleMixin,FormView):
    allowed_roles = 'doctor'


    def get(self, request):
        members=Member.objects.all()
        # content = {}
        # content['userdetail'] = member
        return render(request, 'ecommer/dashboard.html', {'members':members})
        # content = {}
        # if request.member.is_authenticated:
        #     member = request.member
        #     content['userdetail'] = member
        #     return render(request, 'dashboard.html', content)
        # else:
        #     return redirect(reverse('login-view'))


class LoginView(FormView):
    content = {}
    content['form'] = LoginForm
    # member=Member.objects.all()
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginView, self).dispatch(request, *args, **kwargs)
    def get(self, request):

        return render(request, 'ecommer/login.html', self.content)

    def post(self, request):
        content = {}
        email = request.POST['email']
        password = request.POST['password']
        try:
            members = Member.objects.filter(email=email)
            member = authenticate(request,email=email,password=password)
            login(request, member)
            return redirect('ecommer:dashboard-view')
        except Exception as e:
            content = {}
            content['form'] = LoginForm
            # content['error'] = 'Unable to login with provided credentials' + e
            return render('ecommer/login.html', content)

@has_role_decorator('nurse')
def my_view(request, *args, **kwargs):
    members = Member.objects.all()
    # content = {}
    # content['userdetail'] = member

    from rolepermissions.checkers import has_permission
    from django.contrib.auth.models import User

    from ecommerce.roles import Doctor

    from rolepermissions.permissions import available_perm_status
    from rolepermissions.checkers import has_object_permission
    user1 = User.objects.get(id=2)
    permissions = available_perm_status(user1)
    print(permissions)

    if has_permission(user1, 'nurse'):
        print('access granted')
    else:
        print('access not granted')
    if has_object_permission('access_clinic', user1, user1):
        print('access granted')

    from guardian.shortcuts import get_perms
    from guardian.shortcuts import assign_perm
    from guardian.shortcuts import get_perms
    from django.shortcuts import render
    from django.template import RequestContext
    from ecommer.models import Project
    from guardian.shortcuts import get_objects_for_user
    joe=User.objects.get(username='joe')
    post=Post.objects.get(id=1)
    # print(joe.has_perm('post_add', post))
    assign_perm('post_add', joe, post)
    projects = get_objects_for_user(request.user, 'ecommer.post_add')
    print(joe.has_perm('post_add', post))
    # if 'post_add' in get_perms(joe, post):
    #     projects = get_objects_for_user(request.user, 'ecommer.post_add')
    #     print(projects)
    #       print('access granted')
    # else:
    #     print('access denied')
    return render(request, 'ecommer/user_dashboard.html', {'projects': projects})
from rolepermissions.permissions import register_object_checker

from django.views.generic import TemplateView
from rolepermissions.mixins import HasRoleMixin


from django.shortcuts import render
from django.template import RequestContext
from ecommer.models import Project
from guardian.shortcuts import get_objects_for_user


def user_dashboard(request):
    joe = User.objects.get(username='joe')
    post = Post.objects.get(id=1)
    # print(joe.has_perm('post_add', post))
    assign_perm('post_add', joe, post)
    projects = get_objects_for_user(request.user, 'ecommer.post_add')

    from guardian.core import ObjectPermissionChecker
    joe = User.objects.get(username='joe')
    projects = Post.objects.all()
    checker = ObjectPermissionChecker(joe)
    # Prefetch the permissions
    checker.prefetch_perms(projects)
    for project in projects:
        # No additional lookups needed to check permissions
        print(checker.has_perm('post_add', project))



    return render(request, 'ecommer/user_dashboard.html', {'projects': projects})

# joe = User.objects.get(username='joe')
# foobars = Group.objects.create(name='foobars')

# from guardian.decorators import permission_required_or_403
# from django.http import HttpResponse
# @permission_required_or_403('auth.change_group',(Group, 'name', 'group_name'))
# def edit_group(request, group_name):
#     return HttpResponse('some form')
#
# from django.http import HttpRequest
# request = HttpRequest()
# request.user = joe
# print(edit_group(request, group_name='foobars'))

# joe.groups.add(foobars)
# edit_group(request, group_name='foobars')
# from guardian.shortcuts import assign_perm
# assign_perm('auth.change_group', joe, foobars)
# edit_group(request, group_name='foobars')
