from typing import ClassVar, Optional, Type, Mapping, Any

from ..base_client import BaseClient
from ..mixins import (
    FindAllCommandMixin,
    FindCommandMixin,
    UpdateCommandMixin,
    CreateCommandMixin,
)
from ..models.invoice import InvoicePreview, InvoiceResponse
from ..services.json import to_json
from ..services.request import (
    make_headers,
    make_url,
    send_post_request,
    send_put_request,
)
from ..services.response import get_response_data, prepare_object_response, Response


class InvoiceClient(
    FindCommandMixin[InvoiceResponse],
    FindAllCommandMixin[InvoiceResponse],
    UpdateCommandMixin[InvoiceResponse],
    CreateCommandMixin[InvoiceResponse],
    BaseClient,
):
    API_RESOURCE: ClassVar[str] = "invoices"
    RESPONSE_MODEL: ClassVar[Type[InvoiceResponse]] = InvoiceResponse
    ROOT_NAME: ClassVar[str] = "invoice"

    def download(self, resource_id: str) -> Optional[InvoiceResponse]:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "download"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        response_data = get_response_data(response=api_response, key=self.ROOT_NAME)
        if not response_data:
            return None

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=response_data,
        )

    def retry_payment(self, resource_id: str) -> Optional[InvoiceResponse]:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "retry_payment"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        response_data = get_response_data(response=api_response, key=self.ROOT_NAME)
        if not response_data:
            return None

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=response_data,
        )

    def refresh(self, resource_id: str) -> InvoiceResponse:
        api_response: Response = send_put_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "refresh"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def retry(self, resource_id: str) -> InvoiceResponse:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "retry"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def finalize(self, resource_id: str) -> InvoiceResponse:
        api_response: Response = send_put_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "finalize"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def void(self, resource_id: str) -> InvoiceResponse:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "void"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def lose_dispute(self, resource_id: str) -> InvoiceResponse:
        api_response: Response = send_put_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "lose_dispute"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=self.RESPONSE_MODEL,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def payment_url(self, resource_id: str) -> str:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "payment_url"),
            ),
            headers=make_headers(api_key=self.api_key),
        )

        response_data = get_response_data(response=api_response, key="invoice_payment_details")
        return response_data.get("payment_url", "") if isinstance(response_data, Mapping) else ""

    def preview(self, input_object: InvoicePreview) -> InvoiceResponse:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, "preview"),
            ),
            content=to_json(input_object.dict()),
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=InvoiceResponse,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )

    def void_invoice(self, resource_id: str, options: Mapping[str, Any] = {}) -> InvoiceResponse:
        api_response: Response = send_post_request(
            url=make_url(
                origin=self.base_url,
                path_parts=(self.API_RESOURCE, resource_id, "void"),
            ),
            content=to_json(options) if options else None,
            headers=make_headers(api_key=self.api_key),
        )

        return prepare_object_response(
            response_model=InvoiceResponse,
            data=get_response_data(response=api_response, key=self.ROOT_NAME),
        )
