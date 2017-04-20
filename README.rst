Mozlotov
========

Mozilla-specific helpers for writing Molotov tests.


FXA
---

In order to use an API that requires a Firefox Account Bearer token,
you can use the **FXATestAccount** class. The class will create
a test user for you and provide a Bearer token.

Example of Molotov integration:

.. code-block:: python

    from molotov import global_setup, global_teardown setup
    from mozlotov import FXATestAccount

    _FXA = []

    @global_setup()
    def create_accoun(args):
        # creates the user and get a Bearer token
        acct = FXATestAccount()
        acct.create()
        _FXA.append(acct)

    @global_teardown()
    def destroy_account():
        # destroys the user
        _FXA[0].cleanup()

    @setup()
    async def init_test(worker_id, args):
        # grab the Bearer token for the Molotov test
        headers = {"Authorization": _FXA[0].authorization()}
        return {'headers': headers}

