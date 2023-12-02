import logging
import requests
import json
import voluptuous as vol

from homeassistant.components.notify import (
    ATTR_MESSAGE,
    ATTR_TITLE,
    ATTR_DATA,
    ATTR_TARGET,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)

_LOGGER = logging.getLogger(__name__)

def get_service(hass, config, discovery_info=None):
    """Get the notify service."""
    return WeComNotifyService(hass, config)

class WeComNotifyService(BaseNotificationService):
    def __init__(self, hass, config):
        pass

    def send_message(self, message="", **kwargs):
        pass
