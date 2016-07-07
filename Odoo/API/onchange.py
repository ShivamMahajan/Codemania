Searching 18994 files for "@api.onchange"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
  133          return accounts.name_get()
  134  
  135:     @api.onchange('internal_type')
  136      def onchange_internal_type(self):
  137          if self.internal_type in ('receivable', 'payable'):
  ...
  272                  raise ValidationError(_('The holder of a journal\'s bank account must be the company (%s).') % self.company_id.name)
  273  
  274:     @api.onchange('default_debit_account_id')
  275      def onchange_debit_account_id(self):
  276          if not self.default_credit_account_id:
  277              self.default_credit_account_id = self.default_debit_account_id
  278  
  279:     @api.onchange('default_credit_account_id')
  280      def onchange_credit_account_id(self):
  281          if not self.default_debit_account_id:
  ...
  559          return super(AccountTax, self).search(args, offset, limit, order, count=count)
  560  
  561:     @api.onchange('amount')
  562      def onchange_amount(self):
  563          if self.amount_type in ('percent', 'division') and self.amount != 0.0 and not self.description:
  564              self.description = "{0:.4g}%".format(self.amount)
  565  
  566:     @api.onchange('account_id')
  567      def onchange_account_id(self):
  568          self.refund_account_id = self.account_id
  569  
  570:     @api.onchange('price_include')
  571      def onchange_price_include(self):
  572          if self.price_include:
  ...
  716      second_analytic_account_id = fields.Many2one('account.analytic.account', string='Analytic Account', ondelete='set null', domain=[('state', 'not in', ('close', 'cancelled'))])
  717  
  718:     @api.onchange('name')
  719      def onchange_name(self):
  720          self.label = self.name

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_analytic_line.py:
   21  
   22      @api.v8
   23:     @api.onchange('product_id', 'product_uom_id', 'unit_amount', 'currency_id')
   24      def on_change_unit_amount(self):
   25          if not self.product_id:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
  152  
  153  
  154:     @api.onchange('journal_id')
  155      def onchange_journal_id(self):
  156          self._set_opening_balance(self.journal_id.id)

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
  408          return super(AccountInvoice, self).unlink()
  409  
  410:     @api.onchange('invoice_line_ids')
  411      def _onchange_invoice_line_ids(self):
  412          taxes_grouped = self.get_taxes_values()
  ...
  417          return
  418  
  419:     @api.onchange('partner_id', 'company_id')
  420      def _onchange_partner_id(self):
  421          account_id = False
  ...
  463              self.partner_bank_id = bank_id
  464  
  465:     @api.onchange('journal_id')
  466      def _onchange_journal_id(self):
  467          if self.journal_id:
  468              self.currency_id = self.journal_id.currency_id.id or self.journal_id.company_id.currency_id.id
  469  
  470:     @api.onchange('payment_term_id', 'date_invoice')
  471      def _onchange_payment_term_date_invoice(self):
  472          date_invoice = self.date_invoice
  ...
 1081          self.invoice_line_tax_ids = self.invoice_id.fiscal_position_id.map_tax(taxes)
 1082  
 1083:     @api.onchange('product_id')
 1084      def _onchange_product_id(self):
 1085          domain = {}
 ....
 1140          return {'domain': domain}
 1141  
 1142:     @api.onchange('account_id')
 1143      def _onchange_account_id(self):
 1144          if not self.account_id:
 ....
 1150              self._set_taxes()
 1151  
 1152:     @api.onchange('uom_id')
 1153      def _onchange_uom_id(self):
 1154          warning = {}
 ....
 1274              raise UserError(_('Percentages for Payment Term Line must be between 0 and 100.'))
 1275  
 1276:     @api.onchange('option')
 1277      def _onchange_option(self):
 1278          if self.option in ('last_day_current_month', 'last_day_following_month'):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
   64          self.hide_payment_method = len(journal_payment_methods) == 1 and journal_payment_methods[0].code == 'manual'
   65  
   66:     @api.onchange('journal_id')
   67      def _onchange_journal(self):
   68          if self.journal_id:
   ..
   96      _description = "Register payments on multiple invoices"
   97  
   98:     @api.onchange('payment_type')
   99      def _onchange_payment_type(self):
  100          if self.payment_type:
  ...
  215                  self.destination_account_id = self.partner_id.property_account_payable_id.id
  216  
  217:     @api.onchange('partner_type')
  218      def _onchange_partner_type(self):
  219          # Set partner_id domain
  ...
  221              return {'domain': {'partner_id': [(self.partner_type, '=', True)]}}
  222  
  223:     @api.onchange('payment_type')
  224      def _onchange_payment_type(self):
  225          if not self.invoice_ids:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/chart_template.py:
  561          return result
  562  
  563:     @api.onchange('sale_tax_rate')
  564      def onchange_tax_rate(self):
  565          self.purchase_tax_rate = self.sale_tax_rate or False
  566  
  567:     @api.onchange('chart_template_id')
  568      def onchange_chart_template_id(self):
  569          res = {}

