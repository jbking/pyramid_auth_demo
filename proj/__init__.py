from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from sqlahelper import add_engine

from proj.resources import find_object


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    add_engine(engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/', factory=find_object)
    config.scan()
    return config.make_wsgi_app()

