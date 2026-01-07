from odoo import models, fields, api, _
from datetime import datetime

from odoo.exceptions import ValidationError


class BiometricDevice(models.Model):
    _name = 'biometric.device'
    _description = 'Biometric Device'

    name = fields.Char(required=True)
    serial_number = fields.Char(required=True)
    ip_address = fields.Char(required=True)
    port = fields.Integer(default=4370)
    location = fields.Char()
    active = fields.Boolean(default=True)
    last_sync = fields.Datetime()
    state = fields.Selection([
        ('offline', 'Offline'),
        ('online', 'Online')
    ],default='offline')

    _check_serial_number = models.Constraint(
        'unique (serial_number)',
        'Device serial number must be unique, this one is already assigned to another device.'
    )


    @api.constrains('serial_number')
    def _check_serial_number(self):
        for rec in self:
            if rec.serial_number:
                domain = [
                    ('serial_number', '=', rec.serial_number),
                    ('id', '!=', rec.id),
                ]

                if self.search_count(domain):
                    raise ValidationError(
                        _("Device serial number must be unique.")
                    )

    def action_test_connection(self):
        self.write({
            'state': 'online',
            'last_sync': datetime.now()
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'type': 'success',
                'message': _("Device Connection Established!"),
                'next': {'type': 'ir.actions.act_window_close'},
            }
        }
