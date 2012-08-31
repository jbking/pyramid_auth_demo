from pyramid.httpexceptions import HTTPInternalServerError
from sqlahelper import get_session
from sqlalchemy.exc import DBAPIError

from .models import MyModel


def find_object(request):
    session = get_session()
    try:
        one = session.query(MyModel).filter(MyModel.name=='one').first()
    except DBAPIError:
        raise HTTPInternalServerError(explanation=conn_err_msg)
    return one


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_proj_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

