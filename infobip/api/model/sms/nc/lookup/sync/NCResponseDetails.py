# -*- coding: utf-8 -*-
"""This is a generated class and is not intended for modification!
TODO: Point to Github contribution instructions
"""


from datetime import datetime
from infobip.util.models import DefaultObject, serializable
from infobip.api.model.sms.nc.lookup.Network import Network
from infobip.api.model.sms.Error import Error
from infobip.api.model.sms.Status import Status

class NCResponseDetails(DefaultObject):
    @property
    @serializable(name="ported", type=bool)
    def ported(self):
        return self.get_field_value("ported")

    @ported.setter
    def ported(self, ported):
        self.set_field_value("ported", ported)

    def set_ported(self, ported):
        self.ported = ported
        return self

    @property
    @serializable(name="roaming", type=bool)
    def roaming(self):
        return self.get_field_value("roaming")

    @roaming.setter
    def roaming(self, roaming):
        self.set_field_value("roaming", roaming)

    def set_roaming(self, roaming):
        self.roaming = roaming
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
    @serializable(name="roamingNetwork", type=Network)
    def roaming_network(self):
        return self.get_field_value("roaming_network")

    @roaming_network.setter
    def roaming_network(self, roaming_network):
        self.set_field_value("roaming_network", roaming_network)

    def set_roaming_network(self, roaming_network):
        self.roaming_network = roaming_network
        return self

    @property
    @serializable(name="portedNetwork", type=Network)
    def ported_network(self):
        return self.get_field_value("ported_network")

    @ported_network.setter
    def ported_network(self, ported_network):
        self.set_field_value("ported_network", ported_network)

    def set_ported_network(self, ported_network):
        self.ported_network = ported_network
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
    @serializable(name="imsi", type=str)
    def imsi(self):
        return self.get_field_value("imsi")

    @imsi.setter
    def imsi(self, imsi):
        self.set_field_value("imsi", imsi)

    def set_imsi(self, imsi):
        self.imsi = imsi
        return self

    @property
    @serializable(name="servingMSC", type=str)
    def serving_m_s_c(self):
        return self.get_field_value("serving_m_s_c")

    @serving_m_s_c.setter
    def serving_m_s_c(self, serving_m_s_c):
        self.set_field_value("serving_m_s_c", serving_m_s_c)

    def set_serving_m_s_c(self, serving_m_s_c):
        self.serving_m_s_c = serving_m_s_c
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
    @serializable(name="originalNetwork", type=Network)
    def original_network(self):
        return self.get_field_value("original_network")

    @original_network.setter
    def original_network(self, original_network):
        self.set_field_value("original_network", original_network)

    def set_original_network(self, original_network):
        self.original_network = original_network
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