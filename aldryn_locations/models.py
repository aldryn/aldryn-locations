from django.db import models
from django.http import QueryDict
from django.template.defaultfilters import urlencode
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.core.urlresolvers import reverse

from cms.models import CMSPlugin, Site
from cms.utils.i18n import get_current_language
from cms.utils.compat.dj import python_2_unicode_compatible

from filer.fields.file import FilerFileField


GOOGLE_MAPS_API_KEY = settings.ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY
GOOGLE_MAPS_STATICMAPS_URL = getattr(
    settings,
    'ALDRYN_LOCATIONS_GOOGLEMAPS_STATICMAPS_URL',
    'https://maps.googleapis.com/maps/api/staticmap',
)
MARKER_CONTENT_FORMAT = unicode(settings.ALDRYN_LOCATIONS_MARKER_CONTENT_FORMAT)
ZOOM_LEVELS = [(str(level), str(level)) for level in range(22)]

ROADMAP = 'roadmap'
SATELLITE = 'satellite'
HYBRID = 'hybrid'
TERRAIN = 'terrain'

MAP_CHOICES = [
    (ROADMAP, _('Roadmap')),
    (SATELLITE, _('Satellite')),
]

EXTENDED_MAP_CHOICES = MAP_CHOICES + [
    (HYBRID, _('Hybrid')),
    (TERRAIN, _('Terrain')),
]


@python_2_unicode_compatible
class MapPlugin(CMSPlugin):
    title = models.CharField(_("map title"), max_length=255, blank=True,
                             null=True)

    zoom = models.CharField(
        _('Zoom level'), choices=ZOOM_LEVELS, blank=True, null=True,
        help_text=_('Leave empty for auto zoom'), max_length=20)

    route_planner_title = models.CharField(
        _('Route Planner Title'), max_length=255, blank=True, null=True,
        default=_('Calculate your fastest way to here'))

    width = models.CharField(
        _('width'), max_length=255, default='100%',
        help_text=_('Plugin width (in pixels or percent).'))

    height = models.CharField(
        _('height'), max_length=255, default='400px',
        help_text=_('Plugin height (in pixels).'))

    scrollwheel = models.BooleanField(
        _('Enable scrollwheel zooming on the map'), default=True)

    double_click_zoom = models.BooleanField(
        _('Enable double click to zoom'), default=True)

    draggable = models.BooleanField(_('Allow map dragging'), default=True)

    keyboard_shortcuts = models.BooleanField(
        _('Enable keyboard shortcuts'), default=True)

    pan_control = models.BooleanField(_('Show pan control'), default=True)

    zoom_control = models.BooleanField(_('Show zoom control'), default=True)

    street_view_control = models.BooleanField(
        _('Show Street View control'), default=True)

    map_type = models.CharField(_('Map Type'), max_length=255, choices=EXTENDED_MAP_CHOICES, default=ROADMAP)

    def __str__(self):
        ret = ''

        if self.child_plugin_instances:
            locs = sum(not x.route_planner for x in self.child_plugin_instances)
            routes = sum(x.route_planner for x in self.child_plugin_instances)

            _loc = _('Locations') if locs > 1 else _('Location')
            _route = _('Routes') if routes > 1 else _('Route')

            if locs and routes:
                ret = u'%i %s & %i %s' % (locs, _loc, routes, _route)

            elif locs:
                ret = u'%i %s' % (locs, _loc)

            elif routes:
                ret = u'%i %s' % (routes, _route)

        else:
            ret = _(u'Empty: please add at least one location or route')

        if self.title:
            return u'%s (%s)' % (self.title, ret)

        return u'%s' % ret

    @property
    def staticmap_url(self):
        if not self.child_plugin_instances:
            return None

        def clean_size(size):
            if size.endswith('px'):
                return int(size.replace('px', ''))
            return 1000  # default

        qdict = QueryDict('', mutable=True)
        qdict.update({
            'key': GOOGLE_MAPS_API_KEY,
            'size': '{}x{}'.format(
                clean_size(self.width),
                clean_size(self.height)
            ),
            'maptype': self.map_type,
            'language': get_current_language()
        })

        if self.zoom:
            qdict['zoom'] = self.zoom

        query = qdict.urlencode()

        for location in self.child_plugin_instances or []:
            lat_lng = location.get_lat_lng()
            location = (
                ','.join(lat_lng) if lat_lng else
                ' '.join((location.address, location.zipcode, location.city))
            )
            query += '&markers={}'.format(urlencode(location))

        return '{}?{}'.format(GOOGLE_MAPS_STATICMAPS_URL, query)

    def get_route_planner(self):
        for location in self.child_plugin_instances or []:
            if location.route_planner:
                return location.address, location.zipcode, location.city
        return False


