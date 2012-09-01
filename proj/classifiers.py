from pprint import pprint
from zope.interface import directlyProvides
from repoze.who.interfaces import IRequestClassifier
from repoze.who.classifiers import default_request_classifier


def static_request_classifier(environ):
    classifier = default_request_classifier(environ)
    if environ['PATH_INFO'].startswith('/static') and classifier == 'browser':
        return 'browser_static'
    return classifier


directlyProvides(static_request_classifier, IRequestClassifier)
