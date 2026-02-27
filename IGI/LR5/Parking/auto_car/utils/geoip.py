import geoip2.database
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import os

def get_timezone_by_ip(ip_address):
    try:
        geoip_db_path = os.path.join(settings.GEOIP_PATH, settings.GEOIP_CITY)
        # print(geoip_db_path)
        with geoip2.database.Reader(geoip_db_path) as reader:
            response = reader.city(ip_address)
            return response.location.time_zone
    except (geoip2.errors.AddressNotFoundError, FileNotFoundError):
        return settings.TIME_ZONE