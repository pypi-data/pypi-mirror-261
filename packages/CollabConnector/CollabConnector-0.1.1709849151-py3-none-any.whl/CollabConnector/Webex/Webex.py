import sys
from collections import OrderedDict
import requests
from .OutputStyle import TextStyle
import json
import time
import urllib

requests.packages.urllib3.disable_warnings()


class Connect:
    class Token(object):
        import time
        import threading

    access_token = None
    refresh_token = None
    refresh_interval = 0
    client_id = None
    client_secret = None
    org = None
    active_org = None
    profile = None
    id = None
    service_url = "https://webexapis.com"
    type = "wbx"

    # store token then fetch users orgId and save
    def __init__(self,
                 access_token: str = None,
                 org_id: str = None,
                 refresh_token: str = None,
                 client_id: str = None,
                 client_secret: str = None
                 ):
        if not access_token:
            raise Exception("Must pass API token for Admin API")
        else:
            self.access_token = access_token

            try:
                self.profile = self.get("/v1/people/me?callingData=true")
                self.id = self.profile['id']
                self.org = self.profile['orgId']
                self.active_org = self.org

            except Exception as err:
                if client_id is None:
                    raise Exception(f"Error with Token or getting Org")
                else:
                    print("User profile not found. Assuming Service App!", file=sys.stderr)

            if refresh_token and client_id and client_secret:
                import threading
                import time

                self.refresh_token = refresh_token
                self.client_id = client_id
                self.client_secret = client_secret

                thread = threading.Thread(target=self.token_refresh, args=())
                thread.daemon = True
                thread.start()

            if org_id:
                self.org = org_id

    # parses out paging from response headers
    @staticmethod
    def find_next_page(call_response):
        if 'Link' in call_response.headers:
            return call_response.headers['Link'].split(";")[0].strip("<>")
        else:
            return False

    # refresh token
    def token_refresh(self):
        while True:
            time.sleep(1)
            self.refresh_interval -= 1
            if self.refresh_interval <= 0:
                refresh_data = {
                                   "grant_type": "refresh_token",
                                   "client_id": self.client_id,
                                   "client_secret": self.client_secret,
                                   "refresh_token": self.refresh_token
                                }
                try:
                    new_token = self.post("/v1/access_token", refresh_data)
                except Exception as err:
                    raise Exception(f"Not able to perform Webex Token Refresh: {err}")
                else:
                    self.access_token = new_token['access_token']
                    self.refresh_token = new_token['refresh_token']
                    self.refresh_interval = int(new_token['expires_in']) - 1000

    # basic REST GET
    def get(self, uri, data=None, limit=50000, debug=False):
        # URL encode parameters for appending to URI if provided
        if data:
            data = f"?{urllib.urlencode(data)}"
        else:
            data = ""

        headers = {"Accept": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}  # set auth header

        uri = f"{self.service_url}/{uri.strip('/')}{data}"
        return_values = {'items': []}
        # Loop while true to handled paged results and throttling
        while True:
            try:
                # send request to Webex
                response = requests.get(uri, headers=headers, verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST GET - {uri} {err}")

            else:
                if debug:
                    print("GET", uri, response.status_code, response.headers)
                if 200 <= response.status_code <= 300 and response.json():
                    # create or add to return dict
                    response_data = response.json()
                    if isinstance(response_data, dict) and len(response_data) == 1:
                        key = list(response_data.keys())[0]
                        response_data['items'] = response_data[key]
                    if 'items' in response_data:
                        return_values['items'].extend(response_data['items'])
                    else:
                        return response_data

                    # check for additional and loop until max (limit minimum is 50)
                    if len(return_values['items']) >= limit or self.find_next_page(response) is False:
                        key_list = []
                        for item in return_values['items']:
                            for key in item:
                                if key not in key_list:
                                    key_list.append(key)
                        full_return = []
                        for item in return_values['items']:
                            full_return.append(OrderedDict())
                            for key in key_list:
                                if key not in item.keys():
                                    full_return[-1][key] = None
                                else:
                                    full_return[-1][key] = item[key]
                        return full_return
                    else:
                        uri = self.find_next_page(response)
                elif 200 <= response.status_code < 300:
                    return True
                elif response.status_code == 429:  # handle throttling
                    TextStyle.warning(f"Request to {uri} throttled.  Doing it again in a bit.")
                    time.sleep(int(response.headers['Retry-After']) + 1)

                elif response.status_code == 401:  # handle auth issues
                    raise Exception("Webex Admin token invalid.  Generate new token")
                else:  # catch generic failures
                    print(f"Error sending GET to Webex - {uri}{data} {response}{response.text}", file=sys.stderr)
                    raise Exception(f"Error sending GET to Webex - {uri}{data} {response}{response.text}")

    # basic REST DELETE
    def delete(self, uri, debug=False):
        headers = {"Accept": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.delete(f"{self.service_url}/{uri.strip('/')}", headers=headers, verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST DELETE - {uri} {err}")

            else:
                if debug:
                    print("DELETE", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending DELETE to Webex - {uri} {response}{response.text}")

    # basic REST POST
    def post(self, uri, data, debug=False):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.post(f"{self.service_url}/{uri.strip('/')}",
                                         headers=headers,
                                         data=json.dumps(data),
                                         verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST POST - {uri} {err}")

            else:
                if debug:
                    print("POST", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending POST to Webex - {uri} {response}{response.text}")

    # basic REST PUT
    def put(self, uri, data, debug=False):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling\
            try:
                response = requests.put(f"{self.service_url}/{uri.strip('/')}",
                                        headers=headers,
                                        data=json.dumps(data),
                                        verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PUT - {uri} {err}")

            else:
                if debug:
                    print("PUT", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending PUT to Webex - {uri} {response}{response.text}")

    # basic REST patch
    def patch(self, uri, data, debug=False):
        headers = {"Accept": "application/json",
                   "Content-Type": "application/json",
                   "Authorization": f"Bearer {self.access_token}"}

        while True:  # loop for throttling
            try:
                response = requests.patch(f"{self.service_url}/{uri.strip('/')}",
                                          headers=headers,
                                          data=json.dumps(data),
                                          verify=False)

            except Exception as err:
                raise Exception(f"Error sending Webex REST PATCH - {uri} {err}")

            else:
                if debug:
                    print("PATCH", uri, response.status_code, response.headers)
                if response.status_code == 426:  # handle throttling
                    time.sleep(int(response.headers['Retry-After']) + 1)
                elif response.status_code == 200 and response.json():
                    return json.loads(response.text)
                elif 200 < response.status_code < 300:
                    return True
                else:
                    raise Exception(f"Error sending PATCH to Webex - {uri} {response}{response.text}")
