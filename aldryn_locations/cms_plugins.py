import json

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .forms import MapPluginForm, RouteLocationPluginForm, EmbedViewPluginForm
from .models import LocationPlugin, MapPlugin, RouteLocationPlugin, EmbedPlacePlugin, EmbedViewPlugin, \
    EmbedSearchPlugin, EmbedDirectionsPlugin


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
                'content': item.get_content(),
                'admin': reverse('admin:cms_page_edit_plugin', args=[item.pk]),
            }

        if instance.child_plugin_instances:
            location_data = [
                prepare_item(location) for location in instance.child_plugin_instances
            ]
        else:
            location_data = []

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


class RouteLocationCMSPlugin(LocationCMSPlugin):
    model = RouteLocationPlugin
    form = RouteLocationPluginForm
    name = _('Route Location')


# 'New Maps' embed plugins (IFrame)

class EmbedMapCMSPluginBase(LocationsBase):
    render_template = "aldryn_locations/plugins/locations_embed.html"
    fieldsets = (
        (None, {
            'fields': ('query', ),
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('center', 'zoom', 'map_type', 'ui_lang', 'region', ('height', 'width')),
        }),
    )

    class Meta:
        abstract = True


class EmbedPlaceCMSPlugin(EmbedMapCMSPluginBase):
    model = EmbedPlacePlugin
    name = _('Place (IFrame)')


class EmbedSearchCMSPlugin(EmbedMapCMSPluginBase):
    model = EmbedSearchPlugin
    name = _('Search (IFrame)')


class EmbedViewCMSPlugin(EmbedMapCMSPluginBase):
    model = EmbedViewPlugin
    form = EmbedViewPluginForm
    name = _('View (IFrame)')

    fieldsets = (
        (None, {
            'fields': ('center', 'zoom'),
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('map_type', 'ui_lang', 'region', ('height', 'width')),
        }),
    )


class EmbedDirectionsCMSPlugin(EmbedMapCMSPluginBase):
    model = EmbedDirectionsPlugin
    name = _('Directions (IFrame)')
    fieldsets = (
        (None, {
            'fields': ('origin', 'destination'),
        }),
        (None, {
            'fields': ('waypoints', 'travel_mode', 'avoid', 'units'),
        }),
        (_('Advanced'), {
            'classes': ('collapse',),
            'fields': ('center', 'zoom', 'map_type', 'ui_lang', 'region', ('height', 'width')),
        }),
    )


plugin_pool.register_plugin(MapCMSPlugin)
plugin_pool.register_plugin(LocationCMSPlugin)
plugin_pool.register_plugin(RouteLocationCMSPlugin)
plugin_pool.register_plugin(EmbedPlaceCMSPlugin)
plugin_pool.register_plugin(EmbedSearchCMSPlugin)
plugin_pool.register_plugin(EmbedViewCMSPlugin)
plugin_pool.register_plugin(EmbedDirectionsCMSPlugin)
