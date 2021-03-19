from odoo import api, models, fields
from odoo.exceptions import ValidationError
from datetime import datetime


class ScheduledReminders(models.Model):
	_name = 'scheduled.reminders'
	_inherit = ['mail.thread', 'mail.activity.mixin']
	_description = 'Reminders Record'
	
	name = fields.Char(string="Tên lời nhắc")
	
	recipients = fields.Many2many(string="Người nhận", comodel_name='hr.employee')
	description = fields.Text(string="Lời nhắn")
	user_id = fields.Many2one('res.users')
	email_recipients = fields.Char(string="Email người nhận", related="recipients.work_email")
	name_recipients = fields.Char(string="Tên người nhận", related="recipients.name")
	time_reminder = fields.Datetime(string='Thời gian định gửi')
	
	
	# @api.depends('recipients')
	# def _get_name(self):
	# 	val = []
	# 	for rec in self.recipients:
	# 		val.append( rec.work_email)
	# 	self.thu_recipients = val
	
	# Sending Email in Button Click
	def action_send_email(self):
		# sending the email recipients via email
		template_id = self.env.ref('scheduled_reminders.reminder_email_template').id
		template = self.env['mail.template'].browse(template_id)
		template.send_mail(self.id, force_send=True)
	

