# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import IPloneSiteRoot
from five import grok
from zope.interface import alsoProvides

from ulearn5.upc.interfaces import IUlearn5UpcLayer


class resetUserPropertiesCatalog(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('reset_user_catalog')
    grok.require('ulearn.APIAccess')
    grok.layer(IUlearn5UpcLayer)

    def render(self):
        return "Ho sentim, però en l'entorn d'UPC no es pot llançar aquesta vista."


class reBuildUserPropertiesCatalog(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('rebuild_user_catalog')
    grok.require('ulearn.APIAccess')
    grok.layer(IUlearn5UpcLayer)

    def render(self):
        try:
            from plone.protect.interfaces import IDisableCSRFProtection
            alsoProvides(self.request, IDisableCSRFProtection)
        except:
            pass

        return "Ho sentim, però en l'entorn d'UPC no es pot llançar aquesta vista."


class DeleteUserPropertiesCatalog(grok.View):
    grok.context(IPloneSiteRoot)
    grok.name('delete_user_catalog')
    grok.require('ulearn.APIAccess')
    grok.layer(IUlearn5UpcLayer)

    def render(self):
        try:
            from plone.protect.interfaces import IDisableCSRFProtection
            alsoProvides(self.request, IDisableCSRFProtection)
        except:
            pass

        return "Ho sentim, però en l'entorn d'UPC no es pot llançar aquesta vista."
