# coding: utf-8
import re
from django import forms
from django.forms.models import ModelForm, BaseInlineFormSet
from django.utils.translation import ugettext_lazy as _

from .models import MapPlugin, RouteLocationPlugin


class MapPluginForm(ModelForm):
    class Meta:
        model = MapPlugin

    def clean(self):
        cleaned_data = super(MapPluginForm, self).clean()
        width = cleaned_data.get('width', '')
        height = cleaned_data.get('height', '')
        if width or height:
            CSS_WIDTH_RE = re.compile(r'^\d+(?:px|%)$')
            CSS_HEIGHT_RE = re.compile(r'^\d+px$')
            if width and not CSS_WIDTH_RE.match(width):
                self._errors['width'] = self.error_class([
                    _(u'Must be a positive integer followed by “px” or “%”.')])
            if height and not CSS_HEIGHT_RE.match(height):
                self._errors['height'] = self.error_class([
                    _(u'Must be a positive integer followed by “px”.')])
        return cleaned_data


class RouteLocationPluginForm(ModelForm):
    class Meta:
        model = RouteLocationPlugin

    def clean(self):
        # TODO: Do not allow more than 1 route per map
        return super(RouteLocationPluginForm, self).clean()
