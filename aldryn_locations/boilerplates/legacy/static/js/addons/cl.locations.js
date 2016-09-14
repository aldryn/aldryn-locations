/*!
 * @author      Angelo Dini - github.com/finalangel/classjs-plugins
 * @copyright   Distributed under the BSD License.
 * @version     3.0.0
 */

// ensure namespace is defined
var Cl = window.Cl || {};

(function($){
    'use strict';

    // creating class
    Cl.Locations = new Class({

        options: {
            'markers': [],
            'settings': {},
            'mapType': '',
            'route_planner': false,
            'zoom': 12,
            'edit_mode': false,
            'zoomControlOptions': google.maps.ZoomControlStyle.SMALL,
            'mapTypeControlOptions': google.maps.MapTypeControlStyle.DROPDOWN_MENU,
            'markerAnimation': google.maps.Animation.DROP
        },

        initialize: function (container, options) {
            this.container = $(container);
            this.options = $.extend(true, {}, this.options, options);
            this.settings = this.options.settings;
            this.markers = [];
            this.bounds = new google.maps.LatLngBounds();
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
            this.mapContainer = this.container.find('.google-map-container')[0];
            this.map = new google.maps.Map(this.mapContainer, this.settings);

            // add all markers
            this.addMarkers();
            this.addLayers(this.options.layerSources);

            // enable routing
            this.routePlanner();
        },

        addMarkers: function () {
            var that = this;

            // loop through all given markers
            for (var i = 0; i < this.options.markers.length; i++) {
                var marker = this.options.markers[i];

                //  check if we need to calculate the latlng or continue
                if(marker.latlng === null) {
                    // figure out latlng from the address
                    (function (marker) {
                        var geocoder = new google.maps.Geocoder();
                        geocoder.geocode({'address': marker.address}, function (results, status) {
                            if (status === google.maps.GeocoderStatus.OK) {
                                marker.latlng = results[0].geometry.location;
                                that.addMarker(marker);
                            }
                        });
                    })(marker);

                } else {
                    marker.latlng = new google.maps.LatLng(marker.latlng);
                    this.addMarker(marker);
                }
            }
        },

        /**
         * Adds KLM layers
         *
         * @param {String[]} layerSources
         */
        addLayers: function (layerSources) {
            if (!layerSources || !layerSources.length) {
                return;
            }

            var that = this;

            layerSources.forEach(function (src) {
                new google.maps.KmlLayer(src, {
                    suppressInfoWindows: true,
                    preserveViewport: false,
                    map: that.map
                });
            });
        },

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
            if(marker.content) {
                var infoWindow = new google.maps.InfoWindow({
                    'disableAutoPan': true,
                    // to false and InfoWindow is out of bounds
                    'content': marker.content
                });

                google.maps.event.addListener(marker, 'click', function() {
                    infoWindow.open(that.map, marker);
                    marker.setAnimation(google.maps.Animation.BOUNCE);
                    setTimeout(function() { marker.setAnimation(null)}, 750);
                });

                setTimeout(function () {
                    infoWindow.open(that.map, marker);
                }, 500);
            }

            // add admin edit capabilities for markers
            if(this.options.edit && window.CMS) {
                google.maps.event.addListener(marker, 'dblclick', function() {
                    var modal = new CMS.Modal();
                    modal.open(marker.admin, 'Location');
                });
            }

            // update markers and map position
            this.markers.push(marker);
            this.bounds.extend(marker.position);
            this.map.fitBounds(this.bounds);
            this.map.panBy(0, -50);

            // reassign zoom level
            var listener = google.maps.event.addListener(that.map, 'idle', function() {
                if(that.map.getZoom() > that.options.zoom) that.map.setZoom(that.options.zoom);
                google.maps.event.removeListener(listener);
            });
        },

        routePlanner: function () {
            var that = this;
            var mode = '';
            var destination = this.container.find('.google-map-destinations input').val();
            var routers = this.container.find('span[data-type]');
            var directionsService = new google.maps.DirectionsService();
            var directionsDisplay = new google.maps.DirectionsRenderer();
                directionsDisplay.setMap(this.map);
                directionsDisplay.setPanel(this.container.find('.google-map-panel')[0]);

            function getRoute() {
                var origin = that.container.find('.google-map-route .input-text').val();
                // cancel if destination is empty
                if(origin === '') return false;
                // hide streetview
                that.map.getStreetView().setVisible(false);

                var request = {
                    'origin': origin,
                    'destination': destination,
                    'travelMode': google.maps.TravelMode[mode.toUpperCase()]
                };

                directionsService.route(request, function(result, status) {
                    if (status == google.maps.DirectionsStatus.OK) {
                        directionsDisplay.setMap(that.map);
                        directionsDisplay.setDirections(result);
                        that.container.find('form').removeClass('form-error');
                    } else {
                        that.container.find('form').addClass('form-error');
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
            this.container.find('form').on('submit', function(e) {
                e.preventDefault();
                getRoute();
            });
        }

    });

})(jQuery);
