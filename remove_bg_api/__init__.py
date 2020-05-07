"""
File: remove_bg_api.py \n
Description: Remove.bg Python API Wrapper \n
Author: Anodev (OPHoperHPO) (https://github.com/OPHoperHPO) \n
License: MIT \n
"""
import requests

API_URL = "https://api.remove.bg/v1.0"  # remove.bg API Server


class RemoveBg(object):
    """
    Remove.bg API wrapper object
    """

    def __init__(self, api_key):
        self.__api_key__ = api_key
        self.account = Account(self)  # Init account object
        """Alias to Account object. USE ONLY THIS!"""

    def remove_bg_bytes(self, input_bytes: bytes, out_path="nbg.png", size="preview", raw=True, data=None):
        """
        Removes background from original_image bytes. \n
        Returns either original_image bytes or the path to the final original_image file. \n
        :param input_bytes: Image bytes. \n
        :param out_path: The path to the final original_image. If a raw parameter is present, this parameter will be
        ignored! \n
        :param size: Image size. Optional! (default preview) \n
        :param raw: Return images in bytes, or the path to the file. (True by default) \n
        :param data: Image options. Optional! Look https://www.remove.bg/api \n
        :type data: dict
        """
        if data is None:
            data = {
                "image_file": input_bytes,
                "format": "auto",
                'type': "auto",
                'size': size
            }
        else:
            data["image_file"] = input_bytes
        response = self.send_request("removebg", "POST", data)
        return self.__process_response__(response, raw, True, out_path)

    def change_api_key(self, token: str):
        """
        Updates the api key with which the library was initialized. \n
        :param token: New token.
        """
        self.__api_key__ = token

    def remove_bg_file(self, input_path: str, out_path="nbg.png", size="preview", raw=True, data=None):
        """
        Removes background from original_image file. \n
        Returns either original_image bytes or the path to the final original_image file. \n
        :param input_path: The path to the original original_image. \n
        :param out_path: The path to the final original_image. If a raw parameter is present, this parameter will be
        ignored! \n
        :param size: Image size. Optional! (default preview) \n
        :param raw: Return images in bytes, or the path to the file. (True by default) \n
        :param data: Image options. Optional! Look https://www.remove.bg/api \n
        :type data: dict \n
        """
        img = open(input_path, 'rb').read()
        if data is None:
            data = {
                "image_file": img,
                "format": "auto",
                'type': "auto",
                'size': size
            }
        else:
            data["image_file"] = img
        response = self.send_request("removebg", "POST", data)
        return self.__process_response__(response, raw, True, out_path)

    def remove_bg_url(self, input_url: str, out_path="nbg.png", size="preview", raw=True, data=None):
        """
        Removes background from original_image by URL. \n
        Returns either original_image bytes or the path to the final original_image file. \n
        :param input_url: Image link. \n
        :param out_path: The path to the final original_image. If a raw parameter is present, this parameter will be
        ignored! \n
        :param size: Image size. Optional! (default preview) \n
        :param raw: Return images in bytes, or the path to the file. (True by default) \n
        :param data: Image options. Optional! Look https://www.remove.bg/api \n
        :type data: dict
        """
        if data is None:
            data = {
                "image_url": input_url,
                "format": "auto",
                'type': "auto",
                'size': size
            }
        else:
            data["image_url"] = input_url
        response = self.send_request("removebg", "POST", data)
        return self.__process_response__(response, raw, True, out_path)

    def remove_bg_base64(self, input_base64, out_path="nbg.png", size="preview", raw=True, data=None):
        """
        Removes background from input image by URL. \n
        Returns either original_image bytes or the path to the final original_image file. \n
        :param input_base64: Base64 encoded original_image. \n
        :param out_path: The path to the final original_image. If a raw parameter is present, this parameter will be
        ignored! \n
        :param size: Image size. Optional! (default preview) \n
        :param raw: Return images in bytes, or the path to the file. (True by default) \n
        :param data: Image options. Optional! Look https://www.remove.bg/api \n
        :type data: dict
        """
        if data is None:
            data = {
                "image_file_b64": input_base64,
                "format": "auto",
                'type': "auto",
                'size': size
            }
        else:
            data["image_file_b64"] = input_base64
        response = self.send_request("removebg", "POST", data)
        return self.__process_response__(response, raw, True, out_path)

    def send_request(self, api_method: str, method: str, data=None):
        """
        Sends a request to the remove.bg server. \n
        :param api_method: API Method Look https://www.remove.bg/api \n
        :param method: Requests Method. "GET" or "POST". \n
        :param data: Data to send. Dict. Look https://www.remove.bg/api \n
        :type data: dict \n
        :return: Requests response object.
        """
        if data is None:
            data = {}
        if method == "POST":  # sending a post request
            if data:
                files = None
                if "image_file" in data.keys():
                    files = {'image_file': data["image_file"]}
                    del data["image_file"]
                response = requests.post(
                    API_URL + '/' + api_method,
                    data=data, files=files,
                    headers={'X-Api-Key': self.__api_key__}
                )
                return response
            else:
                raise Errors.EmptyResponseDataError
        elif method == "GET":  # sending a get request
            response = requests.get(
                API_URL + '/' + api_method,
                headers={'X-Api-Key': self.__api_key__}
            )
            return response
        else:
            raise Errors.WrongRequestMethodError  # raise error when method wrong

    def __process_response__(self, response: requests.Response, raw_b: bool, process_image=False,
                             output_file="nbg.png"):
        """
        Processes response from requests.bg servers.\n
        If any error appears, raises it up! \n
        :param response: Requests response object. \n
        :param output_file: Output file path. \b
        :param raw_b: Return raw bytes of original_image or path to original_image. \n
        :param process_image: Process original_image or not. \n
        :param output_file The path to output file. \n
        :return Image bytes or original_image path or response body in json
        """
        if response.status_code == 200:  # Image background removed or all ok
            if process_image is True:
                credits_charged = response.headers["X-Credits-Charged"]  # We monitor the change in account balance.
                self.account.__local_balance__ -= int(credits_charged)
                if not raw_b:
                    with open(output_file, 'wb') as f:
                        f.write(response.content)
                    return output_file
                else:
                    return response.content
            else:
                return response.json()
        elif response.status_code == 400:
            raise Errors.ApiErrorCode400  # API Error: Invalid parameters or original_image file unprocessable
        elif response.status_code == 402:
            raise Errors.ApiErrorCode402  # API Error: Insufficient credits
        elif response.status_code == 403:
            raise Errors.ApiErrorCode403  # API Error: Authentication failed
        elif response.status_code == 429:
            raise Errors.ApiErrorCode429  # API Error: Rate limit exceeded
        else:
            raise Errors.UnknownError


