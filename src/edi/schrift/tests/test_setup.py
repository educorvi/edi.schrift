# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from edi.schrift.testing import EDI_SCHRIFT_INTEGRATION_TESTING  # noqa: E501
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that edi.schrift is properly installed."""

    layer = EDI_SCHRIFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if edi.schrift is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'edi.schrift'))

    def test_browserlayer(self):
        """Test that IEdiSchriftLayer is registered."""
        from edi.schrift.interfaces import (
            IEdiSchriftLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IEdiSchriftLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = EDI_SCHRIFT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['edi.schrift'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if edi.schrift is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'edi.schrift'))

    def test_browserlayer_removed(self):
        """Test that IEdiSchriftLayer is removed."""
        from edi.schrift.interfaces import \
            IEdiSchriftLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IEdiSchriftLayer,
            utils.registered_layers())
