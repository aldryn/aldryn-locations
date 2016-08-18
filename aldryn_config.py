from aldryn_client import forms


class Form(forms.BaseForm):
    googlemaps_marker_content_format = forms.CharField(
        'Marker content format',
        required=False,
        help_text=(
            'Example: "<strong>{content}</strong><br>{address}<br>{zipcode} '
            '{city}". All available variables: content, address, zipcode, '
            'city, lat, lng'
        )
    )

    def to_settings(self, data, settings):
        from functools import partial
        from aldryn_addons.utils import djsenv
        env = partial(djsenv, settings=settings)

        settings['ALDRYN_LOCATIONS_MARKER_CONTENT_FORMAT'] = data['googlemaps_marker_content_format']
        settings['ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY'] = env('ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY')
        return settings
