""" myRIO API client: An API client for the myRIO API server

    Last update: 2024/03/12 Aitzol Ezeiza Ramos UPV/EHU

    This is the client of the myRIO API server. Please refer to the
    server documentation for further help. 
    The basics are:
        · Digital Inputs and Outputs
        · Analog Inputs and Outputs
        · onboard button and LEDs
        · onboard accelerometer
    The default port is 8080. Some examples of API calls
    (using curl) would be the following:

    curl -X POST http://172.22.11.2:8080/digital_output/2/1

    This turns on the digital output DIO2 on the default MXP port (A)
    If you use Windows Powershell, you should replace the -X with -method X

    curl -method POST http://172.22.11.2:8080/digital_output/2/1

    You can change the default port with a parameter:

    curl -X GET http://172.22.11.2:8080/digital_input/3?port=B

    Read the examples un the examples folder for more info.
    """

import requests
from typing import Tuple

DEFAULT_HTTP_PORT = 8080
DEFAULT_HOST_IP = "172.22.11.2"

class MyRIO_API_Client:
    """ class MyRIO_API_Client
    This is the base class for making requests to the API.
    We define generic methods for further development and
    developer flexibility. Anyway, there will be specific
    methods for each application route of the API server.

    Developer methods:
        make_request
        get_data
        post_data
        put_data
        delete_data

    Basic methods:
        get_digital_input
        set_digital_output
        get_analog_input
        set_analog_output
        get_onboard_button
        set_onboard_leds
        get_onboard_accelerometer
"""

    def __init__(self, ip_address: str=DEFAULT_HOST_IP,
                 port: int=DEFAULT_HTTP_PORT):
        self.base_url = 'http://'+ip_address+':'+str(DEFAULT_HTTP_PORT)

    def make_request(self, method, endpoint, data=None, params=None):
        url = self.base_url + '/' + endpoint
        response = requests.request(method, url, json=data, params=params)
        response.raise_for_status()
        json_response = response.json()
        
        # Check if the response is a success message
        if isinstance(json_response, dict) and json_response.get("success") is True:
            return None  # Success message, no need to process
        # Check for a single key-value pair
        if isinstance(json_response, dict) and len(json_response) == 1:
            key, value = next(iter(json_response.items()))
            return value
        # Check for a dict of three key-value pairs (accelerometer)
        if isinstance(json_response, dict) and len(json_response) == 3:
            return list(json_response.values())
        # If none of the above cases match, return the full JSON response
        else:
            return json_response

    def get_data(self, endpoint, params=None):
        return self.make_request("GET", endpoint, params=params)

    def post_data(self, endpoint, data=None):
        return self.make_request("POST", endpoint, data=data)

    def put_data(self, endpoint, data=None):
        return self.make_request("PUT", endpoint, data=data)

    def delete_data(self, endpoint, params=None):
        return self.make_request("DELETE", endpoint, params=params)

    def get_digital_input(self, channel_in: int, port_in: str='A') -> bool:
        """ Returns the value (true/false) of a digital input """
        if port_in == 'A':
            endpoint = 'digital_input/'+str(channel_in)
        else:
            endpoint = 'digital_input/'+str(channel_in)+'?port='+port_in

        response=self.get_data(endpoint)
        return response

    def set_digital_output(self, channel_in: int, value_in: int, port_in: str='A'):
        """ Sets the value (true 1, false 0) of a digital output """
        if port_in == 'A':
            endpoint = 'digital_output/'+str(channel_in)+'/'+str(value_in)
        else:
            endpoint = 'digital_output/'+str(channel_in)+'/'+str(value_in)+'?port='+port_in
        self.post_data(endpoint)

    def get_analog_input(self, channel_in: int, port_in: str='A') -> float:
        """ Returns the value (volts in float type) of an analog input """
        if port_in == 'A':
            endpoint = 'analog_input/'+str(channel_in)
        else:
            endpoint = 'analog_input/'+str(channel_in)+'?port='+port_in
        response=self.get_data(endpoint)
        return float(response)

    def set_analog_output(self, channel_in: int, value_in: float, port_in: str='A'):
        """ Sets the value (volts in float type) of an analog output """
        if port_in == 'A':
            endpoint = 'analog_output/'+str(channel_in)+'/'+str(value_in)
        else:
            endpoint = 'analog_output/'+str(channel_in)+'/'+str(value_in)+'?port='+port_in
        self.post_data(endpoint)

    def get_onboard_button(self) -> bool:
        """ Returns the value (true/false) of the onboard button """
        endpoint = 'onboard_button'
        response=self.get_data(endpoint)
        return response

    def set_onboard_leds(self, value_in: int):
        """ Sets the value (0..15 integer) of the onboard LEDs """
        endpoint = 'onboard_leds/'+str(value_in)
        response=self.post_data(endpoint)

    def get_onboard_accelerometer(self) -> Tuple[float, float, float]:
        """ Returns the value (x, y, z floats) of the onboard accelerometer """
        endpoint = 'onboard_accelerometer'
        response=self.get_data(endpoint)
        return response

if __name__ == "__main__":
    from time import sleep
    myRIO = MyRIO_API_Client()
    print('Accelerometer:')
    print(myRIO.get_onboard_accelerometer())
    print('Onboard button:')
    print(myRIO.get_onboard_button())
    print('Digital Input 3:')
    print(myRIO.get_digital_input(3))
    print('Digital Input 0 (port B):')
    print(myRIO.get_digital_input(3,port_in='B'))
    print('Analog Input 1:')
    print(myRIO.get_analog_input(1))
    print('Onboard LEDS (all ON)')
    print(myRIO.set_onboard_leds(15))
    sleep(1)
    print('Onboard LEDS (all OFF)')
    print(myRIO.set_onboard_leds(0))
    sleep(1)
    print('Digital Output 0 ON')
    print(myRIO.set_digital_output(0,1))
    sleep(1)
    print('Digital Output 0 OFF')
    print(myRIO.set_digital_output(0,0))
    sleep(1)
    print('Analog Output 0 5.0V')
    myRIO.set_analog_output(0,5.0)
    print('Analog Input 2: (the same if wired)')
    print(myRIO.get_analog_input(2))
    sleep(1)
    print('Analog Output 0 0.0V')
    myRIO.set_analog_output(0,0.0)
    print('Analog Input 2: (the same if wired)')
    print(myRIO.get_analog_input(2))