@python_2_unicode_compatible
class LocationPlugin(CMSPlugin):
    route_planner = False

    address = models.CharField(_("address"), max_length=255)
    zipcode = models.CharField(_("zip code"), max_length=30)
    city = models.CharField(_("city"), max_length=255)

    content = models.CharField(
        _('Content'), max_length=255, blank=True,
        help_text=_('Displayed in a info window above location marker')
    )

    lat = models.FloatField(
        _('latitude'), null=True, blank=True,
        help_text=_('Use latitude & longitude to fine tune the map position.'))

    lng = models.FloatField(
        _('longitude'), null=True, blank=True)

    def __str__(self):
        return u'%s, %s %s' % (self.address, self.zipcode, self.city)

    def get_content(self):
        if not self.content:
            return None

        fmt = MARKER_CONTENT_FORMAT

        if not fmt:
            return self.content

        return fmt.format(
            content=self.content,
            address=self.address,
            zipcode=self.zipcode,
            city=self.city,
            lat=self.lat,
            lng=self.lng,
        )

    def get_lat_lng(self):
        if self.lat and self.lng:
            return self.lat, self.lng

    def get_location_data_for_map(self):
        return {
            'address': '{}, {} {}'.format(self.address, self.zipcode, self.city),
            'latlng': self.get_lat_lng(),
            'content': self.get_content(),
            'admin': reverse('admin:cms_page_edit_plugin', args=[self.pk]),
        }


class RouteLocationPlugin(LocationPlugin):
    route_planner = True


class PathLocationPlugin(CMSPlugin):
    route_planner = False

    path_file = FilerFileField(
        verbose_name=_('Path File (e.g. KML)'),
        related_name='+',
    )

    def copy_relations(self, oldinstance):
        self.path_file = oldinstance.path_file

    def __unicode__(self):
        if self.path_file:
            return self.path_file.name
        return self.pk

    def get_location_data_for_map(self):
        if self.path_file:
            return self.path_file.url


# 'New Maps' embed plugins (IFrame)
# https://developers.google.com/maps/documentation/embed/guide


class EmbedPlugin(CMSPlugin):
    query = models.CharField(
        _('Query'), max_length=255, help_text=_('defines the place to highlight on the map. It accepts a location '
                                                'as either a place name or address'))

    map_type = models.CharField(_('Map Type'), max_length=255, choices=MAP_CHOICES, default=ROADMAP)

    center = models.CharField(
        _('Center of the map (latitude + longitude)'), null=True, blank=True, max_length=255,
        help_text=_('optionally define the center of the map view. It accepts a comma-separated latitude and longitude '
                    'value (such as 37.4218,-122.0840).'))

    zoom = models.CharField(
        _('Zoom level'), choices=ZOOM_LEVELS, blank=True, null=True, max_length=2,
        help_text=_('0 (the whole world) to 21 (individual buildings). Leave empty for auto zoom'))

    ui_lang = models.CharField(
        _('language for ui elements'), max_length=10, null=True, blank=True, help_text=_('default to page language'))

    region = models.CharField(
        _('map region (ccTLD)'), max_length=10, null=True, blank=True,
        help_text=_(' defines the appropriate borders and labels to display, based on geo-political sensitivities. '
                    'Accepts a region code specified as a two-character ccTLD (top-level domain) value.'))

    width = models.CharField(
        _('width'), max_length=255, default='100%',
        help_text=_('Plugin width (in pixels or percent).'))

    height = models.CharField(
        _('height'), max_length=255, default='400px',
        help_text=_('Plugin height (in pixels).'))

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.query or self.center

    def get_query(self):
        return urlencode(self.query) if self.query else None

    def get_center(self):
        return self.center.replace(' ', '')

    def get_url(self):
        key = getattr(settings, 'ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY', '')
        url = 'https://www.google.com/maps/embed/v1/%(mode)s?key=%(key)s&maptype=%(map_type)s' % {
            'mode': self.mode, 'key': key, 'map_type': self.map_type
        }

        if self.query:
            url += '&q=%s' % self.get_query()

        if self.center:
            url += '&center=%s' % self.get_center()

        if self.zoom:
            url += '&zoom=%s' % self.zoom

        if self.ui_lang:
            url += '&language=%s' % self.ui_lang

        if self.region:
            url += '&region=%s' % self.region

        return url