/home/shivamm/Desktop/odoo-9.0/addons/account/models/partner.py:
  106          return accounts
  107  
  108:     @api.onchange('country_id')
  109      def _onchange_country_id(self):
  110          if self.country_id:
  ...
  113              self.states_count = len(self.country_id.state_ids)
  114  
  115:     @api.onchange('country_group_id')
  116      def _onchange_country_group_id(self):
  117          if self.country_group_id:
  ...
  236          return res
  237  
  238:     @api.onchange('country_id', 'zip')
  239      def _onchange_country_id(self):
  240          self.property_account_position_id = self.env['account.fiscal.position']._get_fpos_by_region(

/home/shivamm/Desktop/odoo-9.0/addons/account/models/res_config.py:
  137  
  138  
  139:     @api.onchange('company_id')
  140      def onchange_company_id(self):
  141          # update related fields
  ...
  163          return {}
  164  
  165:     @api.onchange('chart_template_id')
  166      def onchange_chart_template_id(self):
  167          tax_templ_obj = self.env['account.tax.template']
  ...
  192          return {}
  193  
  194:     @api.onchange('sale_tax_rate')
  195      def onchange_tax_rate(self):
  196          self.purchase_tax_rate = self.sale_tax_rate or False
  ...
  244              wizard.execute()
  245  
  246:     @api.onchange('group_analytic_accounting')
  247      def onchange_analytic_accounting(self):
  248          if self.group_analytic_accounting:

/home/shivamm/Desktop/odoo-9.0/addons/account_analytic_default/account_analytic_default.py:
   60      _description = "Invoice Line"
   61  
   62:     @api.onchange('product_id')
   63      def _onchange_product_id(self):
   64          res = super(account_invoice_line, self)._onchange_product_id()

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
   37      type = fields.Selection([('sale', 'Sale: Revenue Recognition'), ('purchase', 'Purchase: Asset')], required=True, index=True, default='purchase')
   38  
   39:     @api.onchange('account_asset_id')
   40      def onchange_account_asset(self):
   41          self.account_depreciation_id = self.account_asset_id
   42  
   43:     @api.onchange('type')
   44      def onchange_type(self):
   45          if self.type == 'sale':
   ..
  300          self.value_residual = self.value - total_amount - self.salvage_value
  301  
  302:     @api.onchange('company_id')
  303      def onchange_company_id(self):
  304          self.currency_id = self.company_id.currency_id.id
  ...
  316              raise ValidationError(_('Prorata temporis can be applied only for time method "number of depreciations".'))
  317  
  318:     @api.onchange('category_id')
  319      def onchange_category_id(self):
  320          vals = self.onchange_category_id_values(self.category_id.id)
  ...
  339              }
  340  
  341:     @api.onchange('method_time')
  342      def onchange_method_time(self):
  343          if self.method_time != 'number':

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset_invoice.py:
   65          return True
   66  
   67:     @api.onchange('product_id')
   68      def onchange_product_id(self):
   69          if self.product_id:

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_payment.py:
   17               "you can manage the numbering in the journal configuration page.")
   18  
   19:     @api.onchange('journal_id')
   20      def _onchange_journal_id(self):
   21          if hasattr(super(account_register_payments, self), '_onchange_journal_id'):
   ..
   24              self.check_number = self.journal_id.check_sequence_id.number_next_actual
   25  
   26:     @api.onchange('amount')
   27      def _onchange_amount(self):
   28          if hasattr(super(account_register_payments, self), '_onchange_amount'):
   ..
   55               "or if the current numbering is wrong, you can change it in the journal configuration page.")
   56  
   57:     @api.onchange('journal_id')
   58      def _onchange_journal_id(self):
   59          if hasattr(super(account_payment, self), '_onchange_journal_id'):
   ..
   62              self.check_number = self.journal_id.check_sequence_id.number_next_actual
   63  
   64:     @api.onchange('amount')
   65      def _onchange_amount(self):
   66          if hasattr(super(account_payment, self), '_onchange_amount'):

