from datetime import datetime, timedelta

import requests


class Dashboard:
    """This class wraps the dashboard API. 

    The user has the choice to either login via setting the combination of username, password and customer_id or 
    via a session_id. 

    If username, password and customer_id are used, the user has to call login before doing anything further. This 
    step is not necessary when a session_id is used.
    """
    BASE_URL: str = 'https://api.blaulichtsms.net/blaulicht'
    _min_fetch_interval: timedelta = timedelta(seconds=1.0)
    _last_fetch: datetime | None = None
    _last_data: dict | None = None
    _session_id: str | None = None

    def __init__(self, *, 
                 username: str | None = None, 
                 password: str | None = None, 
                 customer_id: str | None = None, 
                 session_id: str | None = None):
        """ Initializes a Dashboard Client

        This function expects either a single session_id or all of username, password and customer_id. 
        These are not about the login data provided to the user, but the information which is given when creating a dashboard in the UI
        
        :param username: The dashboard username
        :param password: The dashboard password
        :param customer_id: The customerId of the dashboard
        :param session_id: Session ID of the dashboard
        """
        assert (session_id is not None) or (username is not None and password is not None and customer_id is not None)
        self._username = username
        self._password = password
        self._customer_id = customer_id
        self._session_id = session_id

    @property
    def min_fetch_interval(self):
        """ Minimum interval in which the API is requested """
        return self._min_fetch_interval

    @min_fetch_interval.setter
    def min_fetch_interval(self, value: timedelta):
        """ Minimum interval in which the API is requested """
        self._min_fetch_interval = value 

    @property
    def _should_fetch(self):
        """ Indicates if it's time again to fetch again from the API """
        if self._last_fetch is None:
            return True
        now = datetime.now()
        delta: timedelta = (now - self._last_fetch)
        return delta.seconds >= self._min_fetch_interval.seconds

    def login(self):
        """ Login to the dashboard

        The credentials given when creating this client are used. Calling this
        function is not necessary when a session_id was given upon creating.
        """
        if self._session_id is None:
            endpoint = f'{self.BASE_URL}/api/alarm/v1/dashboard/login'
            response = requests.post(endpoint, json={
                'username': self._username,
                'password': self._password,
                'customerId': self._customer_id,
            })
            resp_data = response.json()
            if resp_data.get('success', False):
                self._session_id = resp_data.get('sessionId')
            else:
                raise Exception()

    def _fetch(self, *, forced=False) -> dict:
        """ Fetch the latest data from the endpoint 

        :param forced: If forced is True the API will be fetched no matter if it's time or not
        """
        if not self._should_fetch and not forced and self._last_data is not None:
            return self._last_data
        if self._session_id is None:
            raise Exception()
        endpoint = f'{self.BASE_URL}/api/alarm/v1/dashboard/{self._session_id}'
        return requests.get(endpoint).json()

    @property
    def alarms(self):
        """ Get the alarms """
        return self._fetch().get('alarms', [])

    @property
    def infos(self):
        """ Get the infos """
        return self._fetch().get('infos', [])

    
