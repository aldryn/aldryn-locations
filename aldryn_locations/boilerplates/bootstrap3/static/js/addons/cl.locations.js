/*!
 * @author      Angelo Dini - github.com/finalangel/classjs-plugins
 * @copyright   Distributed under the BSD License.
 * @version     3.1.0
 */

// ensure namespace is defined
var Cl = window.Cl || {};

(function ($) {
    'use strict';

    // creating class
    Cl.Locations = new Class({

        options: {
            'edit_mode': false,
            'mapType': '',
            'mapTypeControlOptions': google.maps.MapTypeControlStyle.DROPDOWN_MENU,
            'markers': [],
            'markerAnimation': google.maps.Animation.DROP,
            'routePlanner': false,
            'settings': {},
            'zoom': 12,
            'zoomControlOptions': google.maps.ZoomControlStyle.SMALL,
            'cls': {
                'mapContainer': '.aldryn-locations-container',
                'formContainer': '.aldryn-locations-form',
                'formOutput': '.aldryn-locations-form-output'
            }
        },

        initialize: function (container, options) {
            this.container = $(container);
            this.options = $.extend(true, {}, this.options, options);
            this.settings = this.options.settings;
            this.markers = [];
            this.bounds = new google.maps.LatLngBounds();
            this.form = this.container.find(this.options.cls.formContainer);

            // presets
            this.mapTypes = {
                'hybrid': google.maps.MapTypeId.HYBRID,
                'roadmap': google.maps.MapTypeId.ROADMAP,
                'satellite': google.maps.MapTypeId.SATELLITE,
                'terrain': google.maps.MapTypeId.TERRAIN
            };

            // move to setup
            this._setup();
        },

        _setup: function () {
            // extend google map settings
            this.settings.mapTypeId = this.mapTypes[this.options.mapType];
            this.settings.zoomControlOptions = { 'style': this.options.zoomControlOptions };
            this.settings.mapTypeControlOptions = { 'style': this.options.mapTypeControlOptions };

            // setting up map
            this.mapContainer = this.container.find(this.options.cls.mapContainer)[0];
            this.map = new google.maps.Map(this.mapContainer, this.settings);

            // add all markers
            this.addMarkers(this.options.markers);

            // enable routing
            this._routePlanner();
        },

        /**
         * Adds a collection of markers to the google map instance
         *
         * @param markers {Object[]} exptects a collection of markers (see addMarker())
         */
        addMarkers: function (markers) {
            var that = this;

            // geocoder helper
            function geocode(marker) {
                var geocoder = new google.maps.Geocoder();
                geocoder.geocode({'address': marker.address}, function (results, status) {
                    if (status === google.maps.GeocoderStatus.OK) {
                        marker.latlng = results[0].geometry.location;
                        that.addMarker(marker);
                    }
                });
            }

            // loop through all given markers
            for (var i = 0; i < markers.length; i++) {
                var marker = markers[i];

                //  check if we need to calculate the latlng or continue
                if (marker.latlng === null) {
                    geocode(marker);
                } else {
                    marker.latlng = new google.maps.LatLng(marker.latlng);
                    this.addMarker(marker);
                }
            }
        },

        /**
         * adds a single marker to the google map instance
         *
         * @param marker {Object} marker object
         * @param marker.address {String} expects a valid address
         * @param marker.admin {String} admin link for editing within the cms
         * @param [marker.content] {String} content for the markerInfoWindow
         * @param [marker.latlng] {Number} expects valid lat and lng values
         */
        addMarker: function (marker) {
            var that = this;

            // Creates a marker on the map, calls fitMap afterwards
            marker = new google.maps.Marker({
                'map': this.map,
                'admin': marker.admin,
                'position': marker.latlng,
                'title': marker.title,
                'content': marker.content
            });

            // attach info window
            if (marker.content) {
                var infoWindow = new google.maps.InfoWindow({
                    'disableAutoPan': true,
                    // to false and InfoWindow is out of bounds
                    'content': marker.content
                });

                google.maps.event.addListener(marker, 'click', function () {
                    infoWindow.open(that.map, marker);
                    marker.setAnimation(google.maps.Animation.BOUNCE);
                    setTimeout(function () { marker.setAnimation(null); }, 750);
                });

                setTimeout(function () {
                    infoWindow.open(that.map, marker);
                }, 500);
            }

            // add admin edit capabilities for markers
            if (this.options.edit && window.CMS) {
                google.maps.event.addListener(marker, 'dblclick', function () {
                    var modal = new CMS.Modal();
                    modal.open(
                        url: marker.admin
                    );
                });
            }

            // update markers and map position
            this.markers.push(marker);
            this.bounds.extend(marker.position);
            this.map.fitBounds(this.bounds);
            this.map.panBy(0, -50);

            // reassign zoom level
            var listener = google.maps.event.addListener(that.map, 'idle', function () {
                if (that.map.getZoom() > that.options.zoom) { that.map.setZoom(that.options.zoom); }
                google.maps.event.removeListener(listener);
            });
        },

        _routePlanner: function () {
            var that = this;
            var mode = '';
            var destination = this.form.find('input[type="hidden"]').val();
            var routers = this.container.find('span[data-type]');
            var directionsService = new google.maps.DirectionsService();
            var directionsDisplay = new google.maps.DirectionsRenderer();
            directionsDisplay.setMap(this.map);
            directionsDisplay.setPanel(this.container.find(this.options.cls.formOutput)[0]);

            function getRoute() {
                var origin = that.form.find('input[type="text"]').val();

                // hide streetview
                that.map.getStreetView().setVisible(false);

                var request = {
                    'origin': origin,
                    'destination': destination,
                    'travelMode': google.maps.TravelMode[mode.toUpperCase()]
                };

                directionsService.route(request, function (result, status) {
                    if (status === google.maps.DirectionsStatus.OK) {
                        directionsDisplay.setMap(that.map);
                        directionsDisplay.setDirections(result);
                        that.form.find('.form-group').removeClass('has-error');
                    } else {
                        that.form.find('.form-group').addClass('has-error');
                    }
                });
            }

            // attach routes handling
            routers.on('click', function () {
                routers.removeClass('active');
                $(this).addClass('active');
                mode = $(this).data('type');
            }).eq(0).trigger('click');

            // prevent form submission
            this.form.on('submit', function (e) {
                e.preventDefault();
                getRoute();
            });
        }

    });

})(jQuery);
