import unittest
import transaction

from pyramid import testing


class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        from sqlahelper import add_engine, get_session
        engine = create_engine('sqlite://')
        add_engine(engine)
        from .models import (
            Base,
            MyModel,
            )
        self.session = get_session()
        Base.metadata.create_all(engine)
        self.session = get_session()
        self.model = MyModel(name='one', value=55)
        self.session.add(self.model)

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def test_it(self):
        from .views import my_view
        request = testing.DummyRequest()
        request.context = self.model
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'proj')
