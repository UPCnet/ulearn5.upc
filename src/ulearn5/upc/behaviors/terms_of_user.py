from zope import schema
from zope.interface import implements
from zope.interface import alsoProvides
from zope.interface import Interface

from plone.directives import form

from ulearn5.upc import _
from ulearn5.core.content.community import ICommunity

class InvalidCheckError(schema.ValidationError):
    __doc__ = ""


def isChecked(value):
    if not value == True:
        raise InvalidCheckError
    return True


class ICommunityUPC(form.Schema):

    terms = schema.Bool(
        title=_(u'title_terms_of_user'),
        description=_(u'description_terms_of_user'),
        constraint=isChecked
    )

alsoProvides(ICommunityUPC, form.IFormFieldProvider)


class CommunityUPC(object):
    implements(ICommunityUPC)

    def __init__(self, context):
        self.context = context


class IRegisterSchemaUPC(Interface):

    terms = schema.Bool(
        title=_(u'title_terms_of_user'),
        description=_(u'description_terms_of_user'),
        constraint=isChecked
    )

alsoProvides(IRegisterSchemaUPC, form.IFormFieldProvider)


class RegisterSchemaUPC(object):
    implements(IRegisterSchemaUPC)

    def __init__(self, context):
        self.context = context
