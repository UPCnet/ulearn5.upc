# -*- coding: utf-8 -*-
from plone.registry.interfaces import IRegistry
from Products.CMFPlone.interfaces import INonInstallable
<<<<<<< 24f1a7397eb849d56c919126005d7c3cd2467ede
from Products.CMFPlone.interfaces.controlpanel import ISiteSchema
=======
from Products.CMFCore.utils import getToolByName
>>>>>>> Login with news and wflow customization
from zope.component import queryUtility
from zope.interface import implementer
from zope.component.hooks import getSite

from ulearn5.core.controlpanel import IUlearnControlPanelSettings

import transaction


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'ulearn5.upc:uninstall',
        ]


def post_install(context):
    """Post install script"""
    # Do something at the end of the installation of this package.


def uninstall(context):
    """Uninstall script"""
    # Do something at the end of the uninstallation of this package.


def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('ulearn5.upc_various.txt') is None:
        return

    registry = queryUtility(IRegistry)

    # Define colors of site
    context.settings = registry.forInterface(IUlearnControlPanelSettings)
    context.settings.main_color = u'#007AC1'
    context.settings.secondary_color = u'#007BC0'
    context.settings.background_property = u'transparent'
    context.settings.background_color = u'#EAE9E4'
    context.settings.buttons_color_primary = u'#34495E'
    context.settings.buttons_color_secondary = u'#34495E'
    context.settings.maxui_form_bg = u'#34495C'
    context.settings.alt_gradient_start_color = u'#FA5C2A'
    context.settings.alt_gradient_end_color = u'#ED4033'
    context.settings.color_community_closed = u'#007BC0'
    context.settings.color_community_organizative = u'#B5C035'
    context.settings.color_community_open = u'#888888'

    # Define logo for the toolbar
    site_tool = registry.forInterface(ISiteSchema, prefix='plone')
    site_tool.toolbar_logo = u'/upc-toolbarlogo.png'

    portal = getSite()
    wftool = getToolByName(portal['news'], 'portal_workflow')
    wftool.doActionFor(portal['news'], 'reject')
    wftool.doActionFor(portal['news']['aggregator'], 'reject')
    wftool.doActionFor(portal['news'], 'publish')
    wftool.doActionFor(portal['news']['aggregator'], 'publish')

    transaction.commit()
