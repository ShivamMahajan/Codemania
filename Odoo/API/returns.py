Searching 18994 files for "@api.returns"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
  896  
  897      @api.multi
  898:     @api.returns('self')
  899      def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
  900          new_invoices = self.browse()

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
  214      _description = 'Maintenance Requests'
  215  
  216:     @api.returns('self')
  217      def _default_employee_get(self):
  218          return self.env['hr.employee'].search([('user_id', '=', self.env.uid)], limit=1)
  219  
  220:     @api.returns('self')
  221      def _default_stage(self):
  222          return self.env['hr.equipment.stage'].search([], limit=1)

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_channel.py:
  178  
  179      @api.multi
  180:     @api.returns('self', lambda value: value.id)
  181      def message_post(self, body='', subject=None, message_type='notification', subtype=None, parent_id=False, attachments=None, content_subtype='html', **kwargs):
  182          # auto pin 'direct_message' channel partner

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_thread.py:
 1573  
 1574      @api.multi
 1575:     @api.returns('self', lambda value: value.id)
 1576      def message_post(self, body='', subject=None, message_type='notification',
 1577                       subtype=None, parent_id=False, attachments=None,

/home/shivamm/Desktop/odoo-9.0/addons/project_issue/project_issue.py:
  411  
  412      @api.cr_uid_ids_context
  413:     @api.returns('mail.message', lambda value: value.id)
  414      def message_post(self, cr, uid, thread_id, subtype=None, context=None, **kwargs):
  415          """ Overrides mail_thread message_post so that we can set the date of last action field when

6 matches across 5 files
