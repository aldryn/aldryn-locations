from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import MapPluginForm, RouteLocationPluginForm
from .models import LocationPlugin, MapPlugin, RouteLocationPlugin


class LocationsBase(CMSPluginBase):
    module = 'Locations'


class MapCMSPlugin(LocationsBase):
    model = MapPlugin
    name = _('Map')
    render_template = "aldryn_locations/plugins/locations.html"
    admin_preview = True
    form = MapPluginForm
    allow_children = True
    child_classes = ('LocationCMSPlugin', 'RouteLocationCMSPlugin')
    fieldsets = (
        (None, {
            'fields': (('title', 'map_type'))
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('route_planner_title', 'zoom',
                       ('width', 'height',),
                       ('scrollwheel', 'double_click_zoom', 'keyboard_shortcuts', 'draggable'),
                       ('pan_control', 'zoom_control', 'street_view_control')),
        }),
    )

    def render(self, context, instance, placeholder):
        def prepare_item(item):
            return {
                'address': "%s, %s %s" % (item.address, item.zipcode, item.city),
                'latlng': item.get_lat_lng() or None,
                'content': item.content or None,
                'admin': reverse('admin:cms_page_edit_plugin', args=[item.pk]),
            }

        location_data = [
            prepare_item(location) for location in instance.child_plugin_instances
        ]

        # Options for the map comes from plugin so I assigned it here
        options = {
            'scrollwheel': instance.scrollwheel,
            'disableDoubleClickZoom': not instance.double_click_zoom,
            'draggable': instance.draggable,
            'keyboardShortcuts': instance.keyboard_shortcuts,
            'panControl': instance.pan_control,
            'zoomControl': instance.zoom_control,
            'streetViewControl': instance.street_view_control,
        }

        if instance.get_route_planner():
            route_planner = '%s, %s %s' % (instance.get_route_planner())
        else:
            route_planner = None

        context.update({
            'object': instance,
            'zoom': instance.zoom if instance.zoom else 'false',
            'placeholder': placeholder,
            'locations': json.dumps(location_data),
            'options': json.dumps(options),
            'map_type': json.dumps(instance.map_type),
            'route_planner': json.dumps(route_planner)
        })

        return context

plugin_pool.register_plugin(MapCMSPlugin)


class LocationCMSPlugin(LocationsBase):
    render_template = "aldryn_locations/plugins/empty.html"
    model = LocationPlugin
    name = _('Location')
    require_parent = True
    parent_classes = ['MapCMSPlugin']
    fieldsets = (
        (None, {
            'fields': ('address', ('zipcode', 'city',)),
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('content', ('lat', 'lng'),),
        }),
    )

plugin_pool.register_plugin(LocationCMSPlugin)


class RouteLocationCMSPlugin(LocationCMSPlugin):
    model = RouteLocationPlugin
    form = RouteLocationPluginForm
    name = _('Route Location')

plugin_pool.register_plugin(RouteLocationCMSPlugin)
