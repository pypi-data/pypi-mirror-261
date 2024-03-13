import requests


class F2Client:
    def __init__(self, api_key):
        self.url = "https://www.fast2sms.com/dev/bulkV2"
        self.headers = {'cache-control': "no-cache"}
        self.api_key = api_key

    def send_otp(self, numbers, otp):
        querystring = {
            "authorization": self.api_key,
            "variables_values": otp,
            "route": "otp",
            "numbers": numbers
        }
        return requests.request("GET", self.url, headers=self.headers, params=querystring)

    def send_dlt(self, numbers, dlt_id, msg_id, var_values):
        querystring = {
            "authorization": self.api_key,
            "sender_id": dlt_id,
            "message": msg_id,
            "variables_values": var_values,
            "route": "dlt",
            "numbers": numbers
        }
        return requests.request("GET", self.url, headers=self.headers, params=querystring)

    def quick_sms(self, numbers, msg):
        querystring = {
            "authorization": self.api_key,
            "message": msg,
            "language": "english",
            "route": "q",
            "numbers": numbers
        }
        return requests.request("GET", self.url, headers=self.headers, params=querystring)

    def otp_voice_call(self, numbers, otp):
        querystring = {
            "authorization": self.api_key,
            "variables_values": otp,
            "route": "otp",
            "numbers": numbers
        }
        return requests.request("GET", self.url, headers=self.headers, params=querystring)

    def dlt_manual_sms(self, numbers, dlt_id, msg_id, template_id, entity_id):
        querystring = {
            "authorization": self.api_key,
            "sender_id": dlt_id,
            "message": msg_id,
            "template_id": template_id,
            "entity_id": entity_id,
            "route": "dlt_manual",
            "numbers": numbers
        }
        return requests.request("GET", self.url, headers=self.headers, params=querystring)

    def wallet_balance(self):
        headers = {'authorization': self.api_key}
        url = "https://www.fast2sms.com/dev/wallet"
        return requests.request("POST", url, headers=headers)