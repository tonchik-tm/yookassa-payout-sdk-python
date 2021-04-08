# -*- coding: utf-8 -*-
from yookassa_payout.domain.request.deposition_request import DepositionRequest


class MakeDepositionRequest(DepositionRequest):

    def __init__(self, *args, **kwargs):
        super(MakeDepositionRequest, self).__init__(*args, **kwargs)
        self.request_name = 'makeDeposition'

    def map(self):
        self.validate()
        _map = super(MakeDepositionRequest, self).map()
        return {self.request_name + 'Request': _map}
