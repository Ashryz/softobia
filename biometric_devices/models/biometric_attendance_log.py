from odoo import models, fields

class BiometricAttendanceLog(models.Model):
    _name = 'biometric.attendance.log'
    _description = 'Biometric Attendance Log'
    _order = 'punch_time desc'
    _rec_name = 'employee_id'

    device_id = fields.Many2one(
        'biometric.device',
        ondelete='set null'
    )
    employee_id = fields.Many2one('hr.employee')
    punch_time = fields.Datetime(required=True)
    punch_type = fields.Selection(
        [('in', 'Check In'), ('out', 'Check Out')],
        required=True
    )
    state = fields.Selection([
        ('pending', 'Pending'),
        ('processed', 'Processed'),
        ('error', 'Error')
    ],default='pending')
    error_message = fields.Text()