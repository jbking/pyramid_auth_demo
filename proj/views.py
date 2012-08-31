from pyramid.response import Response
from pyramid.view import view_config, forbidden_view_config

from .models import MyModel


@view_config(context=MyModel, route_name='home',
             permission='view',
             renderer='templates/mytemplate.pt')
def my_view(request):
    return {'one': request.context, 'project': 'proj'}


@forbidden_view_config()
def forbidden(request):
    return Response('''
        <h1>Forbidden</h1>
        <h2 style="-moz-transform: rotate(90deg);
                   -webkit-transform: rotate(90deg);
                   width: 100px; margin-top: 50px">X-(</h2>''')
