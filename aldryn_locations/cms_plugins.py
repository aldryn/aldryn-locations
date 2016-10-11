import json

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from . import models, forms


class LocationsBase(CMSPluginBase):
    module = 'Locations'


class MapCMSPlugin(LocationsBase):
    model = models.MapPlugin
    name = _('Map')
    render_template = "aldryn_locations/plugins/locations.html"
    admin_preview = True
    form = forms.MapPluginForm
    allow_children = True
    child_classes = (
        'LocationCMSPlugin',
        'RouteLocationCMSPlugin',
        'PathLocationCMSPlugin',
    )
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
        location_data = []
        path_sources = []

        request = context['request']
        base_url = '{0}://{1}'.format(
            'https' if request.is_secure() else 'http',
            request.get_host()
        )

        for child in instance.child_plugin_instances or []:
            data = child.get_location_data_for_map()
            if not data.startswith('http') and isinstance(child, models.PathLocationPlugin):
                # make url absolute (required by Google API)
                data = '{}{}'.format(base_url, data)
                path_sources.append(data)
            else:
                location_data.append(data)

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
            'path_sources': json.dumps(path_sources),
            'options': json.dumps(options),
            'map_type': json.dumps(instance.map_type),
            'route_planner': json.dumps(route_planner)
        })

        return context


class MapChildBase(LocationsBase):
    render_template = "aldryn_locations/plugins/empty.html"
    require_parent = True
    parent_classes = ['MapCMSPlugin']


class LocationCMSPlugin(MapChildBase):
    model = models.LocationPlugin
    name = _('Location')
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
    model = models.RouteLocationPlugin
    form = forms.RouteLocationPluginForm
    name = _('Route Location')


class PathLocationCMSPlugin(MapChildBase):
    model = models.PathLocationPlugin
    name = _('Location via path file')


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
    model = models.EmbedPlacePlugin
    name = _('Place (IFrame)')


class EmbedSearchCMSPlugin(EmbedMapCMSPluginBase):
    model = models.EmbedSearchPlugin
    name = _('Search (IFrame)')


class EmbedViewCMSPlugin(EmbedMapCMSPluginBase):
    model = models.EmbedViewPlugin
    form = forms.EmbedViewPluginForm
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
    model = models.EmbedDirectionsPlugin
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
plugin_pool.register_plugin(PathLocationCMSPlugin)
plugin_pool.register_plugin(EmbedPlaceCMSPlugin)
plugin_pool.register_plugin(EmbedSearchCMSPlugin)
plugin_pool.register_plugin(EmbedViewCMSPlugin)
plugin_pool.register_plugin(EmbedDirectionsCMSPlugin)
