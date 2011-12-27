from pyramid.config import Configurator

from lesscss_example.resources import less_resource


def home(request):
    """a simple view to test our resource"""
    less_resource.need()
    return {}

from lesscss_example.resources import bootstrap


def home2(request):
    """a simple view who use bootstrap"""
    bootstrap.need()
    return {}


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_fanstatic')

    config.add_route('home', '/')
    config.add_view(home, route_name='home',
                          renderer='templates/mytemplate.pt')

    config.add_static_view(name='fanstatic/lesscss_example',
                           path='pyramid_lesscss_sample:resources')
    config.add_route('bootstrap', '/bootstrap')
    config.add_view(home2, route_name='bootstrap',
                          renderer='templates/mytemplate.pt')

    return config.make_wsgi_app()
