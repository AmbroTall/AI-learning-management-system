"""Payment utilities — Network Global gateway (XML-based)."""

import uuid
import xml.etree.ElementTree as et
from datetime import datetime
from typing import Any

import requests
from django.conf import settings


class NetworkGlobal:
    """
    Abstraction class for interacting with the Network Global payment API.
    Network Global uses XML for its request/response format.
    """

    def __init__(self, config: dict[str, str]) -> None:
        self.network_global_url = config.get("BASE_URL")
        self.company_token = config.get("COMPANY_TOKEN")
        self.base_url = f"{self.network_global_url}"
        self.frontend_redirect_url = config.get("FRONTEND_REDIRECT_URL")

    def make_request(
        self, endpoint: str, method: str, xml_payload: str = None, params: dict = None
    ):
        url = f"{self.base_url}/{endpoint}"
        headers = {"Content-Type": "application/xml"}

        match method.upper():
            case "POST":
                response = requests.post(url, data=xml_payload, headers=headers, timeout=10)
            case "GET":
                response = requests.get(url, params=params, headers=headers, timeout=10)
            case "PUT":
                response = requests.put(url, data=xml_payload, headers=headers, timeout=10)
            case "DELETE":
                response = requests.delete(url, params=params, headers=headers, timeout=10)
            case _:
                raise ValueError(f"Unsupported HTTP method: {method}")

        return self.xml_to_dict(response.content)

    def xml_to_dict(self, xml_data):
        tree = et.ElementTree(et.fromstring(xml_data))
        root = tree.getroot()

        def recursive_dict(element: et.Element):
            return {
                element.tag: (
                    {child.tag: recursive_dict(child) for child in element}
                    if element
                    else element.text
                )
            }

        return recursive_dict(root)

    def create_transaction_token(self, data: dict[str, Any]):
        """
        Create a token to initiate a transaction.
        Returns the TransToken used to redirect the user to the payment page.
        """
        root = et.Element("API3G")

        company_token = et.SubElement(root, "CompanyToken")
        company_token.text = self.company_token

        request_type = et.SubElement(root, "Request")
        request_type.text = "createToken"

        transaction = et.SubElement(root, "Transaction")

        payment_amount = et.SubElement(transaction, "PaymentAmount")
        payment_amount.text = data.get("amount")

        payment_currency = et.SubElement(transaction, "PaymentCurrency")
        payment_currency.text = data.get("currency")

        payment_ref = et.SubElement(transaction, "CompanyRef")
        payment_ref.text = data.get("id")

        payment_ref_unique = et.SubElement(transaction, "CompanyRefUnique")
        payment_ref_unique.text = "1"

        redirect_url = et.SubElement(transaction, "RedirectURL")
        endpoint = data.get("endpoint")
        redirect_url.text = f"{self.frontend_redirect_url}/payments/{endpoint}/"

        back_url = et.SubElement(transaction, "BackURL")
        back_url.text = data.get("url")

        services_element = et.SubElement(root, "Services")
        services = data.get("services")

        for service in services:
            service_element = et.SubElement(services_element, "Service")

            service_type = et.SubElement(service_element, "ServiceType")
            service_type.text = service.get("name")

            service_description = et.SubElement(service_element, "ServiceDescription")
            service_description.text = service.get("description")

            current_time = datetime.now().strftime("%Y/%m/%d %H:%M")
            service_date = et.SubElement(service_element, "ServiceDate")
            service_date.text = current_time

        payload = et.tostring(root, encoding="utf-8")
        response = self.make_request("API/v6/", "POST", payload, None)
        result = response.get("API3G")

        code = result.get("Result").get("Result")
        explanation = result.get("ResultExplanation").get("ResultExplanation")

        if code != "000":
            raise ValueError(explanation)

        return result.get("TransToken").get("TransToken")

    def verify_transaction_token(self, token: str):
        """
        Verify whether a transaction token has been successfully paid.
        Returns the result dict on success, raises ValueError on failure.
        """
        root = et.Element("API3G")

        company_token = et.SubElement(root, "CompanyToken")
        company_token.text = self.company_token

        request_type = et.SubElement(root, "Request")
        request_type.text = "verifyToken"

        transaction = et.SubElement(root, "TransactionToken")
        transaction.text = token

        payload = et.tostring(root, encoding="utf-8")
        response = self.make_request("API/v7/", "POST", payload, None)
        result = response.get("API3G")

        code = result.get("Result").get("Result")
        explanation = result.get("ResultExplanation").get("ResultExplanation")

        if code != "000":
            raise ValueError(explanation)

        return result

    def generate_network_payment_url(self, token: str) -> str:
        return f"{self.base_url}/payv3.php?ID={token}"


def get_network_global_client() -> NetworkGlobal:
    config = {
        "BASE_URL": settings.NETWORK_GLOBAL_ENDPOINT,
        "COMPANY_TOKEN": settings.NETWORK_GLOBAL_COMPANY_TOKEN,
        "FRONTEND_REDIRECT_URL": settings.FRONTEND_URL,
    }
    return NetworkGlobal(config=config)
