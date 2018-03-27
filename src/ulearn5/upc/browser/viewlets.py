# -*- coding: utf-8 -*-
from five import grok
from Acquisition import aq_inner, aq_chain
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IAboveContent
from ulearn5.upc.interfaces import IUlearn5UpcLayer
from ulearn5.core.browser.viewlets import viewletBase
from ulearn5.core.content.community import ICommunity
from ulearn5.core.interfaces import IDocumentFolder, ILinksFolder, IPhotosFolder, IEventsFolder, INewsItemFolder

grok.context(Interface)


class viewletBaseUPC(viewletBase):
    grok.baseclass()


class folderBar(viewletBase):
    grok.name('upc.folderbar')
    grok.template('folderbar')
    grok.viewletmanager(IAboveContent)
    grok.layer(IUlearn5UpcLayer)

    def update(self):
        context = aq_inner(self.context)
        self.folder_type = ''
        for obj in aq_chain(context):
            if IDocumentFolder.providedBy(obj):
                self.folder_type = 'documents'
                break
            if ILinksFolder.providedBy(obj):
                self.folder_type = 'links'
                break
            if IPhotosFolder.providedBy(obj):
                self.folder_type = 'photos'
                break
            if IEventsFolder.providedBy(obj):
                self.folder_type = 'events'
                break
            if INewsItemFolder.providedBy(obj):
                self.folder_type = 'news'
                break
            if ICommunity.providedBy(obj):
                self.folder_type = 'community'
                break

    def bubble_class(self, bubble):
        width = 'col-xs-3'

        if bubble == self.folder_type:
            return 'active bubble top {}'.format(width)
        elif bubble == 'documents' and 'photos' == self.folder_type:
            return 'active bubble top {}'.format(width)
        else:
            return 'bubble top {}'.format(width)

    def get_community(self):
        context = aq_inner(self.context)
        for obj in aq_chain(context):
            if ICommunity.providedBy(obj):
                return obj

    def render_viewlet(self):
        context = aq_inner(self.context)
        for obj in aq_chain(context):
            if ICommunity.providedBy(obj):
                return True
        return False
