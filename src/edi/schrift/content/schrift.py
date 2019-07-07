# -*- coding: utf-8 -*-
import random
from DateTime import DateTime
# from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer
from plone import api as ploneapi
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from edi.schrift import _

schrifttyp = SimpleVocabulary(
    [SimpleTerm(value=u'dp-pruefstellen-info', title=_(u'DP-Prüfstellen-Info')),
     SimpleTerm(value=u'dp-info', title=_(u'DP-Info'))]
    )

def genWebcode():
    aktuell=unicode(DateTime()).split(' ')[0]
    neujahr='%s/01/01' %str(DateTime()).split(' ')[0][:4]
    konstante=unicode(aktuell[2:4])
    zufallszahl=unicode(random.randint(100000, 999999))
    code=konstante+zufallszahl
    results = ploneapi.content.find(Webcode=code, created={"query":[neujahr,aktuell],"range":"minmax"})
    while results:
        zufallszahl=unicode(random.randint(100000, 999999))
        code=konstante+zufallszahl
        results = ploneapi.content.find(Webcode=code, created={"query":[neujahr,aktuell],"range":"minmax"})
    return code


class ISchrift(model.Schema):
    """ Marker interface and Dexterity Python Schema for Schrift
    """
    
    title = schema.TextLine(title=u"Titel der Schrift",
                            description=u"Der Titel der Schrift wird auf das PDF gedruckt")

    description = schema.Text(title=u"Kurzbeschreibung",
                            description=u"Die Kurzbeschreibung wird nur Online angezeigt.",
                            required=False)

    typ = schema.Choice(title=u"Typ der Schrift",
                        description=u"Bitte wählen Sie einen Schrifttyp aus.",
                        vocabulary=schrifttyp) 

    stand = schema.Date(title=u"Stand der Schrift",
                        description=u"Ohne Angabe wird automtatisch das Änderungsdatum verwendet.",
                        required=False)

    infonr = schema.TextLine(title=u"Info-Nr",
                        description=u"Die Angabe wird momentan nur für die DP-Prüfstellen-Info benötigt.",
                        required=False)

    webcode = schema.TextLine(title=u"Webcode",
                        description=u"Der Webcode wird automatisch beim Anlegen der Schrift erzeugt.",
                        defaultFactory=genWebcode)


@implementer(ISchrift)
class Schrift(Container):
    """
    """
