import os
import functools.partials

from fxa.__main__ import DEFAULT_CLIENT_ID
from fxa.core import Client
from fxa.tests.utils import TestEmailAccount
from fxa.tools.bearer import get_bearer_token


_FXA_SERVER = "https://api.accounts.firefox.com"
_FXA_OAUTH = "https://oauth.accounts.firefox.com/v1"
_PWD = 'MySecretPassword'


class FXATestAccount(object):
    def __init__(self, server=_FXA_SERVER, oauth=_FXA_OAUTH, password=_PWD):
        self.server = server
        self.oauth = oauth
        self.session = self.token = None
        self.password = password
        self.acct = TestEmailAccount()
        self.client = Client(_FXA_SERVER)

    def _verify(self, session, response):
        code = response["headers"].get('x-verify-code')
        if code is None:
            return False
        session.verify_email_code(code)
        return True

    def create(self):
        session = self.client.create_account(self.acct.email, self.password)
        m = self.acct.wait_for_email(functools.partial(self._verify, session))
        if m is None:
            raise RuntimeError("verification email did not arrive")

        self.token = get_bearer_token(self.acct.email, self.password
                                      account_server_url=self.server+"/v1",
                                      oauth_server_url=self.oauth,
                                      scopes=['sync:addon_storage'],
                                      client_id=DEFAULT_CLIENT_ID)

    def cleanup(self):
        self.acct.clear()
        self.client.destroy_account(self.acct.email, self.password)

    def authorization(self):
        if self.token is None:
            raise RuntimeError("You need to call create() first")
        return "Bearer %s" % self.token
