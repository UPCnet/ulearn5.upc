# -*- coding: utf-8 -*-
from five import grok
from plone import api
from plone.app.users.browser.account import AccountPanelSchemaAdapter
from plone.app.users.browser.register import BaseRegistrationForm
from plone.app.users.browser.userdatapanel import UserDataPanel
from plone.directives import form
from plone.registry.interfaces import IRegistry
from plone.supermodel import model
from plone.z3cform.fieldsets import extensible
from repoze.catalog.catalog import Catalog
from repoze.catalog.indexes.field import CatalogFieldIndex
from repoze.catalog.indexes.keyword import CatalogKeywordIndex
from souper.interfaces import ICatalogFactory
from souper.soup import NodeAttributeIndexer
from z3c.form import field
from zope import schema
from zope.component import adapts
from zope.component import queryUtility
from zope.interface import Interface
from zope.interface import implementer

from ulearn5.core.controlpanel import IUlearnControlPanelSettings
from ulearn5.core.widgets.max_portrait_widget import MaxPortraitFieldWidget
from ulearn5.core.widgets.private_policy_widget import PrivatePolicyFieldWidget
from ulearn5.core.widgets.visibility_widget import VisibilityFieldWidget
from ulearn5.upc import _
from ulearn5.upc.interfaces import IUlearn5UpcLayer

import datetime


class IUlearnUserSchema(model.Schema):
    check_twitter_username = schema.Bool(
        title=_(u'', default=u''),
        required=False,
        default=True,
    )

    twitter_username = schema.TextLine(
        title=_(u'label_twitter', default=u'Twitter username'),
        description=_(u'help_twitter',
                      default=u'Fill in your Twitter username.'),
        required=False,
    )

    check_ubicacio = schema.Bool(
        title=_(u'', default=u''),
        required=False,
        default=True,
    )

    ubicacio = schema.TextLine(
        title=_(u'label_ubicacio', default=u'Ubicació'),
        description=_(u'help_ubicacio',
                      default=u'Equip, Àrea / Companyia / Departament'),
        required=False,
    )

    check_telefon = schema.Bool(
        title=_(u'', default=u''),
        required=False,
        default=True,
    )

    telefon = schema.TextLine(
        title=_(u'label_telefon', default=u'Telèfon'),
        description=_(u'help_telefon',
                      default=u'Contacte telefònic'),
        required=False,
    )

    # fieldset_private = schema.TextLine(
        # title=_(u'fieldset_private'),
        # description=_(u'help_fieldset_private'),
        # required=False,
        # readonly=True,
    # )

    private_policy = schema.Bool(
        title=_(u'private_policy'),
        required=True
    )

    time_accepted_private_policy = schema.Text(
        title=_(u'', default=u''),
    )


class UlearnUserDataSchemaAdapter(AccountPanelSchemaAdapter):
    schema = IUlearnUserSchema

    def get_check_twitter_username(self):
        return self._getProperty('check_twitter_username')

    def set_check_twitter_username(self, value):
        return self._setProperty('check_twitter_username', value is not False)

    check_twitter_username = property(get_check_twitter_username, set_check_twitter_username)

    def get_check_ubicacio(self):
        return self._getProperty('check_ubicacio')

    def set_check_ubicacio(self, value):
        return self._setProperty('check_ubicacio', value is not False)

    check_ubicacio = property(get_check_ubicacio, set_check_ubicacio)

    def get_check_telefon(self):
        return self._getProperty('check_telefon')

    def set_check_telefon(self, value):
        return self._setProperty('check_telefon', value is not False)

    check_telefon = property(get_check_telefon, set_check_telefon)

    def get_private_policy(self):
        return self._getProperty('private_policy')

    def set_private_policy(self, value):
        self._setProperty('time_accepted_private_policy', datetime.datetime.now().strftime("%H:%M:%S %d/%m/%Y"))
        return self._setProperty('private_policy', value is not False)

    private_policy = property(get_private_policy, set_private_policy)


class UlearnUserDataPanelExtender(extensible.FormExtender):
    adapts(Interface, IUlearn5UpcLayer, UserDataPanel)

    def update(self):
        fields = field.Fields(IUlearnUserSchema)
        # fields['fieldset_private'].widgetFactory = FieldsetFieldWidget
        # fields = fields.omit('telefon') # Si queremos quitar alguno de los que hemos añadido
        # self.remove('home_page') # Si queremos quitar los de la base (plone.app.users)
        fields['check_twitter_username'].widgetFactory = VisibilityFieldWidget
        fields['check_ubicacio'].widgetFactory = VisibilityFieldWidget
        fields['check_telefon'].widgetFactory = VisibilityFieldWidget
        self.form.fields['portrait'].widgetFactory = MaxPortraitFieldWidget

        # Private policy
        fields['private_policy'].widgetFactory = PrivatePolicyFieldWidget
        fields = fields.omit('time_accepted_private_policy')
        registry = queryUtility(IRegistry)
        ulearn_tool = registry.forInterface(IUlearnControlPanelSettings)
        if ulearn_tool.url_private_policy == None or ulearn_tool.url_private_policy == '' or api.user.get_current().getProperty('private_policy', False):
            fields = fields.omit('private_policy')

        self.add(fields)


class UlearnRegistrationPanelExtender(extensible.FormExtender):
    adapts(Interface, IUlearn5UpcLayer, BaseRegistrationForm)

    def update(self):
        fields = field.Fields(IUlearnUserSchema)
        # fields['fieldset_private'].widgetFactory = FieldsetFieldWidget
        fields['check_twitter_username'].widgetFactory = VisibilityFieldWidget
        fields['check_ubicacio'].widgetFactory = VisibilityFieldWidget
        fields['check_telefon'].widgetFactory = VisibilityFieldWidget
        fields = fields.omit('time_accepted_private_policy')
        fields = fields.omit('private_policy')
        self.add(fields)
