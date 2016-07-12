# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.Status import Status

class NCResponseDetailsAsync(DefaultObject):
    @property
    @serializable(name="messageId", type=str)
    def message_id(self):
        return self.get_field_value("message_id")

    @message_id.setter
    def message_id(self, message_id):
        self.set_field_value("message_id", message_id)

    def set_message_id(self, message_id):
        self.message_id = message_id
        return self

    @property
    @serializable(name="to", type=str)
    def to(self):
        return self.get_field_value("to")

    @to.setter
    def to(self, to):
        self.set_field_value("to", to)

    def set_to(self, to):
        self.to = to
        return self

    @property
    @serializable(name="status", type=Status)
    def status(self):
        return self.get_field_value("status")

    @status.setter
    def status(self, status):
        self.set_field_value("status", status)

    def set_status(self, status):
        self.status = status
        return self