/home/shivamm/Desktop/odoo-9.0/addons/account_voucher/account_voucher.py:
  103      date_due = fields.Date('Due Date', readonly=True, select=True, states={'draft': [('readonly', False)]})
  104  
  105:     @api.onchange('partner_id', 'pay_now')
  106      def onchange_partner_id(self):
  107          if self.pay_now =='pay_now':

/home/shivamm/Desktop/odoo-9.0/addons/barcodes/doc/index.rst:
  118  When the barcode is handled server-side, it works like an onchange. The relevant model must include the
  119  BarcodeEventsMixin and redefine method on_barcode_scanned. This method receives the barcode scanned and
  120: the `self` is a pseudo-record representing the content of the form view, just like in @api.onchange methods.
  121  Barcodes prefixed with 'O-CMD' or 'O-BTN' are reserved for special features and are never passed to on_barcode_scanned.
  122  The form view barcode handler can be extended to add client-side handling. Please refer to the (hopefully

/home/shivamm/Desktop/odoo-9.0/addons/barcodes/models/barcode_events_mixin.py:
   14      _barcode_scanned = fields.Char("Barcode Scanned", help="Value of the last barcode scanned.", store=False)
   15  
   16:     @api.onchange('_barcode_scanned')
   17      def _on_barcode_scanned(self):
   18          barcode = self._barcode_scanned

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_carrier.py:
  142              return getattr(self, '%s_cancel_shipment' % self.delivery_type)(pickings)
  143  
  144:     @api.onchange('state_ids')
  145      def onchange_states(self):
  146          self.country_ids = [(6, 0, self.country_ids.ids + self.state_ids.mapped('country_id.id'))]
  147  
  148:     @api.onchange('country_ids')
  149      def onchange_countries(self):
  150          self.state_ids = [(6, 0, self.state_ids.filtered(lambda state: state.id in self.country_ids.mapped('state_ids').ids).ids)]

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/sale_order.py:
   25                  order.delivery_price = order.carrier_id.with_context(order_id=order.id).price
   26  
   27:     @api.onchange('partner_id')
   28      def onchange_partner_id_dtype(self):
   29          if self.partner_id:

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
  240          self.state = 'confirm'
  241  
  242:     @api.onchange('event_type_id')
  243      def _onchange_type(self):
  244          if self.event_type_id:
  ...
  359          self.state = 'cancel'
  360  
  361:     @api.onchange('partner_id')
  362      def _onchange_partner(self):
  363          if self.partner_id:

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
  131              raise UserError(_('No more available seats for the ticket'))
  132  
  133:     @api.onchange('product_id')
  134      def onchange_product_id(self):
  135          price = self.product_id.list_price if self.product_id else 0

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/sale_order.py:
   42          return res
   43  
   44:     @api.onchange('product_id')
   45      def product_id_change_event(self):
   46          if self.product_id.event_ok:

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
  138  
  139  
  140:     @api.onchange('equipment_assign_to')
  141      def _onchange_equipment_assign_to(self):
  142          if self.equipment_assign_to == 'employee':
  ...
  146          self.assign_date = fields.Date.context_today(self)
  147  
  148:     @api.onchange('category_id')
  149      def _onchange_category_id(self):
  150          self.user_id = self.category_id.user_id
  ...
  258          self.write({'active': True, 'stage_id': first_stage_obj.id})
  259  
  260:     @api.onchange('employee_id', 'department_id')
  261      def onchange_department_or_employee_id(self):
  262          domain = []
  ...
  272          return {'domain': {'equipment_id': domain}}
  273  
  274:     @api.onchange('equipment_id')
  275      def onchange_equipment_id(self):
  276          self.user_id = self.equipment_id.user_id if self.equipment_id.user_id else self.equipment_id.category_id.user_id
  277          self.category_id = self.equipment_id.category_id
  278  
  279:     @api.onchange('category_id')
  280      def onchange_category_id(self):
  281          if not self.user_id or not self.equipment_id or (self.user_id and not self.equipment_id.user_id):

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/models/hr_expense.py:
   59              expense.attachment_number = attachment.get(expense.id, 0)
   60  
   61:     @api.onchange('product_id')
   62      def _onchange_product_id(self):
   63          if self.product_id:
   ..
   68              self.tax_ids = self.product_id.supplier_taxes_id
   69  
   70:     @api.onchange('product_uom_id')
   71      def _onchange_product_uom_id(self):
   72          if self.product_id and self.product_uom_id.category_id != self.product_id.uom_id.category_id:
   73              raise UserError(_('Selected Unit of Measure does not belong to the same category as the product Unit of Measure'))
   74  
   75:     @api.onchange('employee_id')
   76      def _onchange_employee_id(self):
   77          self.department_id = self.employee_id.department_id

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_recruitment.py:
  211      }
  212  
  213:     @api.onchange('job_id')
  214      def onchange_job_id(self):
  215          vals = self._onchange_job_id_internal(self.job_id.id)
  ...
  238          }}
  239  
  240:     @api.onchange('partner_id')
  241      def onchange_partner_id(self):
  242          self.partner_phone = self.partner_id.phone
  ...
  244          self.email_from = self.partner_id.email
  245  
  246:     @api.onchange('stage_id')
  247      def onchange_stage_id(self):
  248          vals = self._onchange_stage_id_internal(self.stage_id.id)

