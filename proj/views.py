from pyramid.view import view_config

from .models import MyModel


@view_config(context=MyModel, route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'one': request.context, 'project': 'proj'}
