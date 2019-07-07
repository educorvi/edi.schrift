# -*- coding: utf-8 -*-
from edi.schrift.content.schrift import ISchrift  # NOQA E501
from edi.schrift.testing import EDI_SCHRIFT_INTEGRATION_TESTING  # noqa
from plone import api
from plone.api.exc import InvalidParameterError
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class SchriftIntegrationTest(unittest.TestCase):

    layer = EDI_SCHRIFT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_ct_schrift_schema(self):
        fti = queryUtility(IDexterityFTI, name='Schrift')
        schema = fti.lookupSchema()
        self.assertEqual(ISchrift, schema)

    def test_ct_schrift_fti(self):
        fti = queryUtility(IDexterityFTI, name='Schrift')
        self.assertTrue(fti)

    def test_ct_schrift_factory(self):
        fti = queryUtility(IDexterityFTI, name='Schrift')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            ISchrift.providedBy(obj),
            u'ISchrift not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_schrift_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='Schrift',
            id='schrift',
        )

        self.assertTrue(
            ISchrift.providedBy(obj),
            u'ISchrift not provided by {0}!'.format(
                obj.id,
            ),
        )

    def test_ct_schrift_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Schrift')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_schrift_filter_content_type_true(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='Schrift')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'schrift_id',
            title='Schrift container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
