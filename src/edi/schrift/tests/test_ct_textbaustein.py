# -*- coding: utf-8 -*-
from edi.schrift.content.textbaustein import ITextbaustein  # NOQA E501
from edi.schrift.testing import EDI_SCHRIFT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class TextbausteinIntegrationTest(unittest.TestCase):

    layer = EDI_SCHRIFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'Schrift',
            self.portal,
            'textbaustein',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_textbaustein_schema(self):
        fti = queryUtility(IDexterityFTI, name='Textbaustein')
        schema = fti.lookupSchema()
        self.assertEqual(ITextbaustein, schema)

    def test_ct_textbaustein_fti(self):
        fti = queryUtility(IDexterityFTI, name='Textbaustein')
        self.assertTrue(fti)

    def test_ct_textbaustein_factory(self):
        fti = queryUtility(IDexterityFTI, name='Textbaustein')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ITextbaustein.providedBy(obj),
            u'ITextbaustein not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_textbaustein_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='Textbaustein',
            id='textbaustein',
        )

        self.assertTrue(
            ITextbaustein.providedBy(obj),
            u'ITextbaustein not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_textbaustein_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Textbaustein')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )
