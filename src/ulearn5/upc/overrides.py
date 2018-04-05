from five import grok
from zope import schema

from Products.CMFPlone.interfaces import IPloneSiteRoot

from ulearn5.core.content.community import ICommunity
from ulearn5.core.content.community import communityAdder

from ulearn5.upc.interfaces import IUlearn5UpcLayer
from ulearn5.upc.behaviors.terms_of_user import ICommunityUPC


class ICommunityUPCPortlet(ICommunity, ICommunityUPC):
    pass


class communityAdderUPC(communityAdder):
    grok.name('addCommunity')
    grok.context(IPloneSiteRoot)
    grok.require('ulearn.addCommunity')
    grok.layer(IUlearn5UpcLayer)

    schema = ICommunityUPCPortlet
    ignoreContext = True
