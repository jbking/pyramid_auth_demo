from pyramid.security import remember, forget, authenticated_userid
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config

from .models import MyModel


@view_config(context=MyModel, route_name='home',
             permission='view',
             renderer='templates/mytemplate.pt')
def my_view(request):
    return {'one': request.context, 'project': 'proj'}


@forbidden_view_config()
def forbidden(request):
    return Response(''
        '<h1>Forbidden</h1>'
        '<h2 style="-moz-transform: rotate(90deg);'
                   '-webkit-transform: rotate(90deg);'
                   'width: 100px; margin-top: 50px">X-(</h2>')


@view_config(route_name='remember')
def remember_view(request):
    userid = authenticated_userid(request)
    if userid is None:
        headers = remember(request, 'friend')
        return Response('<h1>I remember you</h1>', headers=headers)
    else:
        return Response('<h1>I know you :)</h1>')


@view_config(route_name='forget')
def forget_view(request):
    userid = authenticated_userid(request)
    if userid is not None:
        headers = forget(request)
        return Response('<h1>I forget you</h1>', headers=headers)
    else:
        return Response('<h1>Who are you?</h1>')
