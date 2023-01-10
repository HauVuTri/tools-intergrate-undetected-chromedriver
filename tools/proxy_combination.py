import time

import requests


class Proxy:
    def __init__(self, key):
        self.key = key

    def get_current_proxy_data(self):
        """
        Hàm trả về thông tin proxy hiện tại(bao gồm cả status, proxy,..)
        """
        pass

    def get_current_proxy(self):
        pass

    def get_new_proxy(self):
        pass

    def get_rest_time_to_next_proxy(self):
        pass


class TMProxy(Proxy):
    def __init__(self, key):
        super().__init__(key)

    def get_current_proxy_data(self):
        if not self.key:
            raise Exception("dont have tmproxy key")
        URL = 'https://tmproxy.com/api/proxy/get-current-proxy'
        # data to be sent to api
        data = {
            "api_key": self.key,
        }
        # sending post request and saving response as response object
        r = requests.post(url=URL, json=data)
        data = r.json()
        if data['code'] == 0:
            return data
        else:
            raise Exception(data['message'])

    def get_new_proxy(self, id_location=0, protocol='https'):
        proxy_address = None
        URL = 'https://tmproxy.com/api/proxy/get-new-proxy'
        # data to be sent to api
        data = {
            "api_key": self.key,
            "sign": "string",
            "id_location": id_location
        }
        # sending post request and saving response as response object
        r = requests.post(url=URL, json=data)
        data = r.json()
        if data['code'] == 0:
            print(data)
            proxy_address = data['data'][protocol]
        else:
            print(data)
            raise Exception(data['message'])
        print(f"Proxy mới là : {proxy_address}")
        return proxy_address

    def get_rest_time_to_next_proxy(self):
        current_proxy = self.get_current_proxy_data()
        return current_proxy['data']['next_request']

    def get_current_proxy(self, protocol="https"):
        current_proxy = self.get_current_proxy_data()
        return current_proxy['data'][protocol]


class TinsoftProxy(Proxy):
    def __init__(self, key):
        super().__init__(key)

    def get_current_proxy_data(self, localtion=0):
        proxy_address = None
        PARAMS = {'key': self.key, 'location': localtion}
        URL = 'http://proxy.tinsoftsv.com/api/getProxy.php'
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        if data['success']:
            return data
        else:
            raise Exception(data.description)

    def get_new_proxy(self, location=0):
        proxy_address = None
        PARAMS = {'key': self.key, 'location': location}
        URL = 'http://proxy.tinsoftsv.com/api/changeProxy.php'
        r = requests.get(url=URL, params=PARAMS)
        data = r.json()
        if (data['proxy']):
            proxy_address = data['proxy']
        return proxy_address

    def get_rest_time_to_next_proxy(self):
        data = self.get_current_proxy_data()
        return data['next_change']

    def get_current_proxy(self):
        data = self.get_current_proxy_data()
        if not data['proxy']:
            return None
        return data['proxy']

# example: tmproxy
# key = "b4db54765ad40d61415979305a865990"
# tmproxy = TMProxy(key)
# print(tmproxy.get_new_proxy())
# time.sleep(5)
# print(tmproxy.get_current_proxy_data())
# print(tmproxy.get_current_proxy())
# print(tmproxy.get_rest_time_to_next_proxy())


# example tinsoftproxy
# key = "TLDSKAcgrY2eEqrMCFDQ8NzWl7NrS7chcqjqWG"
# tinsoft_proxy = TinsoftProxy(key)
# print(tinsoft_proxy.get_new_proxy())
# time.sleep(2)
# print(tinsoft_proxy.get_current_proxy_data())
# time.sleep(2)
# print(tinsoft_proxy.get_current_proxy())
# time.sleep(2)
# print(tinsoft_proxy.get_rest_time_to_next_proxy())
