# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.Price import Price
from infobip.api.model.sms.Error import Error
from infobip.api.model.sms.Status import Status

class SMSLog(DefaultObject):
    @property
    @serializable(name="doneAt", type=datetime)
    def done_at(self):
        return self.get_field_value("done_at")

    @done_at.setter
    def done_at(self, done_at):
        self.set_field_value("done_at", done_at)

    def set_done_at(self, done_at):
        self.done_at = done_at
        return self

    @property
    @serializable(name="bulkId", type=str)
    def bulk_id(self):
        return self.get_field_value("bulk_id")

    @bulk_id.setter
    def bulk_id(self, bulk_id):
        self.set_field_value("bulk_id", bulk_id)

    def set_bulk_id(self, bulk_id):
        self.bulk_id = bulk_id
        return self

    @property
    @serializable(name="mccMnc", type=str)
    def mcc_mnc(self):
        return self.get_field_value("mcc_mnc")

    @mcc_mnc.setter
    def mcc_mnc(self, mcc_mnc):
        self.set_field_value("mcc_mnc", mcc_mnc)

    def set_mcc_mnc(self, mcc_mnc):
        self.mcc_mnc = mcc_mnc
        return self

    @property
    @serializable(name="smsCount", type=int)
    def sms_count(self):
        return self.get_field_value("sms_count")

    @sms_count.setter
    def sms_count(self, sms_count):
        self.set_field_value("sms_count", sms_count)

    def set_sms_count(self, sms_count):
        self.sms_count = sms_count
        return self

    @property
    @serializable(name="price", type=Price)
    def price(self):
        return self.get_field_value("price")

    @price.setter
    def price(self, price):
        self.set_field_value("price", price)

    def set_price(self, price):
        self.price = price
        return self

    @property
    @serializable(name="from", type=str)
    def from_(self):
        return self.get_field_value("from_")

    @from_.setter
    def from_(self, from_):
        self.set_field_value("from_", from_)

    def set_from_(self, from_):
        self.from_ = from_
        return self

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
    @serializable(name="text", type=str)
    def text(self):
        return self.get_field_value("text")

    @text.setter
    def text(self, text):
        self.set_field_value("text", text)

    def set_text(self, text):
        self.text = text
        return self

    @property
    @serializable(name="sentAt", type=datetime)
    def sent_at(self):
        return self.get_field_value("sent_at")

    @sent_at.setter
    def sent_at(self, sent_at):
        self.set_field_value("sent_at", sent_at)

    def set_sent_at(self, sent_at):
        self.sent_at = sent_at
        return self

    @property
    @serializable(name="error", type=Error)
    def error(self):
        return self.get_field_value("error")

    @error.setter
    def error(self, error):
        self.set_field_value("error", error)

    def set_error(self, error):
        self.error = error
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