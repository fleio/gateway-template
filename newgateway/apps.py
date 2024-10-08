from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class NewgatewayConfig(AppConfig):
    name = "fleio.billing.gateways.newgateway"
    verbose_name = _("NewGateway")
    fleio_module_type = 'payment_gateway'
    module_settings = {
        'capabilities': {
            'can_process_payments': True,
            'returns_fee_information': False
        }
    }
