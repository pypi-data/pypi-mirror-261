import json
import logging

from aurorastack.core import cache, config
from aurorastack.core.connector.aurora_connector import AuroraConnector
from aurorastack.core.auth.jwt import JWTAuthenticator, JWTUtil
from aurorastack.core.transaction import get_transaction
from aurorastack.core.handler import BaseAuthenticationHandler
from aurorastack.core.error import ERROR_AUTHENTICATE_FAILURE

_LOGGER = logging.getLogger(__name__)


class EventHandler(BaseAuthenticationHandler):
    def __init__(self, handler_config):
        super().__init__(handler_config)
        self._initialize()

    def _initialize(self) -> None:
        self.event_conn: RestConnector = RestConnector()

    def notify(self, status: str, message: dict) -> None:
        token = self._get_token()
        tenant_id = self._extract_tenant_id(token)
        # Send Msg

    @staticmethod
    def _get_token() -> str:
        transaction = get_transaction()
        token = transaction.meta.get("token")
        if not isinstance(token, str) or len(token) == 0:
            raise ERROR_AUTHENTICATE_FAILURE(message="empty token provided.")

        return token

    @staticmethod
    def _extract_tenant_id(token):
        try:
            decoded = JWTUtil.unverified_decode(token)
        except Exception:
            _LOGGER.debug(f"[_extract_tenant_id] failed to decode token: {token[:10]}")
            raise ERROR_AUTHENTICATE_FAILURE(message="failed to decode token.")

        if tenant_id := decoded.get("did"):
            return tenant_id
        else:
            raise ERROR_AUTHENTICATE_FAILURE(message="empty tenant_id provided.")