class Account(object):
    """
    Remove.bg Account object
    """

    def __init__(self, parent):
        self.__parent__ = parent
        self.__local_balance__ = None
        self.refresh_balance()  # Set local balance

    def balance(self):
        """
        Returns the current local account balance as the number of ALL credits. \n
        :return: Returns the current local account balance as the number of ALL credits.
        """
        return self.__local_balance__

    def refresh_balance(self):
        """
        Updates the local account balance.
        """
        self.__local_balance__ = self.get_all_info()["data"]["attributes"]["credits"]["total"]

    def get_balance_dict(self):
        """
        Gets the current account balance. This method also updates the local balance! \n
        :return: Returns a dictionary with the current account balance.
        """
        data = self.get_all_info()
        self.__local_balance__ = data["data"]["attributes"]["credits"]["total"]  # Update local balance
        return data["data"]["attributes"]["credits"]

    def free_api_calls(self):
        """
        Gets the current account free api calls. \n
        :return: Returns a dictionary with the current account free api calls.
        """
        return self.get_all_info()["data"]["attributes"]["api"]["free_calls"]

    def get_all_info(self):
        """
        Retrieves account information. \n
        Returns a dictionary with all account information. \n
        To view the dictionary layout, see https://www.remove.bg/api
        """
        response = self.__parent__.send_request("account", "GET")
        return self.__parent__.__process_response__(response, False)


class Errors:
    """This class contains all errors that may occur during operation."""

    class ApiErrorCode400(Exception):
        """API Error: Invalid parameters or original_image file unprocessable"""

        def __str__(self):
            self.txt = "API Error: Invalid parameters or original_image file unprocessable.\n" \
                       "Something is wrong with the parameters or original_image file."
            return self.txt

    class ApiErrorCode402(Exception):
        """API Error: Insufficient credits (no credits charged)"""

        def __str__(self):
            self.txt = "API Error: Insufficient credits.\n" \
                       "Buy some credits on remove.bg."
            return self.txt

    class ApiErrorCode403(Exception):
        """API Error: Authentication failed."""

        def __str__(self):
            self.txt = "API Error: Authentication failed.\n" \
                       "Specify the correct API key. "
            return self.txt

    class ApiErrorCode429(Exception):
        """API Error:  Rate limit exceeded."""

        def __str__(self):
            self.txt = "API Error: Rate limit exceeded."
            return self.txt

    class WrongRequestMethodError(Exception):
        """API Wrapper Error: A nonexistent method for sending a request to remove.bg servers is indicated. """

        def __str__(self):
            self.txt = "API Wrapper Error: " \
                       "A nonexistent method for sending a request to remove.bg servers is indicated.\n" \
                       "Look https://www.remove.bg/api."
            return self.txt

    class EmptyResponseDataError(Exception):
        """API Wrapper Error: Attempt to send empty data to remove.bg server using POST request."""

        def __str__(self):
            self.txt = "API Wrapper Error: Attempt to send empty data to remove.bg server using POST request.\n" \
                       "Look https://www.remove.bg/api."
            return self.txt

    class UnknownError(Exception):
        """API Error: Unknown Error"""

        def __str__(self):
            self.txt = "API Error: Unknown Error!"
            return self.txt
