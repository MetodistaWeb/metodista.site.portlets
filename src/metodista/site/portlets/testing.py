# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import metodista.site.portlets
        self.loadZCML(package=metodista.site.portlets)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'metodista.site.portlets:default')


FIXTURE = Fixture()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='metodista.site.portlets:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='metodista.site.portlets:Functional',
)
