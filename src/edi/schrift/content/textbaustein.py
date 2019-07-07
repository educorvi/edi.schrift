# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from edi.schrift import _


class ITextbaustein(model.Schema):
    """ Marker interface and Dexterity Python Schema for Textbaustein
    """

    title = schema.TextLine(title=u"Titel des Textbausteins",
                            description=u"Der Titel des Texbausteins wird nur in der redaktionellen Inhaltsübersicht angezeigt.")

    text = RichText(title=u"Texbaustein",
                    description=u"Sie bearbeiten hier einen Textabschnitt der Schrift. Bitte betten Sie keine Bilder in die Schrift ein.")


@implementer(ITextbaustein)
class Textbaustein(Item):
    """
    """
