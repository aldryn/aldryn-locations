from aldryn_client import forms


class Form(forms.BaseForm):
    def to_settings(self, data, settings):
        from functools import partial
        from aldryn_addons.utils import djsenv
        env = partial(djsenv, settings=settings)

        settings['ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY'] = env('ALDRYN_LOCATIONS_GOOGLEMAPS_APIKEY')
        return settings
