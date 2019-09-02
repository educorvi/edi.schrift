# -*- coding: utf-8 -*-

from edi.schrift import _
from Products.Five.browser import BrowserView
from edi.schrift.content.schrift import schrifttyp


# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class SchriftView(BrowserView):

    def getSchriftHeader(self):
        header = {}
        header['typ'] = schrifttyp.getTerm(self.context.typ).title
        header['stand'] = self.context.modified().strftime('%d.%m.%Y')
        if self.context.stand:
            header['stand'] = self.context.stand.strftime('%d.%m.%Y')
        return header

    def getSchriftContent(self):
        fc = self.context.getFolderContents()
        html = ''
        for i in fc:
            obj = i.getObject()
            if obj.portal_type == "Textbaustein":
                if obj.text:
                    html += obj.text.output
            if obj.portal_type == "Image":
                if obj.image:
                    imgurl = '%s/@@images/image' % obj.absolute_url()
                    html += '<p><img class="img-responsive inline" src="%s" title="%s"></p>' % (imgurl, obj.title)
                if obj.description:
                    html += '<p class="discreet">%s</p>' % obj.description
        return html
