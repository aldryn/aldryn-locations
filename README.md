Aldryn Locations
================

A Google Maps plugin for Aldryn with multiple Locations, info boxes and navigations.


Installation
------------

### Aldryn Platform Users

Choose a site you want to install the add-on to from the dashboard. Then go to ``Apps -> Install app`` and click ``Install`` next to ``Locations`` app.

Redeploy the site.

### Manual Installation

Run ``pip install aldryn-locations``.

Add ``aldryn_locations`` to ``INSTALLED_APPS`` and run ``manage.py migrate aldryn_locations``.

Plugins
-------
Aldryn Locations offers five different plugins to use. First one is the ``Map`` which works with the Google Maps JavaScript API. The other four, ``Place``, ``Directions``, ``Search`` and ``View``, are based on [Google's embed maps](https://developers.google.com/maps/documentation/embed/guide).

### Place
``Place`` mode displays a map pin at a particular place or address, such as a landmark, business, geographic feature, or town.

### Directions
``Directions`` mode displays the path between two or more specified points on the map, as well as the distance and travel time.

### Search
``Search`` mode displays results for a search across the visible map region. It's recommended that a location for the search be defined, either by including a location in the search term (record stores in Seattle) or by including a center and zoom parameter to bound the search.

### View
``View`` mode returns a map with no markers or directions baed on the search term.
