from infobip.util import configuration

__author__ = 'mmatosevic'

from infobip.clients import get_received_sms_logs

get_delivery_reports_client = get_received_sms_logs(configuration)
response = get_delivery_reports_client.execute({"limit": 1})
print((str(response)))
