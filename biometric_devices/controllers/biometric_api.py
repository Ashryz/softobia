from odoo import http
from odoo.http import request
from datetime import datetime

class BiometricAPI(http.Controller):

    @http.route('/api/biometric/attendance', type='jsonrpc', auth='public', methods=['POST'],csrf=False)
    def push_attendance(self, **payload):

        serial = payload.get('device_serial')
        punches = payload.get('punches', [])

        device = request.env['biometric.device'].sudo().search([
            ('serial_number', '=', serial),
            ('is_active', '=', True)
        ], limit=1)

        if not device:
            return {'success': False, 'message': 'Invalid device'}

        created = 0
        errors = []

        Employee = request.env['hr.employee'].sudo()
        Log = request.env['biometric.attendance.log'].sudo()

        for punch in punches:
            try:
                emp = Employee.search([
                    ('pin', '=', punch.get('pin'))
                ], limit=1)

                if not emp:
                    raise Exception('Employee not found')

                Log.create({
                    'device_id': device.id,
                    'employee_id': emp.id,
                    'punch_time': punch.get('timestamp'),
                    'punch_type': punch.get('type'),
                })
                created += 1
            except Exception as e:
                errors.append(str(e))

        device.write({
            'last_sync': datetime.now(),
            'status': 'online'
        })

        return {
            'success': True,
            'created': created,
            'errors': errors
        }