/home/shivamm/Desktop/odoo-9.0/addons/l10n_be_invoice_bba/invoice.py:
   50  
   51  
   52:     @api.onchange('partner_id')
   53      def _onchange_partner_id(self):
   54          result = super(account_invoice, self)._onchange_partner_id()

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/ir_actions.py:
   26      )
   27  
   28:     @api.onchange('template_id')
   29      def on_change_template_id(self):
   30          """ Render the raw template in the server action fields. """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_template.py:
  162      copyvalue = fields.Char('Placeholder Expression', help="Final placeholder expression, to be copy-pasted in the desired template field.")
  163  
  164:     @api.onchange('model_id')
  165      def onchange_model_id(self):
  166          # TDE CLEANME: should'nt it be a stored related ?
  ...
  188          return expression
  189  
  190:     @api.onchange('model_object_field', 'sub_model_object_field', 'null_value')
  191      def onchange_sub_model_object_value_field(self):
  192          if self.model_object_field:

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/email_template_preview.py:
   36      partner_ids = fields.Many2many('res.partner', string='Recipients')
   37  
   38:     @api.onchange('res_id')
   39      @api.multi
   40      def on_change_res_id(self):

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/mail_compose_message.py:
  321  
  322      @api.multi
  323:     @api.onchange('template_id')
  324      def onchange_template_id_wrapper(self):
  325          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/my_proroject/alert.py:
   12  
   13  	
   14: 	@api.onchange('operation')
   15  	def on_change_alert(self):
   16  		

