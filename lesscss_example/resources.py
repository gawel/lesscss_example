from fanstatic import Library
from js.lesscss import LessResource

library = Library('lesscss_example', 'resources')

less_resource = LessResource(library, 'main.less')

bootstrap = LessResource(library, 'bootstrap/lib/bootstrap.less')


def pserve():
    """A script aware of static resource"""
    import pyramid.scripts.pserve
    import pyramid_fanstatic
    import os

    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname, 'resources')
    pyramid.scripts.pserve.add_file_callback(
                pyramid_fanstatic.file_callback(dirname))
    pyramid.scripts.pserve.main()
