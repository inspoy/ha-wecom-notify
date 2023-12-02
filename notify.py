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
import homeassistant.helpers.config_validation as cv

from .const import (
    DOMAIN,
    CONF_API_URL,
    CONF_PUSH_KEY,
    ATTR_LINK,
)

_LOGGER = logging.getLogger(__name__)

CONFIG_SCHEMA = vol.Schema({
    vol.Required(CONF_API_URL): cv.string,
    vol.Required(CONF_PUSH_KEY): cv.string,
}, extra=vol.ALLOW_EXTRA)

def get_service(hass, config, discovery_info=None):
    """Get the notify service."""
    return WeComNotifyService(hass, config)

class WeComNotifyService(BaseNotificationService):
    """Implement the notification service for WeCom Notify."""
    def __init__(self, hass, config):
        self._hass = hass
        self._api_url = config[CONF_API_URL]
        self._push_key = config[CONF_PUSH_KEY]
        pass

    def send_message(self, message="", **kwargs):
        resp = requests.post(self._api_url, json={
            "title": kwargs.get(ATTR_TITLE) or "",
            "desc": message or "",
            "link": kwargs.get(ATTR_LINK) or "",
        }, headers={
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json",
            "Push-Key": self._push_key,
        })
        resp.json()
