# coding: utf-8
import re

from django.forms.models import ModelForm
from django.utils.translation import ugettext_lazy as _

from .models import MapPlugin, RouteLocationPlugin, EmbedViewPlugin


class MapPluginForm(ModelForm):

    class Meta:
        model = MapPlugin
        fields = [
            'title',
            'zoom',
            'route_planner_title',
            'width',
            'height',
            'scrollwheel',
            'double_click_zoom',
            'draggable',
            'keyboard_shortcuts',
            'pan_control',
            'zoom_control',
            'street_view_control',
            'map_type',
        ]

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
        fields = [
            'address',
            'zipcode',
            'city',
            'content',
            'lat',
            'lng',
        ]

    def clean(self):
        # TODO: Do not allow more than 1 route per map
        return super(RouteLocationPluginForm, self).clean()


class EmbedViewPluginForm(ModelForm):

    class Meta:
        model = EmbedViewPlugin
        fields = [
            'query',
            'map_type',
            'center',
            'zoom',
            'ui_lang',
            'region',
            'width',
            'height',
        ]

    def __init__(self, *args, **kwargs):
        super(EmbedViewPluginForm, self).__init__(*args, **kwargs)
        self.fields['center'].required = True
