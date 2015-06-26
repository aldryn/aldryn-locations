Aldryn Locations
================

Aldryn Locations is the easiest way to integrate Google Maps into `Aldryn <http://aldryn.com>`_ and `django CMS
<http://django-cms>`_ sites via Google's API.

It's fully featured, and includes several plugins to provide support for:

* multiple locations
* location information
* routes and directions
* searching


Aldryn Platform Users
---------------------

Choose a site you want to install the add-on to from the dashboard. Then go to ``Apps -> Install app`` and click
``Install`` next to ``Locations`` app.

Redeploy the site.

Manual Installation
-------------------

::

    pip install aldryn-locations

Add ``aldryn_locations`` to ``INSTALLED_APPS`` and run ``manage.py migrate aldryn_locations``.

Add ``ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY`` to your ``settings.py`` using the provided key from google

Configure ``aldryn-boilerplates`` (https://pypi.python.org/pypi/aldryn-boilerplates/).

To use the old templates, set ``ALDRYN_BOILERPLATE_NAME='legacy'``.
To use https://github.com/aldryn/aldryn-boilerplate-standard (recommended, will be renamed to
``aldryn-boilerplate-bootstrap3``) set ``ALDRYN_BOILERPLATE_NAME='bootstrap3'``.


Plugins
-------
Aldryn Locations offers five different plugins to use. First one is the ``Map`` which works with the Google Maps JavaScript API. The other four, ``Place``, ``Directions``, ``Search`` and ``View``, are based on [Google's embed maps](https://developers.google.com/maps/documentation/embed/guide).

* Place
  ``Place`` mode displays a map pin at a particular place or address, such as a landmark, business, geographic feature, or town.

* Directions
  ``Directions`` mode displays the path between two or more specified points on the map, as well as the distance and travel time.

* Search
  ``Search`` mode displays results for a search across the visible map region. It's recommended that a location for the search be defined, either by including a location in the search term (record stores in Seattle) or by including a center and zoom parameter to bound the search.

* View
  ``View`` mode returns a map with no markers or directions baed on the search term.
