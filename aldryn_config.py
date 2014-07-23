from aldryn_client import forms


class Form(forms.BaseForm):
    googlemaps_apikey = forms.CharField('Google Maps API Key', required=False)

    def to_settings(self, data, settings):
        settings['ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY'] = data['googlemaps_apikey']
        return settings
