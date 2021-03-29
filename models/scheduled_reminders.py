from odoo import api, models, fields
from odoo.exceptions import ValidationError
import datetime
from datetime import timedelta


class ScheduledReminders(models.Model):
	_name = 'scheduled.reminders'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Reminders Record'
	
	name = fields.Char('Name')
	
	recipients = fields.Many2many(string="Người nhận", comodel_name='hr.employee')
	description = fields.Text(string="Lời nhắn")
	user_id = fields.Many2one('res.users')
	time_reminder = fields.Datetime(string='Thời gian định gửi')
	
	
	# Sending Email in Button Click
	@api.multi
	def action_send_email(self):
		# sending the email recipients via email:
		template_id = self.env.ref('scheduled_reminders.reminder_email_template').id
		template = self.env['mail.template'].browse(template_id)
		template.send_mail(self.id, force_send=True)
		for rec in self:
			rec.state = 'confirm'
			return {
				'effect': {
					'fadeout': 'slow',
					'message': 'Send mail sucsses...~_~',
					'type': 'rainbow_man',
				}
			}
		

	
	def send_email(self):
		email = self.env['scheduled.reminders'].search([])
		for rc in email:
			if datetime.datetime.today() >= rc.time_reminder:
				print('chao1')
				rc.action_send_email()