/home/shivamm/Desktop/odoo-9.0/addons/openacademy/models.py:
   36  	price=fields.Float("Total Price",readonly=True)
   37  
   38: 	@api.onchange('amount','unit_price')
   39  	def _onchange_price(self):
   40  	    # set auto-changing field
   ..
   59  #                 r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
   60  
   61: # @api.onchange('seats', 'attendee_ids')
   62  #     def _verify_valid_seats(self):
   63  #         if self.seats < 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_activity/wizard/student_migrate_wizard.py:
   52  
   53      @api.one
   54:     @api.onchange('course_from_id')
   55      def onchange_course_id(self):
   56          self.student_ids = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission.py:
  111      partner_id = fields.Many2one('res.partner', 'Partner')
  112  
  113:     @api.onchange('register_id')
  114      def onchange_register(self):
  115          self.course_id = self.register_id.course_id
  116          self.fees = self.register_id.product_id.lst_price
  117  
  118:     @api.onchange('course_id')
  119      def onchange_course(self):
  120          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_assignment/models/assignment.py:
   65                  "Submission Date cannot be set before Issue Date.")
   66  
   67:     @api.onchange('course_id')
   68      def onchange_course(self):
   69          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/models/attendance_register.py:
   32      subject_id = fields.Many2one('op.subject', 'Subject')
   33  
   34:     @api.onchange('course_id')
   35      def onchange_course(self):
   36          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/hr.py:
   26      _inherit = 'hr.employee'
   27  
   28:     @api.onchange('user_id')
   29      def onchange_user(self):
   30          if self.user_id:
   ..
   33              self.identification_id = False
   34  
   35:     @api.onchange('address_id')
   36      def onchange_address_id(self):
   37          if self.address_id:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/roll_number.py:
   32      student_id = fields.Many2one('op.student', 'Student', required=True)
   33  
   34:     @api.onchange('student_id')
   35      def onchange_student(self):
   36          self.course_id = self.student_id.course_id

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/student.py:
   74                  "Birth Date can't be greater than current date!")
   75  
   76:     @api.onchange('course_id')
   77      def onchange_course(self):
   78          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_attendees.py:
   38      batch_id = fields.Many2one('op.batch', 'Batch', readonly=True)
   39  
   40:     @api.onchange('exam_id')
   41      def onchange_exam(self):
   42          self.course_id = self.exam_id.session_id.course_id

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_res_allocation.py:
   32      student_ids = fields.Many2many('op.student', string='Student')
   33  
   34:     @api.onchange('exam_session_ids')
   35      def onchange_exam_session_res(self):
   36          for session in self.exam_session_ids:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_room.py:
   40              raise ValidationError('Capacity over Classroom capacity!')
   41  
   42:     @api.onchange('classroom_id')
   43      def onchange_classroom(self):
   44          self.capacity = self.classroom_id.capacity

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_session.py:
   43                  'End Date cannot be set before Start Date.')
   44  
   45:     @api.onchange('course_id')
   46      def onchange_course(self):
   47          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/result_template_line.py:
   39          'op.result.exam.line', 'result_id', 'Exam Lines')
   40  
   41:     @api.onchange('exam_session_id')
   42      def onchange_exam_session(self):
   43          for exam_obj in self.exam_session_id.exam_ids:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/hostel_room.py:
   39              raise ValidationError("Enter proper Student Per Room")
   40  
   41:     @api.onchange('hostel_id')
   42      def onchange_hostel(self):
   43          if self.hostel_id:
   44              self.name = False
   45  
   46:     @api.onchange('name')
   47      def onchange_name(self):
   48          if self.name:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_movement.py:
   75                      'Actual Return Date cannot be set before Issued Date')
   76  
   77:     @api.onchange('book_unit_id')
   78      def onchange_book_unit_id(self):
   79          self.state = self.book_unit_id.state
   80  
   81:     @api.onchange('library_card_id')
   82      def onchange_library_card_id(self):
   83          self.type = self.library_card_id.type

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_queue.py:
   44          'Status', copy=False, default='request', track_visibility='onchange')
   45  
   46:     @api.onchange('user_id')
   47      def onchange_user(self):
   48          self.partner_id = self.user_id.partner_id.id

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/issue_book.py:
   51                  'Return Date cannot be set before Issued Date.')
   52  
   53:     @api.onchange('library_card_id')
   54      def onchange_library_card_id(self):
   55          self.type = self.library_card_id.type

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/models/timetable.py:
   51                  'End Time cannot be set before Start Time.')
   52  
   53:     @api.onchange('course_id')
   54      def onchange_course(self):
   55          self.batch_id = False
   56  
   57:     @api.onchange('start_datetime')
   58      def onchange_start_date(self):
   59          start_datetime = datetime.datetime.strptime(

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/generate_timetable.py:
   75              raise ValidationError("End Date cannot be set before Start Date.")
   76  
   77:     @api.onchange('course_id')
   78      def onchange_course(self):
   79          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/time_table_report.py:
   57              raise ValidationError("Select date range for a week!")
   58  
   59:     @api.onchange('course_id')
   60      def onchange_course(self):
   61          self.batch_id = False

/home/shivamm/Desktop/odoo-9.0/addons/product_expiry/product_expiry.py:
   63      _inherit = 'stock.production.lot'
   64  
   65:     @api.onchange('product_id')
   66      def _onchange_product(self):
   67          defaults = self.with_context(

/home/shivamm/Desktop/odoo-9.0/addons/product_visible_discount/product_visible_discount.py:
   43  
   44      @api.multi
   45:     @api.onchange('product_id')
   46      def product_id_change(self):
   47          res = super(sale_order_line, self).product_id_change()
   ..
   70          return res
   71  
   72:     @api.onchange('product_uom')
   73      def product_uom_change(self):
   74          res = super(sale_order_line, self).product_uom_change()

/home/shivamm/Desktop/odoo-9.0/addons/purchase/invoice.py:
   13  
   14      # Load all unsold PO lines
   15:     @api.onchange('purchase_id')
   16      def purchase_order_change(self):
   17          result = []

/home/shivamm/Desktop/odoo-9.0/addons/purchase/purchase.py:
  196          return super(PurchaseOrder, self)._track_subtype(init_values)
  197  
  198:     @api.onchange('partner_id')
  199      def onchange_partner_id(self):
  200          if not self.partner_id:
  ...
  553              return datetime.today() + relativedelta(days=seller.delay if seller else 0)
  554  
  555:     @api.onchange('product_id', 'product_qty', 'product_uom')
  556      def onchange_product_id(self):
  557          result = {}

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale.py:
   86          return self.env['crm.team'].browse(default_team_id)
   87  
   88:     @api.onchange('fiscal_position_id')
   89      def _compute_tax_id(self):
   90          """
   ..
  164  
  165      @api.multi
  166:     @api.onchange('partner_shipping_id')
  167      def onchange_partner_shipping_id(self):
  168          """
  ...
  175  
  176      @api.multi
  177:     @api.onchange('partner_id')
  178      def onchange_partner_id(self):
  179          """
  ...
  693  
  694      @api.multi
  695:     @api.onchange('product_id')
  696      def product_id_change(self):
  697          if not self.product_id:
  ...
  724          return {'domain': domain}
  725  
  726:     @api.onchange('product_uom')
  727      def product_uom_change(self):
  728          if not self.product_uom:

/home/shivamm/Desktop/odoo-9.0/addons/sale/wizard/sale_make_invoice_advance.py:
   38      deposit_taxes_id = fields.Many2many("account.tax", string="Customer Taxes", help="Taxes used for deposits")
   39  
   40:     @api.onchange('advance_payment_method')
   41      def onchange_advance_payment_method(self):
   42          if self.advance_payment_method == 'percentage':

/home/shivamm/Desktop/odoo-9.0/addons/sale_margin/sale_margin.py:
    9  
   10      @api.multi
   11:     @api.onchange('product_id', 'product_uom_qty')
   12      def product_id_change_margin(self):
   13          for line in self:

/home/shivamm/Desktop/odoo-9.0/addons/sale_stock/sale_stock.py:
   35              order.delivery_count = len(order.picking_ids)
   36  
   37:     @api.onchange('warehouse_id')
   38      def _onchange_warehouse_id(self):
   39          if self.warehouse_id.company_id:
   ..
  103              line.qty_delivered_updateable = False
  104  
  105:     @api.onchange('product_id')
  106      def _onchange_product_id_set_customer_lead(self):
  107          self.customer_lead = self.product_id.sale_delay
  108          return {}
  109  
  110:     @api.onchange('product_packaging')
  111      def _onchange_product_packaging(self):
  112          if self.product_packaging:
  ...
  114          return {}
  115  
  116:     @api.onchange('product_id', 'product_uom_qty')
  117      def _onchange_product_id_check_availability(self):
  118          if not self.product_id:
  ...
  146          return {}
  147  
  148:     @api.onchange('product_uom_qty')
  149      def _onchange_product_uom_qty(self):
  150          if self.state == 'sale' and self.product_id.type != 'service' and self.product_uom_qty < self._origin.product_uom_qty:

/home/shivamm/Desktop/odoo-9.0/addons/sale_timesheet/models/sale_timesheet.py:
   29      track_service = fields.Selection(selection_add=[('timesheet', 'Timesheets on contract')])
   30  
   31:     @api.onchange('type', 'invoice_policy')
   32      def onchange_type_timesheet(self):
   33          if self.type == 'service' and self.invoice_policy == 'cost':

/home/shivamm/Desktop/odoo-9.0/addons/stock/stock.py:
 4902      _inherit = 'stock.pack.operation'
 4903  
 4904:     @api.onchange('pack_lot_ids')
 4905      def _onchange_packlots(self):
 4906          self.qty_done = sum([x.qty for x in self.pack_lot_ids])

/home/shivamm/Desktop/odoo-9.0/addons/stock_account/product.py:
   76          return super(product_template, self).create(cr, uid, vals, context=context)
   77  
   78:     @api.onchange('type')
   79      def onchange_type_valuation(self):
   80          if self.type != 'product':
   ..
  159      _inherit = 'product.product'
  160  
  161:     @api.onchange('type')
  162      def onchange_type_valuation(self):
  163          if self.type != 'product':

/home/shivamm/Desktop/odoo-9.0/addons/stock_landed_costs/purchase_config_settings.py:
   10      _inherit = 'purchase.config.settings'
   11  
   12:     @api.onchange('group_costing_method')
   13      def onchange_costing_method(self):
   14          if self.group_costing_method == 0:

/home/shivamm/Desktop/odoo-9.0/addons/warning/warning.py:
   38      _inherit = 'sale.order'
   39  
   40:     @api.onchange('partner_id')
   41      def onchange_partner_id_warning(self):
   42          if not self.partner_id:
   ..
   72      _inherit = 'purchase.order'
   73  
   74:     @api.onchange('partner_id')
   75      def onchange_partner_id_warning(self):
   76          if not self.partner_id:
   ..
  109      _inherit = 'account.invoice'
  110  
  111:     @api.onchange('partner_id', 'company_id')
  112      def _onchange_partner_id(self):
  113          result =  super(account_invoice, self)._onchange_partner_id()
  ...
  228      _inherit = 'purchase.order.line'
  229  
  230:     @api.onchange('product_id')
  231      def onchange_product_id_warning(self):
  232          if not self.product_id:

/home/shivamm/Desktop/odoo-9.0/addons/website_quote/models/order.py:
  400          return self.on_change_product_id(cr, uid, ids, product, uom_id=uom_id, context=context)
  401  
  402:     @api.onchange('product_id')
  403      def _onchange_product_id(self):
  404          product = self.product_id.with_context(lang=self.order_id.partner_id.lang)

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/slides.py:
  123          return res
  124  
  125:     @api.onchange('visibility')
  126      def change_visibility(self):
  127          if self.visibility == 'public':
  ...
  261      mime_type = fields.Char('Mime-type')
  262  
  263:     @api.onchange('url')
  264      def on_change_url(self):
  265          self.ensure_one()

125 matches across 64 files
