# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import ulearn5.upc


class Ulearn5UpcLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=ulearn5.upc)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'ulearn5.upc:default')


ULEARN5_UPC_FIXTURE = Ulearn5UpcLayer()


ULEARN5_UPC_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ULEARN5_UPC_FIXTURE,),
    name='Ulearn5UpcLayer:IntegrationTesting'
)


ULEARN5_UPC_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ULEARN5_UPC_FIXTURE,),
    name='Ulearn5UpcLayer:FunctionalTesting'
)


ULEARN5_UPC_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ULEARN5_UPC_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='Ulearn5UpcLayer:AcceptanceTesting'
)
