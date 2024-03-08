import asyncio
from flet import Page, View, ControlEvent
from typing import Any, Dict
from flet_easy.extras_jwt import (
    encode_verified,
    SecretKey,
    _decode_payload_async,
    _decode_payload,
)
from flet_easy.extras import Msg
from datetime import timedelta
from flet_easy.inheritance import (
    SessionStorageEdit,
    Keyboardsy,
    Resizesy,
)

from schedule import CancelJob, every, repeat, run_pending
from datetime import datetime, timezone


class Datasy:
    """
    The decorated function will always receive a parameter which is `data` (can be any name), which will make an object of type `Datasy` of `Flet-Easy`.

    This class has the following attributes, in order to access its data:

    * `page` : We get the values of the page provided by `Flet` (https://flet.dev/docs/controls/page) .
    * `url_params` : We obtain a dictionary with the values passed through the url.
    * `view` : Get a `View` object from `Flet` (https://flet.dev/docs/controls/view), previously configured with the `view` decorator of `Flet-Easy`.
    * `route_prefix` : Value entered in the `FletEasy` class parameters to create the app object.
    * `route_init` : Value entered in the `FletEasy` class parameters to create the app object.
    * `route_login` : Value entered in the `FletEasy` class parameters to create the app object.
    ---
    * `share` : It is used to be able to store and to obtain values in the client session, the utility is to be able to have greater control in the pages in which it is wanted to share and not in all the pages, for it the `share_data` parameter of the `page` decorator must be used. The methods to use are similar `page.session` (https://flet.dev/docs/guides/python/session-storage).

    Besides that you get some extra methods:

        * `contains` : Returns a boolean, it is useful to know if there is shared data.
        * `get_values` : Get a list of all shared values.
        * `get_all` : Get the dictionary of all shared values.
    ----
    * `on_keyboard_event` : get event values to use in the page.
    * `on_resize` : get event values to use in the page.
    * `logout and logout_async` : method to close sessions of all sections in the browser (client storage), requires as parameter the key or the control (the parameter key of the control must have the value to delete), this is to avoid creating an extra function.
    * `login and login_async` : method to create sessions of all sections in the browser (client storage), requires as parameters the key and the value, the same used in the `page.client_storage.set` method.
    * `go and go_async` : Method to change the path of the application, in order to reduce the code, you must assign the value of the `key` parameter of the `control` used, for example buttons.
    """

    def __init__(
        self,
        page: str,
        route_prefix: str = None,
        route_init: str = None,
        route_login: str = None,
        secret_key: str = None,
        auto_logout: bool = False,
    ) -> None:
        self.__page: Page = page
        self.__url_params: dict = None
        self.__view: View = None
        self.__route_prefix: str = route_prefix
        self.__route_init: str = route_init
        self.__route_login: str = route_login
        self.__share = SessionStorageEdit(self.__page)
        self.__on_keyboard_event: Keyboardsy = None
        self.__on_resize: Resizesy = None
        self._login_done: bool = False
        self.__secret_key: SecretKey = secret_key
        self.__key_login: str = None
        self.__auto_logout: bool = auto_logout

    @property
    def key_login(self):
        return self.__key_login

    @property
    def auto_logout(self):
        return self.__auto_logout

    @property
    def secret_key(self):
        return self.__secret_key

    @property
    def page(self):
        return self.__page

    @page.setter
    def page(self, page: object):
        self.__page = page

    @property
    def url_params(self):
        return self.__url_params

    @url_params.setter
    def url_params(self, url_params: dict):
        self.__url_params = url_params

    @property
    def view(self):
        return self.__view

    @view.setter
    def view(self, view: View):
        self.__view = view

    @property
    def route_prefix(self):
        return self.__route_prefix

    @route_prefix.setter
    def route_prefix(self, route_prefix: str):
        self.__route_prefix = route_prefix

    @property
    def route_init(self):
        return self.__route_init

    @route_init.setter
    def route_init(self, route_init: str):
        self.__route_init = route_init

    @property
    def route_login(self):
        return self.__route_login

    @route_login.setter
    def route_login(self, route_login: str):
        self.__route_login = route_login

    @property
    def share(self):
        return self.__share

    # events
    @property
    def on_keyboard_event(self):
        return self.__on_keyboard_event

    @on_keyboard_event.setter
    def on_keyboard_event(self, on_keyboard_event: object):
        self.__on_keyboard_event = on_keyboard_event

    @property
    def on_resize(self):
        return self.__on_resize

    @on_resize.setter
    def on_resize(self, on_resize: object):
        self.__on_resize = on_resize

    def _create_task_login_update(self, decode: Dict[str, Any]):
        """Updates the login status, in case it does not exist it creates a new task that checks the user's login status."""
        time_exp = datetime.utcfromtimestamp(int(decode.get("exp"))).replace(
            tzinfo=timezone.utc
        )
        time_now = datetime.now(tz=timezone.utc)
        time_res = time_exp - time_now
        self._login_done = True

        @repeat(every(int(time_res.total_seconds())).seconds, self.key_login)
        def job(key_login: str):
            asyncio.create_task(self.logout_async(key_login))
            return CancelJob

        async def run_task_login(data):
            while data._login_done:
                run_pending()
                print("Running task login Update")
                await asyncio.sleep(1)

        asyncio.create_task(run_task_login(self))

    """ login authentication | ASYNC"""

    async def _create_login_async(self):
        """Create the pubsub connection when starting the app."""
        await self.page.pubsub.subscribe_topic_async(
            self.page.client_ip, self.__logout_init_async
        )

    async def _logout_sessions_async(self, key: str) -> None:
        """Closes sections of browser tabs or sessions of the same user when the jwt expires or an error occurs in the decode."""
        await self.page.pubsub.send_all_on_topic_async(
            self.page.client_ip, Msg("logout", key)
        )

    async def logout_async(self, e: ControlEvent | str):
        """Closes sections of the browser tabs or sessions of the same user, deletes the login key of the
        client_storage.
        """
        if isinstance(e, str):
            key = e
        else:
            key = e.control.key
        await self.page.pubsub.send_all_on_topic_async(
            self.page.client_ip, Msg("logout", key)
        )

    async def __logout_init_async(self, topic, msg: Msg):
        """It is executed when messages are received via pubsub."""
        try:
            if msg.method == "login":
                await self.page.client_storage.set_async(msg.key, msg.value)

            elif msg.method == "logout":
                await self.page.client_storage.remove_async(msg.key)
                self._login_done = False
                await self.page.go_async(self.route_login)

            elif msg.method == "updateLogin":
                print("updateLogin:", self.page.session_id, "value:", msg.value)
                self._login_done = msg.value

            elif msg.method == "updateLoginSessions":
                if not msg.value:
                    self._create_task_login_update(
                        decode=await _decode_payload_async(
                            self.page,
                            self.key_login,
                            self.secret_key.secret
                            if self.secret_key.secret is not None
                            else self.secret_key.pem_key.public,
                        )
                    )

        except Exception:
            pass

    def _create_tasks(self, time_expiry: timedelta, key: str) -> None:
        """Creates the logout task when logging in."""
        if time_expiry is not None:

            @repeat(every(int(time_expiry.total_seconds())).seconds, self, key)
            def job(self: object, key: str):
                asyncio.create_task(self.logout_async(key))
                return CancelJob

            async def run_task_login(self):
                while self._login_done:
                    run_pending()
                    print("running task login initalization")
                    await asyncio.sleep(1)

            asyncio.create_task(run_task_login(self))

    async def login_async(
        self,
        key: str,
        value: Dict[str, Any],
        time_expiry: timedelta = None,
        next_route: str = None,
    ):
        """Creates the user login. | Registering in the client's storage the key and value in all browser sessions."""
        self.__key_login = key
        value = encode_verified(self.secret_key, value, time_expiry)
        self._login_done = True

        if self.__auto_logout:
            self._create_tasks(time_expiry, key)

        await self.page.client_storage.set_async(key, value)
        await self.page.pubsub.send_others_on_topic_async(
            self.page.client_ip, Msg("login", key, value)
        )

        if next_route is not None:
            await self.page.go_async(next_route)

    """ login authentication"""

    def _create_login(self):
        """Create the pubsub connection when starting the app."""
        self.page.pubsub.subscribe_topic(self.page.client_ip, self.__logout_init)

    def _logout_sessions(self, key: str) -> None:
        """Closes sections of browser tabs or sessions of the same user when the jwt expires or an error occurs in the decode."""
        self.page.pubsub.send_all_on_topic(self.page.client_ip, Msg("logout", key))

    def logout(self, key_login: str | ControlEvent):
        """Closes sections of the browser tabs or sessions of the same user, deletes the login key of the
        client_storage.
        """
        if isinstance(key_login, str):
            key = key_login
        else:
            key = key_login.control.key
        self.page.pubsub.send_all_on_topic(self.page.client_ip, Msg("logout", key))

    def __logout_init(self, topic, msg: Msg):
        """It is executed when messages are received via pubsub."""
        try:
            if msg.method == "login":
                self.page.client_storage.set(msg.key, msg.value)

            elif msg.method == "logout":
                print("ok")
                self.page.client_storage.remove(msg.key)
                self._login_done = False
                self.page.go(self.route_login)

            elif msg.method == "updateLogin":
                self._login_done = msg.value

            elif msg.method == "updateLoginSessions":
                if not msg.value:
                    self._create_task_login_update(
                        decode=_decode_payload(
                            self.page,
                            self.key_login,
                            self.secret_key.secret
                            if self.secret_key.secret is not None
                            else self.secret_key.pem_key.public,
                        )
                    )

        except Exception:
            pass

    def login(
        self,
        key: str,
        value: Dict[str, Any],
        time_expiry: timedelta = None,
        next_route: str = None,
    ):
        """Creates the user login. | Registering in the client's storage the key and value in all browser sessions."""
        self.__key_login = key
        value = encode_verified(value, time_expiry)
        self._login_done = True

        if self.__auto_logout:
            self._create_tasks(time_expiry, key)

        self.page.client_storage.set(key, value)
        self.page.pubsub.send_others_on_topic(
            self.page.client_ip, Msg("login", key, value)
        )

        if next_route is not None:
            self.page.go(next_route)

    # ----------------------------------------------------------------

    """ Page go """

    def go(self, e: ControlEvent | str):
        """To change the path of the app, in order to reduce code, you must assign the value of the `key` parameter of the `control` used, for example buttons."""
        if isinstance(e, str):
            route = e
        else:
            route = e.control.key
        self.page.go(route)

    async def go_async(self, e: ControlEvent | str):
        """To change the path of the app, in order to reduce code, you must assign the value of the `key` parameter of the `control` used, for example buttons."""
        if isinstance(e, str):
            route = e
        else:
            route = e.control.key
        await self.page.go_async(route)
