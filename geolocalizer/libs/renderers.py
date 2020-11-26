from typing import Any
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.renderers import BrowsableAPIRenderer


class BrowsableAPIRendererWithOtherInputContent(BrowsableAPIRenderer):

    def get_raw_data_form(self, data: Any, view: APIView, method: str, request: Request):
        if method in view.input_serializer_class[1]:
            view.serializer_class = view.input_serializer_class[0]
        return super(BrowsableAPIRendererWithOtherInputContent, self).get_raw_data_form(data, view, method, request)