class EmbedPlacePlugin(EmbedPlugin):
    """
    Required fields: query
    """

    mode = 'place'


class EmbedSearchPlugin(EmbedPlugin):
    """
    Required fields: query
    """

    mode = 'search'


class EmbedViewPlugin(EmbedPlugin):
    """
    Required fields: center
    """

    mode = 'view'
    query = None


class EmbedDirectionsPlugin(EmbedPlugin):
    AUTO = ('auto', _('Automatic'))

    DRIVING = 'driving'
    WALKING = 'walking'
    BICYCLING = 'bicycling'
    TRANSIT = 'transit'
    FLYING = 'flying'

    TRAVEL_MODES = [
        (DRIVING, _('Driving')),
        (WALKING, _('Walking')),
        (BICYCLING, _('Bicycling')),
        (TRANSIT, _('Transit')),
        (FLYING, _('Flying')),
    ]

    TOLLS = 'tolls'
    HIGHWAYS = 'highways'
    FERRIES = 'ferries'

    AVOID_CHOICES = (
        ('%s' % TOLLS, _('Tolls')),
        ('%s' % HIGHWAYS, _('Highways')),
        ('%s' % FERRIES, _('Ferries')),

        ('%s|%s' % (TOLLS, HIGHWAYS), _('Tolls & Highways')),
        ('%s|%s' % (TOLLS, FERRIES), _('Tolls & Ferries')),
        ('%s|%s' % (FERRIES, HIGHWAYS), _('Ferries & Highways')),

        ('%s|%s|%s' % (TOLLS, FERRIES, HIGHWAYS), _('Tolls, Ferries & Highways')),
    )

    UNITS_CHOICES = [
        ('metric', _('Metric')),
        ('imperial', _('Imperial')),
    ]

    mode = 'directions'

    query = None

    origin = models.CharField(
        _('origin'), max_length=255,
        help_text=_('defines the origin and accepts a location as either a place name or address'))

    destination = models.CharField(
        _('destination'), max_length=255,
        help_text=_('defines the destination and accepts a location as either a place name or address'))

    waypoints = models.CharField(
        _('list of waypoints'), max_length=255, null=True, blank=True,
        help_text=_('separated by the pipe character (|) (e.g. Berlin,Germany|Paris,France)'))

    travel_mode = models.CharField(_('travel mode'), max_length=50, default=AUTO[0], choices=[AUTO] + TRAVEL_MODES)
    avoid = models.CharField(_('avoid certain means'), max_length=50, null=True, blank=True, choices=AVOID_CHOICES)
    units = models.CharField(
        _('units for distances in results'), max_length=10, default=AUTO[0], choices=[AUTO] + UNITS_CHOICES)

    def __unicode__(self):
        ret = self.origin
        if self.waypoints:
            ret += ' -> %s' % ' -> '.join(self.waypoints.split('|'))
        ret += ' -> %s' % self.destination
        return ret

    def get_origin(self):
        return urlencode(self.origin)

    def get_destination(self):
        return urlencode(self.destination)

    def get_waypoints(self):
        return urlencode(self.waypoints)

    def get_travel_mode(self):
        # If set to auto we let Google decide
        return self.travel_mode if self.travel_mode != self.AUTO[0] else None

    def get_units(self):
        # If set to auto we let Google decide
        return self.units if self.units != self.AUTO[0] else None

    def get_url(self):
        url = super(EmbedDirectionsPlugin, self).get_url()
        url += '&origin=%(origin)s&destination=%(destination)s' % {
            'origin': self.get_origin(), 'destination': self.get_destination()}

        if self.waypoints:
            url += '&waypoints=%s' % self.get_waypoints()

        if self.get_travel_mode():
            url += '&mode=%s' % self.get_travel_mode()

        if self.avoid:
            url += '&avoid=%s' % self.avoid

        if self.get_units():
            url += '&units=%s' % self.get_units()

        return url
