from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config
from sqlahelper import add_engine

from proj.resources import find_object


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    add_engine(engine)
    authentication_policy = AuthTktAuthenticationPolicy('seekrit')
    authorization_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings)
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/', factory=find_object)
    config.scan()
    return config.make_wsgi_app()

