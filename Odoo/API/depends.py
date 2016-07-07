Searching 18994 files for "@api.depends"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
  139  
  140      @api.multi
  141:     @api.depends('name', 'code')
  142      def name_get(self):
  143          result = []
  ...
  440  
  441      @api.multi
  442:     @api.depends('name', 'currency_id', 'company_id', 'company_id.currency_id')
  443      def name_get(self):
  444          res = []
  ...
  450  
  451      @api.multi
  452:     @api.depends('inbound_payment_method_ids', 'outbound_payment_method_ids')
  453      def _methods_compute(self):
  454          for journal in self:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
   19  
   20      @api.one
   21:     @api.depends('coin_value', 'number')
   22      def _sub_total(self):
   23          """ Calculates Sub total"""
   ..
   74  
   75      @api.one
   76:     @api.depends('line_ids', 'balance_start', 'line_ids.amount', 'balance_end_real')
   77      def _end_balance(self):
   78          self.total_entry_encoding = sum([line.amount for line in self.line_ids])
   ..
   81  
   82      @api.one
   83:     @api.depends('journal_id')
   84      def _compute_currency(self):
   85          self.currency_id = self.journal_id.currency_id or self.env.user.company_id.currency_id
   86  
   87      @api.one
   88:     @api.depends('line_ids.journal_entry_ids')
   89      def _check_lines_reconciled(self):
   90          self.all_lines_reconciled = all([line.journal_entry_ids.ids or line.account_id.id for line in self.line_ids])

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
   40  
   41      @api.one
   42:     @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'currency_id', 'company_id')
   43      def _compute_amount(self):
   44          self.amount_untaxed = sum(line.price_subtotal for line in self.invoice_line_ids)
   ..
   76  
   77      @api.one
   78:     @api.depends(
   79          'state', 'currency_id', 'invoice_line_ids.price_subtotal',
   80          'move_id.line_ids.amount_residual',
   ..
  132  
  133      @api.one
  134:     @api.depends('payment_move_line_ids.amount_residual')
  135      def _get_payment_info_JSON(self):
  136          self.payments_widget = json.dumps(False)
  ...
  168  
  169      @api.one
  170:     @api.depends('move_id.line_ids.amount_residual')
  171      def _compute_payments(self):
  172          payment_lines = []
  ...
  993  
  994      @api.one
  995:     @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
  996          'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id')
  997      def _compute_price(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_move.py:
   21  
   22      @api.multi
   23:     @api.depends('name', 'state')
   24      def name_get(self):
   25          result = []
   ..
   33  
   34      @api.multi
   35:     @api.depends('line_ids.debit', 'line_ids.credit')
   36      def _amount_compute(self):
   37          for move in self:
   ..
   41              move.amount = total
   42  
   43:     @api.depends('line_ids.debit', 'line_ids.credit', 'line_ids.matched_debit_ids.amount', 'line_ids.matched_credit_ids.amount', 'line_ids.account_id.user_type_id.type')
   44      def _compute_matched_percentage(self):
   45          """Compute the percentage to apply for cash basis method. This value is relevant only for moves that
   ..
   61  
   62      @api.one
   63:     @api.depends('company_id')
   64      def _compute_currency(self):
   65          self.currency_id = self.company_id.currency_id or self.env.user.company_id.currency_id
   ..
  220      _order = "date desc, id desc"
  221  
  222:     @api.depends('debit', 'credit', 'amount_currency', 'currency_id', 'matched_debit_ids.amount', 'matched_credit_ids.amount', 'account_id.currency_id')
  223      def _amount_residual(self):
  224          """ Computes the residual amount of a move line from a reconciliable account in the company currency and the line's currency.
  ...
  258              line.amount_residual_currency = line.currency_id and line.currency_id.round(amount_residual_currency * sign) or 0.0
  259  
  260:     @api.depends('debit', 'credit')
  261      def _store_balance(self):
  262          for line in self:
  ...
  289          return journal_id
  290  
  291:     @api.depends('debit', 'credit', 'move_id.matched_percentage', 'move_id.journal_id')
  292      def _compute_cash_basis(self):
  293          for move_line in self:
  ...
  301  
  302      @api.one
  303:     @api.depends('move_id.line_ids')
  304      def _get_counterpart(self):
  305          counterpart = set()
  ...
 1045  
 1046      @api.multi
 1047:     @api.depends('ref', 'move_id')
 1048      def name_get(self):
 1049          result = []

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
   56  
   57      @api.one
   58:     @api.depends('payment_type', 'journal_id')
   59      def _compute_hide_payment_method(self):
   60          if not self.journal_id:
   ..
  167  
  168      @api.one
  169:     @api.depends('invoice_ids')
  170      def _get_has_invoices(self):
  171          self.has_invoices = bool(self.invoice_ids)
  172  
  173      @api.one
  174:     @api.depends('invoice_ids', 'amount', 'payment_date', 'currency_id')
  175      def _compute_payment_difference(self):
  176          if len(self.invoice_ids) == 0:
  ...
  201  
  202      @api.one
  203:     @api.depends('invoice_ids', 'payment_type', 'partner_type', 'partner_id')
  204      def _compute_destination_account_id(self):
  205          if self.invoice_ids:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/chart_template.py:
   43  
   44      @api.multi
   45:     @api.depends('name', 'code')
   46      def name_get(self):
   47          res = []
   ..
  412  
  413      @api.multi
  414:     @api.depends('name', 'description')
  415      def name_get(self):
  416          res = []

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_financial_report.py:
   14  
   15      @api.multi
   16:     @api.depends('parent_id', 'parent_id.level')
   17      def _get_level(self):
   18          '''Returns a dictionary with key=the ID of a record and value = the level of this  

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_invoice_report.py:
   12  
   13      @api.multi
   14:     @api.depends('currency_id', 'date', 'price_total', 'price_average', 'residual')
   15      def _compute_amounts_in_user_currency(self):
   16          """Compute the amounts in the currency of the user

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_invoice_refund.py:
   28          default='refund', string='Refund Method', required=True, help='Refund base on this type. You can not Modify and Cancel if the invoice is already reconciled')
   29  
   30:     @api.depends('date_invoice')
   31      @api.one
   32      def _get_refund_only(self):

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
  292  
  293      @api.one
  294:     @api.depends('value', 'salvage_value', 'depreciation_line_ids')
  295      def _amount_residual(self):
  296          total_amount = 0.0
  ...
  305  
  306      @api.multi
  307:     @api.depends('account_move_ids')
  308      def _entry_count(self):
  309          for asset in self:
  ...
  400  
  401      @api.one
  402:     @api.depends('move_id')
  403      def _get_move_check(self):
  404          self.move_check = bool(self.move_id)

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset_invoice.py:
   28  
   29      @api.one
   30:     @api.depends('asset_category_id', 'invoice_id.date_invoice')
   31      def _get_asset_date(self):
   32          self.asset_mrr = 0

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_journal.py:
    8  
    9      @api.one
   10:     @api.depends('outbound_payment_method_ids')
   11      def _compute_check_printing_payment_method_selected(self):
   12          self.check_printing_payment_method_selected = any(pm.code == 'check_printing' for pm in self.outbound_payment_method_ids)
   13  
   14      @api.one
   15:     @api.depends('check_manual_sequencing')
   16      def _get_check_next_number(self):
   17          if self.check_sequence_id:

/home/shivamm/Desktop/odoo-9.0/addons/account_voucher/account_voucher.py:
   12  
   13      @api.one
   14:     @api.depends('move_id.line_ids.reconciled', 'move_id.line_ids.account_id.internal_type')
   15      def _check_paid(self):
   16          self.paid = any([((line.account_id.internal_type, 'in', ('receivable', 'payable')) and line.reconciled) for line in self.move_id.line_ids])
   ..
   24  
   25      @api.multi
   26:     @api.depends('name', 'number')
   27      def name_get(self):
   28          return [(r.id, (r.number or _('Voucher'))) for r in self]
   29  
   30      @api.one
   31:     @api.depends('journal_id', 'company_id')
   32      def _get_journal_currency(self):
   33          self.currency_id = self.journal_id.currency_id.id or self.company_id.currency_id.id
   ..
   44  
   45      @api.multi
   46:     @api.depends('tax_correction', 'line_ids.price_subtotal')
   47      def _compute_total(self):
   48          for voucher in self:
   ..
   57  
   58      @api.one
   59:     @api.depends('account_pay_now_id', 'account_pay_later_id', 'pay_now')
   60      def _get_account(self):
   61          self.account_id = self.account_pay_now_id if self.pay_now == 'pay_now' else self.account_pay_later_id
   ..
  304  
  305      @api.one
  306:     @api.depends('price_unit', 'tax_ids', 'quantity', 'product_id', 'voucher_id.currency_id')
  307      def _compute_subtotal(self):
  308          self.price_subtotal = self.quantity * self.price_unit

/home/shivamm/Desktop/odoo-9.0/addons/base_iban/base_iban.py:
   45  
   46      @api.one
   47:     @api.depends('acc_number')
   48      def _compute_acc_type(self):
   49          try:

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_carrier.py:
   53      shipping_enabled = fields.Boolean(string="Shipping enabled", default=True, help="Uncheck this box to disable package shipping while validating Delivery Orders")
   54  
   55:     @api.depends('product_id.list_price', 'product_id.product_tmpl_id.list_price')
   56      def _compute_fixed_price(self):
   57          for carrier in self:

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_price_rule.py:
   11      _order = 'sequence, list_price'
   12  
   13:     @api.depends('variable', 'operator', 'max_value', 'list_base_price', 'list_price', 'variable_factor')
   14      def _get_name(self):
   15          for rule in self:

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/sale_order.py:
   13      invoice_shipping_on_delivery = fields.Boolean(string="Invoice Shipping on Delivery")
   14  
   15:     @api.depends('carrier_id', 'partner_id', 'order_line')
   16      def _compute_delivery_price(self):
   17          for order in self:

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/stock_move.py:
   17      weight_uom_id = fields.Many2one('product.uom', string='Unit of Measure', required=True, readonly=True, help="Unit of Measure (Unit of Measure) is the unit of measurement for Weight", default=_default_uom)
   18  
   19:     @api.depends('product_id', 'product_uom_qty', 'product_uom')
   20      def _cal_move_weight(self):
   21          for move in self.filtered(lambda moves: moves.product_id.weight > 0.00):

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/stock_picking.py:
   11  
   12      @api.one
   13:     @api.depends('quant_ids', 'children_ids')
   14      def _compute_weight(self):
   15          weight = 0
   ..
   32  
   33      @api.one
   34:     @api.depends('pack_operation_ids')
   35      def _compute_packages(self):
   36          self.ensure_one()
   ..
   44  
   45      @api.one
   46:     @api.depends('pack_operation_ids')
   47      def _compute_bulk_weight(self):
   48          weight = 0.0
   ..
   64      weight_bulk = fields.Float('Bulk Weight', compute='_compute_bulk_weight')
   65  
   66:     @api.depends('product_id', 'move_lines')
   67      def _cal_weight(self):
   68          for picking in self:

/home/shivamm/Desktop/odoo-9.0/addons/engineer/models.py:
   11  #     description = fields.Text()
   12  #
   13: #     @api.depends('value')
   14  #     def _value_pc(self):
   15  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
   87  
   88      @api.multi
   89:     @api.depends('seats_max', 'registration_ids.state')
   90      def _compute_seats(self):
   91          """ Determine reserved, available, reserved but unconfirmed and used seats. """
   ..
  135  
  136      @api.one
  137:     @api.depends('date_tz', 'date_begin')
  138      def _compute_date_begin_tz(self):
  139          if self.date_begin:
  ...
  145  
  146      @api.one
  147:     @api.depends('date_tz', 'date_end')
  148      def _compute_date_end_tz(self):
  149          if self.date_end:
  ...
  183  
  184      @api.multi
  185:     @api.depends('name', 'date_begin', 'date_end')
  186      def name_get(self):
  187          result = []

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event_mail.py:
   45  
   46      @api.one
   47:     @api.depends('mail_sent', 'interval_type', 'event_id.registration_ids', 'mail_registration_ids')
   48      def _compute_done(self):
   49          if self.interval_type in ['before_event', 'after_event']:
   ..
   53  
   54      @api.one
   55:     @api.depends('event_id.state', 'event_id.date_begin', 'interval_type', 'interval_unit', 'interval_nbr')
   56      def _compute_scheduled_date(self):
   57          if self.event_id.state not in ['confirm', 'done']:
   ..
  112  
  113      @api.one
  114:     @api.depends('registration_id', 'scheduler_id.interval_unit', 'scheduler_id.interval_type')
  115      def _compute_scheduled_date(self):
  116          if self.registration_id:

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
   51  
   52      @api.one
   53:     @api.depends('deadline')
   54      def _is_expired(self):
   55          if self.deadline:
   ..
   65                                  digits=dp.get_precision('Product Price'))
   66      @api.one
   67:     @api.depends('price', 'product_id.lst_price', 'product_id.price')
   68      def _get_price_reduce(self):
   69          product = self.product_id
   ..
   97  
   98      @api.multi
   99:     @api.depends('seats_max', 'registration_ids.state')
  100      def _compute_seats(self):
  101          """ Determine reserved, available, reserved but unconfirmed and used seats. """

/home/shivamm/Desktop/odoo-9.0/addons/exam/models/exam.py:
  145  
  146      @api.one
  147:     @api.depends('result_ids')
  148      def _compute_total(self):
  149          total = 0.0
  ...
  184  
  185      @api.one
  186:     @api.depends('result_ids', 'student_id')
  187      def _compute_result(self):
  188          flag = False
  ...
  344  
  345      @api.one
  346:     @api.depends('exam_id', 'obtain_marks')
  347      def _get_grade(self):
  348          if (self.exam_id and self.exam_id.student_id
  ...
  377  
  378      @api.one
  379:     @api.depends('standard_id', 'year')
  380      def compute_grade(self):
  381          fina_tot = 0
  ...
  410  
  411      @api.one
  412:     @api.depends('a_exam_id', 'obtain_marks')
  413      def _calc_result(self):
  414          if (self.a_exam_id and self.a_exam_id.subject_id

/home/shivamm/Desktop/odoo-9.0/addons/exam_test_quiz/etq_exam.py:
   27                 }        
   28         
   29:     @api.depends('name')
   30      def slug_me(self):
   31          if self.name:
   ..
   48  
   49      @api.one
   50:     @api.depends('question_options')
   51      def calc_options(self):
   52          self.num_options = self.question_options.search_count([('question_id','=',self.id)])
   53      
   54      @api.one
   55:     @api.depends('question_options')
   56      def calc_correct(self):
   57          self.num_correct = self.question_options.search_count([('question_id','=',self.id), ('correct','=',True)])

/home/shivamm/Desktop/odoo-9.0/addons/hr/hr.py:
  184               "Use this field anywhere a small image is required.")
  185  
  186:     @api.depends('image')
  187      def _compute_images(self):
  188          for rec in self:

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
   26  
   27      @api.one
   28:     @api.depends('equipment_ids')
   29      def _compute_fold(self):
   30          self.fold = False if self.equipment_count else True
   ..
  132  
  133      @api.one
  134:     @api.depends('maintenance_ids.stage_id.done')
  135      def _compute_maintenance_count(self):
  136          self.maintenance_count = len(self.maintenance_ids)

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/models/hr_expense.py:
   45          \nIf the manager approve it, the status is \'Approved\'.\n If the accountant genrate the accounting entries for the expense request, the status is \'Waiting Payment\'.')
   46  
   47:     @api.depends('quantity', 'unit_amount', 'tax_ids', 'currency_id')
   48      def _compute_amount(self):
   49          for expense in self:

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_recruitment.py:
  149      attachment_ids = fields.One2many('ir.attachment', 'res_id', domain=[('res_model', '=', 'hr.applicant')], string='Attachments')
  150  
  151:     @api.depends('date_open', 'date_closed')
  152      @api.one
  153      def _compute_day(self):

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/im_livechat_channel.py:
   68  
   69      @api.one
   70:     @api.depends('image')
   71      def _compute_image(self):
   72          self.image_medium = tools.image_resize_image_medium(self.image)
   ..
   91  
   92      @api.multi
   93:     @api.depends('channel_ids')
   94      def _compute_nbr_channel(self):
   95          for record in self:
   ..
   97  
   98      @api.multi
   99:     @api.depends('channel_ids.rating_ids')
  100      def _compute_percentage_satisfaction(self):
  101          for record in self:

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/rating.py:
    8  
    9      @api.one
   10:     @api.depends('res_model', 'res_id')
   11      def _compute_res_name(self):
   12          # cannot change the rec_name of session since it is use to create the bus channel

/home/shivamm/Desktop/odoo-9.0/addons/link_tracker/models/link_tracker.py:
   67  
   68      @api.one
   69:     @api.depends('link_click_ids.link_id')
   70      def _compute_count(self):
   71          self.count = len(self.link_click_ids)
   72  
   73      @api.one
   74:     @api.depends('code')
   75      def _compute_short_url(self):
   76          base_url = self.env['ir.config_parameter'].get_param('web.base.url')
   ..
   87  
   88      @api.one
   89:     @api.depends('favicon')
   90      def _compute_icon_src(self):
   91          self.icon_src = 'data:image/png;base64,' + self.favicon
   92  
   93      @api.one
   94:     @api.depends('url')
   95      def _compute_redirected_url(self):
   96          parsed = urlparse(self.url)
   ..
  105  
  106      @api.model
  107:     @api.depends('url')
  108      def _get_title_from_url(self, url):
  109          try:
  ...
  117  
  118      @api.one
  119:     @api.depends('url')
  120      def _compute_favicon(self):
  121          try:

/home/shivamm/Desktop/odoo-9.0/addons/lunch/models/lunch.py:
   50  
   51      @api.one
   52:     @api.depends('order_line_ids')
   53      def _compute_total(self):
   54          """
   ..
   62          return [(order.id, '%s %s' % (_('Lunch Order'), '#%d' % order.id)) for order in self]
   63  
   64:     @api.depends('state')
   65      def _compute_alerts_get(self):
   66          """
   ..
   74              self.alerts = alert_msg and '\n'.join(alert_msg) or False
   75  
   76:     @api.depends('user_id')
   77      def _compute_previous_order_ids(self):
   78          self.previous_order_ids = self._default_previous_order_ids()
   79  
   80      @api.one
   81:     @api.depends('user_id')
   82      def _compute_cash_move_balance(self):
   83          domain = [('user_id', '=', self.user_id.id)]
   ..
   99  
  100      @api.one
  101:     @api.depends('order_line_ids.state')
  102      def _compute_order_state(self):
  103          """

/home/shivamm/Desktop/odoo-9.0/addons/lunch2/models.py:
   11  #     description = fields.Text()
   12  #
   13: #     @api.depends('value')
   14  #     def _value_pc(self):
   15  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_channel.py:
   85  
   86      @api.one
   87:     @api.depends('image')
   88      def _get_image(self):
   89          self.image_medium = tools.image_resize_image_medium(self.image)

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_message.py:
  125          return [('needaction_partner_ids', 'not in', self.env.user.partner_id.id)]
  126  
  127:     @api.depends('starred_partner_ids')
  128      def _get_starred(self):
  129          """ Compute if the message is starred by the current user. """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_thread.py:
  114  
  115      @api.one
  116:     @api.depends('message_follower_ids')
  117      def _get_followers(self):
  118          self.message_partner_ids = self.message_follower_ids.mapped('partner_id')
  ...
  146  
  147      @api.multi
  148:     @api.depends('message_follower_ids')
  149      def _compute_is_follower(self):
  150          followers = self.env['mail.followers'].sudo().search([

/home/shivamm/Desktop/odoo-9.0/addons/my_proroject/models.py:
   10  	description = fields.Text()
   11  
   12: 	@api.depends('value')
   13  	def _value_pc(self):
   14  		self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/my_proroject/user.py:
   13  
   14  
   15: 	@api.depends('a','b')
   16  	def _value_pc(self):
   17  		self.c = float(self.a+self.b)

/home/shivamm/Desktop/odoo-9.0/addons/new/models.py:
   18  #     description = fields.Text()
   19  #
   20: #     @api.depends('value')
   21  #     def _value_pc(self):
   22  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/models/attendance_sheet.py:
   27  
   28      @api.one
   29:     @api.depends('attendance_line.present')
   30      def _total_present(self):
   31          self.total_present = len(self.attendance_line.filtered(
   ..
   33  
   34      @api.one
   35:     @api.depends('attendance_line.present')
   36      def _total_absent(self):
   37          self.total_absent = len(self.attendance_line.filtered(

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/student.py:
   29  
   30      @api.one
   31:     @api.depends('roll_number_line', 'batch_id', 'course_id')
   32      def _get_curr_roll_number(self):
   33          # TO_DO:: Improve the logic by adding sequence field in course.

/home/shivamm/Desktop/odoo-9.0/addons/pos_cache/models/pos_cache.py:
   55  
   56      @api.one
   57:     @api.depends('cache_ids')
   58      def _get_oldest_cache_time(self):
   59          pos_cache = self.env['pos.cache']

/home/shivamm/Desktop/odoo-9.0/addons/product/pricelist.py:
  326  
  327      @api.one
  328:     @api.depends('categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
  329          'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge')
  330      def _get_pricelist_item_name_price(self):

/home/shivamm/Desktop/odoo-9.0/addons/product/product.py:
  531               "Use this field anywhere a small image is required.")
  532  
  533:     @api.depends('image')
  534      def _compute_images(self):
  535          for rec in self:

/home/shivamm/Desktop/odoo-9.0/addons/programmer/models.py:
   13  #	description = fields.Text()
   14  #
   15: #     @api.depends('value')
   16  #     def _value_pc(self):
   17  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/purchase/purchase.py:
   17      _order = 'date_order desc, id desc'
   18  
   19:     @api.depends('order_line.price_total')
   20      def _amount_all(self):
   21          for order in self:
   ..
   35              order.order_line.write({'date_planned': self.date_planned})
   36  
   37:     @api.depends('order_line.date_planned')
   38      def _compute_date_planned(self):
   39          for order in self:
   ..
   45                  order.date_planned = min_date
   46  
   47:     @api.depends('state', 'order_line.qty_invoiced', 'order_line.product_qty')
   48      def _get_invoiced(self):
   49          precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
   ..
   60                  order.invoice_status = 'no'
   61  
   62:     @api.depends('order_line.invoice_lines.invoice_id.state')
   63      def _compute_invoice(self):
   64          for order in self:
   ..
   78          return types[0].id if types else False
   79  
   80:     @api.depends('order_line.move_ids.picking_id')
   81      def _compute_picking(self):
   82          for order in self:
   ..
  162  
  163      @api.multi
  164:     @api.depends('name', 'partner_ref')
  165      def name_get(self):
  166          result = []
  ...
  408      _description = 'Purchase Order Line'
  409  
  410:     @api.depends('product_qty', 'price_unit', 'taxes_id')
  411      def _compute_amount(self):
  412          for line in self:
  ...
  418              })
  419  
  420:     @api.depends('invoice_lines.invoice_id.state')
  421      def _compute_qty_invoiced(self):
  422          for line in self:
  ...
  426              line.qty_invoiced = qty
  427  
  428:     @api.depends('order_id.state', 'move_ids.state')
  429      def _compute_qty_received(self):
  430          for line in self:

/home/shivamm/Desktop/odoo-9.0/addons/rating/models/rating.py:
   14  
   15      @api.one
   16:     @api.depends('res_model', 'res_id')
   17      def _compute_res_name(self):
   18          name = self.env[self.res_model].sudo().browse(self.res_id).name_get()

/home/shivamm/Desktop/odoo-9.0/addons/rating_project/models/project.py:
   39  
   40      @api.one
   41:     @api.depends('percentage_satisfaction_task')
   42      def _compute_percentage_satisfaction_project(self):
   43          self.percentage_satisfaction_project = self.percentage_satisfaction_task
   44  
   45      @api.one
   46:     @api.depends('tasks.rating_ids.rating')
   47      def _compute_percentage_satisfaction_task(self):
   48          activity = self.tasks.rating_get_grades()

/home/shivamm/Desktop/odoo-9.0/addons/rating_project_issue/models/project_issue.py:
   25  
   26      @api.multi
   27:     @api.depends('percentage_satisfaction_task', 'percentage_satisfaction_issue')
   28      def _compute_percentage_satisfaction_project(self):
   29          super(Project, self)._compute_percentage_satisfaction_project()
   ..
   63  
   64      @api.one
   65:     @api.depends('issue_ids.rating_ids.rating')
   66      def _compute_percentage_satisfaction_issue(self):
   67          project_issue = self.env['project.issue'].search([('project_id', '=', self.id)])

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale.py:
   21      _order = 'date_order desc, id desc'
   22  
   23:     @api.depends('order_line.price_total')
   24      def _amount_all(self):
   25          """
   ..
   37              })
   38  
   39:     @api.depends('state', 'order_line.invoice_status')
   40      def _get_invoiced(self):
   41          """
   ..
  416      _order = 'order_id desc, sequence, id'
  417  
  418:     @api.depends('state', 'product_uom_qty', 'qty_delivered', 'qty_to_invoice', 'qty_invoiced')
  419      def _compute_invoice_status(self):
  420          """
  ...
  445                  line.invoice_status = 'no'
  446  
  447:     @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
  448      def _compute_amount(self):
  449          """
  ...
  459              })
  460  
  461:     @api.depends('product_id.invoice_policy', 'order_id.state')
  462      def _compute_qty_delivered_updateable(self):
  463          for line in self:
  464              line.qty_delivered_updateable = line.product_id.invoice_policy in ('order', 'delivery') and line.order_id.state == 'sale' and line.product_id.track_service == 'manual'
  465  
  466:     @api.depends('qty_invoiced', 'qty_delivered', 'product_uom_qty', 'order_id.state')
  467      def _get_to_invoice_qty(self):
  468          """
  ...
  479                  line.qty_to_invoice = 0
  480  
  481:     @api.depends('invoice_lines.invoice_id.state', 'invoice_lines.quantity')
  482      def _get_invoice_qty(self):
  483          """
  ...
  495              line.qty_invoiced = qty_invoiced
  496  
  497:     @api.depends('price_subtotal', 'product_uom_qty')
  498      def _get_price_reduce(self):
  499          for line in self:
  ...
  825  
  826      @api.multi
  827:     @api.depends('product_variant_ids.sales_count')
  828      def _sales_count(self):
  829          for product in self:

/home/shivamm/Desktop/odoo-9.0/addons/sale_crm/crm_lead.py:
    9  
   10      @api.one
   11:     @api.depends('order_ids')
   12      def _get_sale_amount_total(self):
   13          total = 0.0

/home/shivamm/Desktop/odoo-9.0/addons/sale_service/models/timesheet.py:
   13  
   14      @api.multi
   15:     @api.depends('order_line.product_id.project_id')
   16      def _compute_tasks_ids(self):
   17          for order in self:

/home/shivamm/Desktop/odoo-9.0/addons/sale_stock/sale_stock.py:
   29  
   30      @api.multi
   31:     @api.depends('procurement_group_id')
   32      def _compute_picking_ids(self):
   33          for order in self:
   ..
   96  
   97      @api.multi
   98:     @api.depends('product_id')
   99      def _compute_qty_delivered_updateable(self):
  100          for line in self:
  ...
  243      _inherit = 'stock.picking'
  244  
  245:     @api.depends('move_lines')
  246      def _compute_sale_id(self):
  247          for picking in self:

/home/shivamm/Desktop/odoo-9.0/addons/sale_timesheet/models/sale_timesheet.py:
   81  
   82      @api.multi
   83:     @api.depends('project_id.line_ids')
   84      def _compute_timesheet_ids(self):
   85          for order in self:

/home/shivamm/Desktop/odoo-9.0/addons/shivam/models.py:
   11  #     description = fields.Text()
   12  #
   13: #     @api.depends('value')
   14  #     def _value_pc(self):
   15  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/test/models.py:
   27  #     description = fields.Text()
   28  #
   29: #     @api.depends('value')
   30  #     def _value_pc(self):
   31  #         self.value2 = float(self.value) / 100

/home/shivamm/Desktop/odoo-9.0/addons/web_tip/web_tip.py:
    9  
   10      @api.one
   11:     @api.depends('user_ids')
   12      def _is_consumed(self):
   13          self.is_consumed = self.env.user in self.user_ids

/home/shivamm/Desktop/odoo-9.0/addons/website_event/models/event.py:
   25  
   26      @api.multi
   27:     @api.depends('name')
   28      def _website_url(self, name, arg):
   29          res = super(event, self)._website_url(name, arg)

/home/shivamm/Desktop/odoo-9.0/addons/website_event_track/models/event.py:
   57  
   58      @api.one
   59:     @api.depends('speaker_ids.image')
   60      def _compute_image(self):
   61          if self.speaker_ids:
   ..
   97  
   98      @api.multi
   99:     @api.depends('name')
  100      def _website_url(self, field_name, arg):
  101          res = super(event_track, self)._website_url(field_name, arg)
  ...
  160  
  161      @api.one
  162:     @api.depends('track_ids.tag_ids')
  163      def _get_tracks_tag_ids(self):
  164          self.tracks_tag_ids = self.track_ids.mapped('tag_ids').ids

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/forum.py:
  279  
  280      @api.one
  281:     @api.depends('content')
  282      def _get_plain_content(self):
  283          self.plain_content = tools.html2plaintext(self.content)[0:500] if self.content else False
  284  
  285      @api.one
  286:     @api.depends('vote_count', 'forum_id.relevancy_post_vote', 'forum_id.relevancy_time_decay')
  287      def _compute_relevancy(self):
  288          if self.create_date:
  ...
  300  
  301      @api.multi
  302:     @api.depends('vote_ids.vote')
  303      def _get_vote_count(self):
  304          read_group_res = self.env['forum.post.vote'].read_group([('post_id', 'in', self._ids)], ['post_id', 'vote'], ['post_id', 'vote'], lazy=False)
  ...
  314  
  315      @api.one
  316:     @api.depends('favourite_ids')
  317      def _get_favorite_count(self):
  318          self.favourite_count = len(self.favourite_ids)
  319  
  320      @api.one
  321:     @api.depends('create_uid', 'parent_id')
  322      def _is_self_reply(self):
  323          self.self_reply = self.parent_id.create_uid.id == self._uid
  324  
  325      @api.one
  326:     @api.depends('child_ids.create_uid', 'website_message_ids')
  327      def _get_child_count(self):
  328          def process(node):
  ...
  338  
  339      @api.one
  340:     @api.depends('child_ids.is_correct')
  341      def _get_has_validated_answer(self):
  342          self.has_validated_answer = any(answer.is_correct for answer in self.child_ids)
  ...
  439  
  440      @api.multi
  441:     @api.depends('name', 'post_type')
  442      def name_get(self):
  443          result = []
  ...
  833  
  834      @api.multi
  835:     @api.depends("post_ids.tag_ids")
  836      def _get_posts_count(self):
  837          for tag in self:

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/res_users.py:
   27  
   28      @api.multi
   29:     @api.depends('badge_ids')
   30      def _get_user_badge_level(self):
   31          """ Return total badge per level of users

/home/shivamm/Desktop/odoo-9.0/addons/website_hr_recruitment/models/hr_recruitment_source.py:
    8      _inherit = 'hr.recruitment.source'
    9  
   10:     @api.depends('source_id', 'source_id.name', 'job_id')
   11      @api.one
   12      def _compute_url(self):

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/slides.py:
   45      promoted_slide_id = fields.Many2one('slide.slide', string='Featured Slide', compute='_compute_promoted_slide_id', store=True)
   46  
   47:     @api.depends('custom_slide_id', 'promote_strategy', 'slide_ids.likes',
   48                   'slide_ids.total_views', "slide_ids.date_published")
   49      def _compute_promoted_slide_id(self):
   ..
   65      total = fields.Integer(compute='_count_presentations', store=True)
   66  
   67:     @api.depends('slide_ids.slide_type', 'slide_ids.website_published')
   68      def _count_presentations(self):
   69          result = dict.fromkeys(self.ids, dict())
   ..
  109  
  110      @api.one
  111:     @api.depends('visibility', 'group_ids', 'upload_group_ids')
  112      def _compute_access(self):
  113          self.can_see = self.visibility in ['public', 'private'] or bool(self.group_ids & self.env.user.groups_id)
  ...
  116  
  117      @api.multi
  118:     @api.depends('name')
  119      def _website_url(self, name, arg):
  120          res = super(Channel, self)._website_url(name, arg)
  ...
  145      total = fields.Integer(compute='_count_presentations', store=True)
  146  
  147:     @api.depends('slide_ids.slide_type', 'slide_ids.website_published')
  148      def _count_presentations(self):
  149          result = dict.fromkeys(self.ids, dict())
  ...
  236      image_thumb = fields.Binary('Thumbnail', compute="_get_image", store=True, attachment=True)
  237  
  238:     @api.depends('image')
  239      def _get_image(self):
  240          for record in self:
  ...
  288      total_views = fields.Integer("Total # Views", default="0", compute='_compute_total', store=True)
  289  
  290:     @api.depends('slide_views', 'embed_views')
  291      def _compute_total(self):
  292          for record in self:
  ...
  311  
  312      @api.multi
  313:     @api.depends('name')
  314      def _website_url(self, name, arg):
  315          res = super(Slide, self)._website_url(name, arg)

160 matches across 64 files
