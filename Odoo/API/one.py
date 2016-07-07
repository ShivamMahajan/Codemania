Searching 18994 files for "@api.one"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
  147          return result
  148  
  149:     @api.one
  150      def copy(self, default=None):
  151          default = dict(default or {})
  ...
  252      ]
  253  
  254:     @api.one
  255      @api.constrains('currency_id', 'default_credit_account_id', 'default_debit_account_id')
  256      def _check_currency(self):
  ...
  261                  raise UserError(_('Configuration error!\nThe currency of the journal should be the same than the default debit account.'))
  262  
  263:     @api.one
  264      @api.constrains('type', 'bank_account_id')
  265      def _check_bank_account(self):
  ...
  289          return ret
  290  
  291:     @api.one
  292      def copy(self, default=None):
  293          default = dict(default or {})
  ...
  463          help="The accounting journal corresponding to this bank account.")
  464  
  465:     @api.one
  466      @api.constrains('journal_id')
  467      def _check_journal_id(self):
  ...
  518      ]
  519  
  520:     @api.one
  521      @api.constrains('children_tax_ids', 'type_tax_use')
  522      def _check_children_scope(self):
  ...
  524              raise UserError(_('The application scope of taxes in a group must be either the same as the group or "None".'))
  525  
  526:     @api.one
  527      def copy(self, default=None):
  528          default = dict(default or {}, name=_("%s (Copy)") % self.name)

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
   18      _order = 'coin_value'
   19  
   20:     @api.one
   21      @api.depends('coin_value', 'number')
   22      def _sub_total(self):
   ..
   73  class AccountBankStatement(models.Model):
   74  
   75:     @api.one
   76      @api.depends('line_ids', 'balance_start', 'line_ids.amount', 'balance_end_real')
   77      def _end_balance(self):
   ..
   80          self.difference = self.balance_end_real - self.balance_end
   81  
   82:     @api.one
   83      @api.depends('journal_id')
   84      def _compute_currency(self):
   85          self.currency_id = self.journal_id.currency_id or self.env.user.company_id.currency_id
   86  
   87:     @api.one
   88      @api.depends('line_ids.journal_entry_ids')
   89      def _check_lines_reconciled(self):
   ..
  379      currency_id = fields.Many2one('res.currency', string='Currency', help="The optional other currency if it is a multi-currency entry.")
  380  
  381:     @api.one
  382      @api.constrains('amount')
  383      def _check_amount(self):
  ...
  387              raise ValidationError(_('A transaction can\'t have a 0 amount.'))
  388  
  389:     @api.one
  390      @api.constrains('amount', 'amount_currency')
  391      def _check_amount_currency(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
   39      _order = "date_invoice desc, number desc, id desc"
   40  
   41:     @api.one
   42      @api.depends('invoice_line_ids.price_subtotal', 'tax_line_ids.amount', 'currency_id', 'company_id')
   43      def _compute_amount(self):
   ..
   75          return [('none', _('Free Reference'))]
   76  
   77:     @api.one
   78      @api.depends(
   79          'state', 'currency_id', 'invoice_line_ids.price_subtotal',
   ..
   99              self.reconciled = True
  100  
  101:     @api.one
  102      def _get_outstanding_info_JSON(self):
  103          self.outstanding_credits_debits_widget = json.dumps(False)
  ...
  131                  self.has_outstanding = True
  132  
  133:     @api.one
  134      @api.depends('payment_move_line_ids.amount_residual')
  135      def _get_payment_info_JSON(self):
  ...
  167              self.payments_widget = json.dumps(info)
  168  
  169:     @api.one
  170      @api.depends('move_id.line_ids.amount_residual')
  171      def _compute_payments(self):
  ...
  992          }
  993  
  994:     @api.one
  995      @api.depends('price_unit', 'discount', 'invoice_line_tax_ids', 'quantity',
  996          'product_id', 'invoice_id.partner_id', 'invoice_id.currency_id', 'invoice_id.company_id')
  ...
 1201  
 1202      @api.constrains('line_ids')
 1203:     @api.one
 1204      def _check_lines(self):
 1205          payment_term_lines = self.line_ids.sorted()
 ....
 1210              raise ValidationError(_('A Payment Term should have only one line of type Balance.'))
 1211  
 1212:     @api.one
 1213      def compute(self, value, date_ref=False):
 1214          date_ref = date_ref or fields.Date.today()
 ....
 1268      sequence = fields.Integer(default=10, help="Gives the sequence order when displaying a list of payment term lines.")
 1269  
 1270:     @api.one
 1271      @api.constrains('value', 'value_amount')
 1272      def _check_percent(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_journal_dashboard.py:
   11      _inherit = "account.journal"
   12  
   13:     @api.one
   14      def _kanban_dashboard(self):
   15          self.kanban_dashboard = json.dumps(self.get_journal_dashboard_datas())
   16  
   17:     @api.one
   18      def _kanban_dashboard_graph(self):
   19          if (self.type in ['sale', 'purchase']):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_move.py:
   60                  move.matched_percentage = total_reconciled / total_amount
   61  
   62:     @api.one
   63      @api.depends('company_id')
   64      def _compute_currency(self):
   ..
  300              move_line.balance_cash_basis = move_line.debit_cash_basis - move_line.credit_cash_basis
  301  
  302:     @api.one
  303      @api.depends('move_id.line_ids')
  304      def _get_counterpart(self):
  ...
 1078                  self.env['account.analytic.line'].create(vals_line)
 1079  
 1080:     @api.one
 1081      def _prepare_analytic_line(self):
 1082          """ Prepare the values used to create() an account.analytic.line upon validation of an account.move.line having

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
   49          help="Technical field used to hide the payment method if the selected journal has only one available which is 'manual'")
   50  
   51:     @api.one
   52      @api.constrains('amount')
   53      def _check_amount(self):
   ..
   55              raise ValidationError('The payment amount must be strictly positive.')
   56  
   57:     @api.one
   58      @api.depends('payment_type', 'journal_id')
   59      def _compute_hide_payment_method(self):
   ..
  166      _order = "payment_date desc, name desc"
  167  
  168:     @api.one
  169      @api.depends('invoice_ids')
  170      def _get_has_invoices(self):
  171          self.has_invoices = bool(self.invoice_ids)
  172  
  173:     @api.one
  174      @api.depends('invoice_ids', 'amount', 'payment_date', 'currency_id')
  175      def _compute_payment_difference(self):
  ...
  200      move_line_ids = fields.One2many('account.move.line', 'payment_id', readonly=True, copy=False, ondelete='restrict')
  201  
  202:     @api.one
  203      @api.depends('invoice_ids', 'payment_type', 'partner_type', 'partner_id')
  204      def _compute_destination_account_id(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/chart_template.py:
   92      property_stock_valuation_account_id = fields.Many2one('account.account.template', string="Account Template for Stock Valuation")
   93  
   94:     @api.one
   95      def try_loading_for_current_company(self):
   96          self.ensure_one()
   ..
  662          return res
  663  
  664:     @api.one
  665      def _create_tax_templates_from_rates(self, company_id):
  666          '''

/home/shivamm/Desktop/odoo-9.0/addons/account/models/partner.py:
   34      states_count = fields.Integer(compute='_compute_states_count')
   35  
   36:     @api.one
   37      def _compute_states_count(self):
   38          self.states_count = len(self.country_id.state_ids)
   39  
   40:     @api.one
   41      @api.constrains('zip_from', 'zip_to')
   42      def _check_zip(self):
   ..
  360              partner.issued_total = issued_total
  361  
  362:     @api.one
  363      def _compute_has_unreconciled_entries(self):
  364          # Avoid useless work if has_unreconciled_entries is not relevant for this partner
  ...
  400          return self.write({'last_time_entries_checked': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)})
  401  
  402:     @api.one
  403      def _get_company_currency(self):
  404          if self.company_id:

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_invoice_refund.py:
   29  
   30      @api.depends('date_invoice')
   31:     @api.one
   32      def _get_refund_only(self):
   33          invoice_id = self.env['account.invoice'].browse(self._context.get('active_id',False))

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/pos_box.py:
   31          return {}
   32  
   33:     @api.one
   34      def _create_bank_statement_line(self, record):
   35          if record.state == 'confirm':
   ..
   44      ref = fields.Char('Reference')
   45  
   46:     @api.one
   47      def _calculate_values_for_statement_line(self, record):
   48          if not record.journal_id.company_id.transfer_account_id:
   ..
   62      _name = 'cash.box.out'
   63  
   64:     @api.one
   65      def _calculate_values_for_statement_line(self, record):
   66          if not record.journal_id.company_id.transfer_account_id:

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
  291          self.write({'state': 'draft'})
  292  
  293:     @api.one
  294      @api.depends('value', 'salvage_value', 'depreciation_line_ids')
  295      def _amount_residual(self):
  ...
  310              asset.entry_count = self.env['account.move'].search_count([('asset_id', '=', asset.id)])
  311  
  312:     @api.one
  313      @api.constrains('prorata', 'method_time')
  314      def _check_prorata(self):
  ...
  399      move_check = fields.Boolean(compute='_get_move_check', string='Posted', track_visibility='always', store=True)
  400  
  401:     @api.one
  402      @api.depends('move_id')
  403      def _get_move_check(self):

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset_invoice.py:
   27      asset_mrr = fields.Float(string='Monthly Recurring Revenue', compute='_get_asset_date', readonly=True, digits=dp.get_precision('Account'), store=True)
   28  
   29:     @api.one
   30      @api.depends('asset_category_id', 'invoice_id.date_invoice')
   31      def _get_asset_date(self):
   ..
   44                  self.asset_end_date = end_date.strftime(DF)
   45  
   46:     @api.one
   47      def asset_create(self):
   48          if self.asset_category_id and self.asset_category_id.method_number > 1:

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/wizard/account_asset_change_duration.py:
   16      asset_method_time = fields.Char(compute='_get_asset_method_time', string='Asset Method Time', readonly=True)
   17  
   18:     @api.one
   19      def _get_asset_method_time(self):
   20          if self.env.context.get('active_id'):

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_journal.py:
    7      _inherit = "account.journal"
    8  
    9:     @api.one
   10      @api.depends('outbound_payment_method_ids')
   11      def _compute_check_printing_payment_method_selected(self):
   12          self.check_printing_payment_method_selected = any(pm.code == 'check_printing' for pm in self.outbound_payment_method_ids)
   13  
   14:     @api.one
   15      @api.depends('check_manual_sequencing')
   16      def _get_check_next_number(self):
   ..
   20              self.check_next_number = 1
   21  
   22:     @api.one
   23      def _set_check_next_number(self):
   24          if self.check_next_number < self.check_sequence_id.number_next_actual:
   ..
   44          return rec
   45  
   46:     @api.one
   47      def copy(self, default=None):
   48          rec = super(AccountJournal, self).copy(default)
   ..
   50          return rec
   51  
   52:     @api.one
   53      def _create_check_sequence(self):
   54          """ Create a check sequence for the journal """

/home/shivamm/Desktop/odoo-9.0/addons/account_voucher/account_voucher.py:
   11  class AccountVoucher(models.Model):
   12  
   13:     @api.one
   14      @api.depends('move_id.line_ids.reconciled', 'move_id.line_ids.account_id.internal_type')
   15      def _check_paid(self):
   ..
   28          return [(r.id, (r.number or _('Voucher'))) for r in self]
   29  
   30:     @api.one
   31      @api.depends('journal_id', 'company_id')
   32      def _get_journal_currency(self):
   ..
   56              voucher.tax_amount = tax_amount
   57  
   58:     @api.one
   59      @api.depends('account_pay_now_id', 'account_pay_later_id', 'pay_now')
   60      def _get_account(self):
   ..
  303      _description = 'Voucher Lines'
  304  
  305:     @api.one
  306      @api.depends('price_unit', 'tax_ids', 'quantity', 'product_id', 'voucher_id.currency_id')
  307      def _compute_subtotal(self):

/home/shivamm/Desktop/odoo-9.0/addons/barcodes/barcodes.py:
  208      }
  209  
  210:     @api.one
  211      @api.constrains('pattern')
  212      def _check_pattern(self):

/home/shivamm/Desktop/odoo-9.0/addons/base_iban/base_iban.py:
   44      _inherit = "res.partner.bank"
   45  
   46:     @api.one
   47      @api.depends('acc_number')
   48      def _compute_acc_type(self):
   ..
   70          return super(ResPartnerBank, self).write(vals)
   71  
   72:     @api.one
   73      @api.constrains('acc_number')
   74      def _check_iban(self):

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_carrier.py:
   62              carrier.product_id.list_price = carrier.fixed_price
   63  
   64:     @api.one
   65      def get_price(self):
   66          SaleOrder = self.env['sale.order']

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/stock_picking.py:
   10      _inherit = "stock.quant.package"
   11  
   12:     @api.one
   13      @api.depends('quant_ids', 'children_ids')
   14      def _compute_weight(self):
   ..
   31          return self.env['product.uom'].search([('category_id', '=', uom_categ_id), ('factor', '=', 1)], limit=1)
   32  
   33:     @api.one
   34      @api.depends('pack_operation_ids')
   35      def _compute_packages(self):
   ..
   43          self.package_ids = list(packs)
   44  
   45:     @api.one
   46      @api.depends('pack_operation_ids')
   47      def _compute_bulk_weight(self):
   ..
  107          return client_action
  108  
  109:     @api.one
  110      def cancel_shipment(self):
  111          self.carrier_id.cancel_shipment(self)

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
  134          return [(x, x) for x in pytz.all_timezones]
  135  
  136:     @api.one
  137      @api.depends('date_tz', 'date_begin')
  138      def _compute_date_begin_tz(self):
  ...
  144              self.date_begin_located = False
  145  
  146:     @api.one
  147      @api.depends('date_tz', 'date_end')
  148      def _compute_date_end_tz(self):
  ...
  161      auto_confirm = fields.Boolean(string='Confirmation not required', compute='_compute_auto_confirm')
  162  
  163:     @api.one
  164      def _compute_auto_confirm(self):
  165          self.auto_confirm = self.env['ir.values'].get_default('event.config.settings', 'auto_confirmation')
  ...
  192          return result
  193  
  194:     @api.one
  195      @api.constrains('seats_max', 'seats_available')
  196      def _check_seats_limit(self):
  ...
  198              raise UserError(_('No more available seats.'))
  199  
  200:     @api.one
  201      @api.constrains('date_begin', 'date_end')
  202      def _check_closing_date(self):
  ...
  220          return res
  221  
  222:     @api.one
  223      def button_draft(self):
  224          self.state = 'draft'
  225  
  226:     @api.one
  227      def button_cancel(self):
  228          for event_reg in self.registration_ids:
  ...
  232          self.state = 'cancel'
  233  
  234:     @api.one
  235      def button_done(self):
  236          self.state = 'done'
  237  
  238:     @api.one
  239      def button_confirm(self):
  240          self.state = 'confirm'
  ...
  256          return res
  257  
  258:     @api.one
  259      def mail_attendees(self, template_id, force_send=False, filter_func=lambda self: True):
  260          for attendee in self.registration_ids.filtered(filter_func):
  ...
  292      name = fields.Char(string='Attendee Name', select=True)
  293  
  294:     @api.one
  295      @api.constrains('event_id', 'state')
  296      def _check_seats_limit(self):
  ...
  333          return data
  334  
  335:     @api.one
  336      def do_draft(self):
  337          self.state = 'draft'
  338  
  339:     @api.one
  340      def confirm_registration(self):
  341          self.state = 'open'
  ...
  346          onsubscribe_schedulers.execute()
  347  
  348:     @api.one
  349      def button_reg_close(self):
  350          """ Close Registration """
  ...
  355              raise UserError(_("You must wait for the starting day of the event to do this action."))
  356  
  357:     @api.one
  358      def button_reg_cancel(self):
  359          self.state = 'cancel'

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event_mail.py:
   44      done = fields.Boolean('Sent', compute='_compute_done', store=True)
   45  
   46:     @api.one
   47      @api.depends('mail_sent', 'interval_type', 'event_id.registration_ids', 'mail_registration_ids')
   48      def _compute_done(self):
   ..
   52              self.done = len(self.mail_registration_ids) == len(self.event_id.registration_ids) and all(filter(lambda line: line.mail_sent, self.mail_registration_ids))
   53  
   54:     @api.one
   55      @api.depends('event_id.state', 'event_id.date_begin', 'interval_type', 'interval_unit', 'interval_nbr')
   56      def _compute_scheduled_date(self):
   ..
   67              self.scheduled_date = datetime.strptime(date, tools.DEFAULT_SERVER_DATETIME_FORMAT) + _INTERVALS[self.interval_unit](sign * self.interval_nbr)
   68  
   69:     @api.one
   70      def execute(self):
   71          if self.interval_type == 'after_sub':
   ..
  105      mail_sent = fields.Boolean('Mail Sent')
  106  
  107:     @api.one
  108      def execute(self):
  109          if self.registration_id.state in ['open', 'done'] and not self.mail_sent:
  ...
  111              self.write({'mail_sent': True})
  112  
  113:     @api.one
  114      @api.depends('registration_id', 'scheduler_id.interval_unit', 'scheduler_id.interval_type')
  115      def _compute_scheduled_date(self):

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
   50              return False
   51  
   52:     @api.one
   53      @api.depends('deadline')
   54      def _is_expired(self):
   ..
   64      price_reduce = fields.Float("Price Reduce", compute="_get_price_reduce", store=False,
   65                                  digits=dp.get_precision('Product Price'))
   66:     @api.one
   67      @api.depends('price', 'product_id.lst_price', 'product_id.price')
   68      def _get_price_reduce(self):
   ..
  125                  ticket.seats_available = ticket.seats_max - (ticket.seats_reserved + ticket.seats_used)
  126  
  127:     @api.one
  128      @api.constrains('registration_ids', 'seats_max')
  129      def _check_seats_limit(self):
  ...
  147      sale_order_line_id = fields.Many2one('sale.order.line', 'Sale Order Line', ondelete='cascade')
  148  
  149:     @api.one
  150      @api.constrains('event_ticket_id', 'state')
  151      def _check_ticket_seats_limit(self):

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/wizard/event_edit_registration.py:
   71      name = fields.Char(string='Name', select=True)
   72  
   73:     @api.one
   74      def get_registration_data(self):
   75          return {

/home/shivamm/Desktop/odoo-9.0/addons/exam/models/exam.py:
  144      _description = 'exam result Information'
  145  
  146:     @api.one
  147      @api.depends('result_ids')
  148      def _compute_total(self):
  ...
  183          return res
  184  
  185:     @api.one
  186      @api.depends('result_ids', 'student_id')
  187      def _compute_result(self):
  ...
  343                               should not extend maximum marks.'))
  344  
  345:     @api.one
  346      @api.depends('exam_id', 'obtain_marks')
  347      def _get_grade(self):
  ...
  376      _description = 'exam result Information by Batch wise'
  377  
  378:     @api.one
  379      @api.depends('standard_id', 'year')
  380      def compute_grade(self):
  ...
  409      _description = 'subject result Information'
  410  
  411:     @api.one
  412      @api.depends('a_exam_id', 'obtain_marks')
  413      def _calc_result(self):

/home/shivamm/Desktop/odoo-9.0/addons/exam_test_quiz/etq_exam.py:
   47      num_correct = fields.Integer(string="Correct Options",compute="calc_correct")
   48  
   49:     @api.one
   50      @api.depends('question_options')
   51      def calc_options(self):
   52          self.num_options = self.question_options.search_count([('question_id','=',self.id)])
   53      
   54:     @api.one
   55      @api.depends('question_options')
   56      def calc_correct(self):

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
   25      _description = 'Asset Category'
   26  
   27:     @api.one
   28      @api.depends('equipment_ids')
   29      def _compute_fold(self):
   ..
  131      maintenance_open_count = fields.Integer(compute='_compute_maintenance_count', string="Current Maintenance", store=True)
  132  
  133:     @api.one
  134      @api.depends('maintenance_ids.stage_id.done')
  135      def _compute_maintenance_count(self):

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_recruitment.py:
  150  
  151      @api.depends('date_open', 'date_closed')
  152:     @api.one
  153      def _compute_day(self):
  154          if self.date_open:

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/im_livechat_channel.py:
   63  
   64  
   65:     @api.one
   66      def _are_you_inside(self):
   67          self.are_you_inside = bool(self.env.uid in [u.id for u in self.user_ids])
   68  
   69:     @api.one
   70      @api.depends('image')
   71      def _compute_image(self):

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/rating.py:
    7      _inherit = "rating.rating"
    8  
    9:     @api.one
   10      @api.depends('res_model', 'res_id')
   11      def _compute_res_name(self):

/home/shivamm/Desktop/odoo-9.0/addons/link_tracker/models/link_tracker.py:
   66          return html
   67  
   68:     @api.one
   69      @api.depends('link_click_ids.link_id')
   70      def _compute_count(self):
   71          self.count = len(self.link_click_ids)
   72  
   73:     @api.one
   74      @api.depends('code')
   75      def _compute_short_url(self):
   ..
   77          self.short_url = urljoin(base_url, '/r/%(code)s' % {'code': self.code})
   78  
   79:     @api.one
   80      def _compute_short_url_host(self):
   81          self.short_url_host = self.env['ir.config_parameter'].get_param('web.base.url') + '/r/'
   82  
   83:     @api.one
   84      def _compute_code(self):
   85          record = self.env['link.tracker.code'].search([('link_id', '=', self.id)], limit=1, order='id DESC')
   86          self.code = record.code
   87  
   88:     @api.one
   89      @api.depends('favicon')
   90      def _compute_icon_src(self):
   91          self.icon_src = 'data:image/png;base64,' + self.favicon
   92  
   93:     @api.one
   94      @api.depends('url')
   95      def _compute_redirected_url(self):
   ..
  116          return title
  117  
  118:     @api.one
  119      @api.depends('url')
  120      def _compute_favicon(self):

/home/shivamm/Desktop/odoo-9.0/addons/lunch/models/lunch.py:
   49      balance_visible = fields.Boolean(compute='_compute_cash_move_balance', multi='cash_move_balance')
   50  
   51:     @api.one
   52      @api.depends('order_line_ids')
   53      def _compute_total(self):
   ..
   78          self.previous_order_ids = self._default_previous_order_ids()
   79  
   80:     @api.one
   81      @api.depends('user_id')
   82      def _compute_cash_move_balance(self):
   ..
   87          self.balance_visible = (self.user_id == self.env.user) or self.user_has_groups('lunch.group_lunch_manager')
   88  
   89:     @api.one
   90      @api.constrains('date')
   91      def _check_date(self):
   ..
   98              raise UserError(_('The date of your order is in the past.'))
   99  
  100:     @api.one
  101      @api.depends('order_line_ids.state')
  102      def _compute_order_state(self):
  ...
  152      currency_id = fields.Many2one('res.currency', related='order_id.currency_id')
  153  
  154:     @api.one
  155      def order(self):
  156          """
  ...
  159          self.state = 'ordered'
  160  
  161:     @api.one
  162      def confirm(self):
  163          """
  ...
  176              self.state = 'confirmed'
  177  
  178:     @api.one
  179      def cancel(self):
  180          """
  ...
  251          return [(alert.id, '%s %s' % (_('Alert'), '#%d' % alert.id)) for alert in self]
  252  
  253:     @api.one
  254      def _compute_display_get(self):
  255          """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_alias.py:
   91              record.alias_domain = alias_domain
   92  
   93:     @api.one
   94      @api.constrains('alias_defaults')
   95      def _check_alias_defaults(self):

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_channel.py:
   84          help="The email address associated with this group. New emails received will automatically create new topics.")
   85  
   86:     @api.one
   87      @api.depends('image')
   88      def _get_image(self):

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_thread.py:
  113          help="Number of messages which requires an action")
  114  
  115:     @api.one
  116      @api.depends('message_follower_ids')
  117      def _get_followers(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_activity/wizard/student_migrate_wizard.py:
   35          'op.student', string='Student(s)', required=True)
   36  
   37:     @api.one
   38      @api.constrains('course_from_id', 'course_to_id')
   39      def _check_admission_register(self):
   ..
   51                  "Can't migrate, Proceed for new admission")
   52  
   53:     @api.one
   54      @api.onchange('course_from_id')
   55      def onchange_course_id(self):
   56          self.student_ids = False
   57  
   58:     @api.one
   59      def student_migrate_forward(self):
   60          activity_type = self.env["op.activity.type"]

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission.py:
  120          self.batch_id = False
  121  
  122:     @api.one
  123      @api.constrains('register_id', 'application_date')
  124      def _check_admission_register(self):
  ...
  131                  End Date of Admission Register.")
  132  
  133:     @api.one
  134      @api.constrains('birth_date')
  135      def _check_birthdate(self):
  ...
  138                  "Birth Date can't be greater than current date!")
  139  
  140:     @api.one
  141      def confirm_in_progress(self):
  142          self.state = 'confirm'
  ...
  166          }
  167  
  168:     @api.one
  169      def enroll_student(self):
  170          total_admission = self.env['op.admission'].search_count(
  ...
  186          })
  187  
  188:     @api.one
  189      def confirm_rejected(self):
  190          self.state = 'reject'
  191  
  192:     @api.one
  193      def confirm_pending(self):
  194          self.state = 'pending'
  195  
  196:     @api.one
  197      def confirm_to_draft(self):
  198          self.state = 'draft'
  199  
  200:     @api.one
  201      def confirm_cancel(self):
  202          self.state = 'cancel'
  203  
  204:     @api.one
  205      def payment_process(self):
  206          self.state = 'fees_paid'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission_register.py:
   62          'Status',  default='draft', track_visibility='onchange')
   63  
   64:     @api.one
   65      @api.constrains('start_date', 'end_date')
   66      def check_dates(self):
   ..
   70              raise ValidationError("End Date cannot be set before Start Date.")
   71  
   72:     @api.one
   73      @api.constrains('min_count', 'max_count')
   74      def check_no_of_admission(self):
   ..
   79                  "Min Admission can't be greater than Max Admission")
   80  
   81:     @api.one
   82      def confirm_register(self):
   83          self.state = 'confirm'
   84  
   85:     @api.one
   86      def set_to_draft(self):
   87          self.state = 'draft'
   88  
   89:     @api.one
   90      def cancel_register(self):
   91          self.state = 'cancel'
   92  
   93:     @api.one
   94      def start_application(self):
   95          self.state = 'application'
   96  
   97:     @api.one
   98      def start_admission(self):
   99          self.state = 'admission'
  100  
  101:     @api.one
  102      def close_register(self):
  103          self.state = 'done'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_assignment/models/assignment.py:
   56      reviewer = fields.Many2one('op.faculty', 'Reviewer')
   57  
   58:     @api.one
   59      @api.constrains('issued_date', 'submission_date')
   60      def check_dates(self):
   ..
   69          self.batch_id = False
   70  
   71:     @api.one
   72      def act_publish(self):
   73          self.state = 'publish'
   74  
   75:     @api.one
   76      def act_finish(self):
   77          self.state = 'finish'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_assignment/models/assignment_sub_line.py:
   45      note = fields.Text('Note')
   46  
   47:     @api.one
   48      def act_draft(self):
   49          self.state = 'draft'
   50  
   51:     @api.one
   52      def act_submit(self):
   53          self.state = 'submit'
   54  
   55:     @api.one
   56      def act_accept(self):
   57          self.state = 'accept'
   58  
   59:     @api.one
   60      def act_change_req(self):
   61          self.state = 'change'
   62  
   63:     @api.one
   64      def act_reject(self):
   65          self.state = 'reject'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/models/attendance_sheet.py:
   26      _name = 'op.attendance.sheet'
   27  
   28:     @api.one
   29      @api.depends('attendance_line.present')
   30      def _total_present(self):
   ..
   32              lambda self: self.present))
   33  
   34:     @api.one
   35      @api.depends('attendance_line.present')
   36      def _total_absent(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/wizards/attendance_import.py:
   38      student_ids = fields.Many2many('op.student', string='Add Student(s)')
   39  
   40:     @api.one
   41      def confirm_student(self):
   42          for sheet in self.env.context.get('active_ids', []):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/wizards/student_attendance_wizard.py:
   32          'To Date', required=True, default=lambda self: fields.Date.today())
   33  
   34:     @api.one
   35      @api.constrains('from_date', 'to_date')
   36      def check_dates(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/batch.py:
   34      course_id = fields.Many2one('op.course', 'Course', required=True)
   35  
   36:     @api.one
   37      @api.constrains('start_date', 'end_date')
   38      def check_dates(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/faculty.py:
   53      emp_id = fields.Many2one('hr.employee', 'Employee')
   54  
   55:     @api.one
   56      @api.constrains('birth_date')
   57      def _check_birthdate(self):
   ..
   60                  "Birth Date can't be greater than current date!")
   61  
   62:     @api.one
   63      def create_employee(self):
   64          vals = {

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/student.py:
   28      _inherits = {'res.partner': 'partner_id'}
   29  
   30:     @api.one
   31      @api.depends('roll_number_line', 'batch_id', 'course_id')
   32      def _get_curr_roll_number(self):
   ..
   67      gr_no = fields.Char("GR Number", size=20)
   68  
   69:     @api.one
   70      @api.constrains('birth_date')
   71      def _check_birthdate(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/wizard/faculty_create_employee_wizard.py:
   29      user_boolean = fields.Boolean("Want to create user too ?", default=True)
   30  
   31:     @api.one
   32      def create_employee(self):
   33          active_id = self.env.context.get('active_ids', []) or []

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/wizard/faculty_create_user_wizard.py:
   35          'op.faculty', default=_get_faculties, string='Faculties')
   36  
   37:     @api.one
   38      def create_faculty_user(self):
   39          user_group = self.env.ref('openeducat_core.group_op_faculty')

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/wizard/students_create_user_wizard.py:
   35          'op.student', default=_get_students, string='Students')
   36  
   37:     @api.one
   38      def create_student_user(self):
   39          user_group = self.env.ref('openeducat_core.group_op_student')

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam.py:
   64              raise ValidationError('End Time cannot be set before Start Time.')
   65  
   66:     @api.one
   67      def act_held(self):
   68          self.state = 'held'
   69  
   70:     @api.one
   71      def act_done(self):
   72          self.state = 'done'
   73  
   74:     @api.one
   75      def act_schedule(self):
   76          self.state = 'schedule'
   77  
   78:     @api.one
   79      def act_cancel(self):
   80          self.state = 'cancel'
   81  
   82:     @api.one
   83      def act_new_exam(self):
   84          self.state = 'new'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/result_template.py:
   39      pass_status_ids = fields.Many2many('op.pass.status', string='Pass Status')
   40  
   41:     @api.one
   42      def generate_result(self):
   43          marksheet_reg_id = self.env['op.marksheet.register'].create({

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/hostel.py:
   32          'op.hostel.room', 'hostel_id', 'Room(s)')
   33  
   34:     @api.one
   35      @api.constrains('hostel_room_lines')
   36      def _check_hostel_capacity(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/hostel_room.py:
   49              self.students_per_room = self.name.capacity
   50  
   51:     @api.one
   52      @api.constrains('student_ids', 'students_per_room')
   53      def _check_student_capacity(self):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_movement.py:
   85          self.faculty_id = self.library_card_id.faculty_id.id
   86  
   87:     @api.one
   88      def issue_book(self):
   89          ''' function to issue book '''
   ..
   92              self.state = 'issue'
   93  
   94:     @api.one
   95      def calculate_penalty(self):
   96          penalty_amt = 0

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_purchase.py:
   46          default='draft', track_visibility='onchange')
   47  
   48:     @api.one
   49      def act_requested(self):
   50          self.state = 'request'
   51  
   52:     @api.one
   53      def act_accept(self):
   54          self.state = 'accept'
   55  
   56:     @api.one
   57      def act_reject(self):
   58          self.state = 'reject'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_queue.py:
   60          return super(OpBookQueue, self).create(vals)
   61  
   62:     @api.one
   63      def do_reject(self):
   64          self.state = 'reject'
   65  
   66:     @api.one
   67      def do_accept(self):
   68          self.state = 'accept'
   69  
   70:     @api.one
   71      def do_request_again(self):
   72          self.state = 'request'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/issue_book.py:
   60                  days=self.library_card_id.library_card_type_id.duration)
   61  
   62:     @api.one
   63      def check_max_issue(self, student_id, library_card_id):
   64          book_movement_search = self.env["op.book.movement"].search(
   ..
   72              return False
   73  
   74:     @api.one
   75      def do_issue(self):
   76          value = {}

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/reserve_book.py:
   30      partner_id = fields.Many2one('res.partner', required=True)
   31  
   32:     @api.one
   33      def set_partner(self):
   34          self.env['op.book.movement'].browse(

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/return_book.py:
   37          required=True)
   38  
   39:     @api.one
   40      def do_return(self):
   41          book_movement = self.env['op.book.movement']

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/returndate.py:
   32          default=lambda self: fields.Date.today())
   33  
   34:     @api.one
   35      def assign_return_date(self):
   36          book_movement = self.env['op.book.movement'].browse(

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_placement/models/placement.py:
   38          default='draft', track_visibility='onchange')
   39  
   40:     @api.one
   41      def placement_offer(self):
   42          self.state = 'offer'
   43  
   44:     @api.one
   45      def placement_join(self):
   46          self.state = 'join'
   47  
   48:     @api.one
   49      def confirm_rejected(self):
   50          self.state = 'reject'
   51  
   52:     @api.one
   53      def confirm_to_draft(self):
   54          self.state = 'draft'
   55  
   56:     @api.one
   57      def confirm_cancel(self):
   58          self.state = 'cancel'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_scholarship/models/scholarship.py:
   36          select=True, track_visibility='onchange')
   37  
   38:     @api.one
   39      def act_confirm(self):
   40          self.state = 'confirm'
   41  
   42:     @api.one
   43      def act_reject(self):
   44          self.state = 'reject'

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/generate_timetable.py:
   79          self.batch_id = False
   80  
   81:     @api.one
   82      def gen_datewise(self, line, st_date, en_date, self_obj):
   83          day_cnt = 7
   ..
  114          return True
  115  
  116:     @api.one
  117      def act_gen_time_table(self):
  118          st_date = datetime.datetime.strptime(

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/time_table_report.py:
   47              datetime.today()).weekday())).strftime('%Y-%m-%d'))
   48  
   49:     @api.one
   50      @api.constrains('start_date', 'end_date')
   51      def _check_dates(self):

/home/shivamm/Desktop/odoo-9.0/addons/pos_cache/models/pos_cache.py:
   21          self.env['pos.cache'].search([]).refresh_cache()
   22  
   23:     @api.one
   24      def refresh_cache(self):
   25          products = self.env['product.product'].search(self.get_product_domain())
   ..
   54      _inherit = 'pos.config'
   55  
   56:     @api.one
   57      @api.depends('cache_ids')
   58      def _get_oldest_cache_time(self):
   ..
   92              return new_cache.get_cache(domain, fields)
   93  
   94:     @api.one
   95      def delete_cache(self):
   96          # throw away the old caches

/home/shivamm/Desktop/odoo-9.0/addons/pos_mercury/models/pos_mercury.py:
   39      mercury_invoice_no = fields.Integer(string='Mercury invoice number', help='Invoice number from Mercury Pay')
   40  
   41:     @api.one
   42      def _compute_prefixed_card_number(self):
   43          if self.mercury_card_number:

/home/shivamm/Desktop/odoo-9.0/addons/product/pricelist.py:
  325      _inherit = "product.pricelist.item"
  326  
  327:     @api.one
  328      @api.depends('categ_id', 'product_tmpl_id', 'product_id', 'compute_price', 'fixed_price', \
  329          'pricelist_id', 'percent_price', 'price_discount', 'price_surcharge')

/home/shivamm/Desktop/odoo-9.0/addons/product_uos/models/product_uos.py:
   20      _inherit = 'sale.order.line'
   21  
   22:     @api.one
   23      def _set_uos(self):
   24          if self.product_id.uos_coeff:
   ..
   26              self.product_uom = self.product_id.uom_id
   27  
   28:     @api.one
   29      def _compute_uos(self):
   30          self.product_uos_qty = self.product_uom_qty * self.product_id.uos_coeff

/home/shivamm/Desktop/odoo-9.0/addons/rating/models/rating.py:
   13      ]
   14  
   15:     @api.one
   16      @api.depends('res_model', 'res_id')
   17      def _compute_res_name(self):

/home/shivamm/Desktop/odoo-9.0/addons/rating_project/models/project.py:
   38      _inherit = "project.project"
   39  
   40:     @api.one
   41      @api.depends('percentage_satisfaction_task')
   42      def _compute_percentage_satisfaction_project(self):
   43          self.percentage_satisfaction_project = self.percentage_satisfaction_task
   44  
   45:     @api.one
   46      @api.depends('tasks.rating_ids.rating')
   47      def _compute_percentage_satisfaction_task(self):

/home/shivamm/Desktop/odoo-9.0/addons/rating_project_issue/models/project_issue.py:
   62                  record.percentage_satisfaction_project = -1
   63  
   64:     @api.one
   65      @api.depends('issue_ids.rating_ids.rating')
   66      def _compute_percentage_satisfaction_issue(self):

/home/shivamm/Desktop/odoo-9.0/addons/sale_crm/crm_lead.py:
    8      _inherit = ['crm.lead']
    9  
   10:     @api.one
   11      @api.depends('order_ids')
   12      def _get_sale_amount_total(self):

/home/shivamm/Desktop/odoo-9.0/addons/web_tip/web_tip.py:
    8      _description = 'Tips'
    9  
   10:     @api.one
   11      @api.depends('user_ids')
   12      def _is_consumed(self):

/home/shivamm/Desktop/odoo-9.0/addons/website_event/models/event.py:
   39      menu_id = fields.Many2one('website.menu', 'Event Menu')
   40  
   41:     @api.one
   42      def _get_new_menu_pages(self):
   43          todo = [
   ..
   54          return result
   55  
   56:     @api.one
   57      def _set_show_menu(self):
   58          if self.menu_id and not self.show_menu:
   ..
   72              self.menu_id = root_menu
   73  
   74:     @api.one
   75      def _get_show_menu(self):
   76          self.show_menu = bool(self.menu_id)

/home/shivamm/Desktop/odoo-9.0/addons/website_event_track/models/event.py:
   56      image = fields.Binary('Image', compute='_compute_image', store=True, attachment=True)
   57  
   58:     @api.one
   59      @api.depends('speaker_ids.image')
   60      def _compute_image(self):
   ..
  155              event.count_tracks = result.get(event.id, 0)
  156  
  157:     @api.one
  158      def _count_sponsor(self):
  159          self.count_sponsor = len(self.sponsor_ids)
  160  
  161:     @api.one
  162      @api.depends('track_ids.tag_ids')
  163      def _get_tracks_tag_ids(self):
  ...
  175      count_sponsor = fields.Integer('# Sponsors', compute='_count_sponsor')
  176  
  177:     @api.one
  178      def _get_new_menu_pages(self):
  179          result = super(event_event, self)._get_new_menu_pages()[0]  # TDE CHECK api.one -> returns a list with one item ?
  ...
  187          return result
  188  
  189:     @api.one
  190      def _set_show_menu(self):
  191          # if the number of menu items have changed, then menu items must be regenerated

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/forum.py:
  132      karma_moderate = fields.Integer(string='Moderate posts', default=1000)
  133  
  134:     @api.one
  135      @api.constrains('allow_question', 'allow_discussion', 'allow_link', 'default_post_type')
  136      def _check_default_post_type(self):
  ...
  140              raise UserError(_('You cannot choose %s as default post since the forum does not allow it.' % self.default_post_type))
  141  
  142:     @api.one
  143      @api.constrains('allow_link', 'allow_question', 'allow_discussion', 'default_post_type')
  144      def _check_default_post_type(self):
  ...
  146              raise Warning(_('Post type in "Default post" must be activated'))
  147  
  148:     @api.one
  149      def _compute_count_posts_waiting_validation(self):
  150          domain = [('forum_id', '=', self.id), ('state', '=', 'pending')]
  151          self.count_posts_waiting_validation = self.env['forum.post'].search_count(domain)
  152  
  153:     @api.one
  154      def _compute_count_flagged_posts(self):
  155          domain = [('forum_id', '=', self.id), ('state', '=', 'flagged')]
  ...
  278      can_moderate = fields.Boolean('Can Moderate', compute='_get_post_karma_rights')
  279  
  280:     @api.one
  281      @api.depends('content')
  282      def _get_plain_content(self):
  283          self.plain_content = tools.html2plaintext(self.content)[0:500] if self.content else False
  284  
  285:     @api.one
  286      @api.depends('vote_count', 'forum_id.relevancy_post_vote', 'forum_id.relevancy_time_decay')
  287      def _compute_relevancy(self):
  ...
  309              post.vote_count = result[post.id]
  310  
  311:     @api.one
  312      def _get_user_favourite(self):
  313          self.user_favourite = self._uid in self.favourite_ids.ids
  314  
  315:     @api.one
  316      @api.depends('favourite_ids')
  317      def _get_favorite_count(self):
  318          self.favourite_count = len(self.favourite_ids)
  319  
  320:     @api.one
  321      @api.depends('create_uid', 'parent_id')
  322      def _is_self_reply(self):
  323          self.self_reply = self.parent_id.create_uid.id == self._uid
  324  
  325:     @api.one
  326      @api.depends('child_ids.create_uid', 'website_message_ids')
  327      def _get_child_count(self):
  ...
  333          self.child_count = process(self)
  334  
  335:     @api.one
  336      def _get_uid_has_answered(self):
  337          self.uid_has_answered = any(answer.create_uid.id == self._uid for answer in self.child_ids)
  338  
  339:     @api.one
  340      @api.depends('child_ids.is_correct')
  341      def _get_has_validated_answer(self):
  ...
  375              post.can_moderate = is_admin or user.karma >= post.forum_id.karma_moderate
  376  
  377:     @api.one
  378      @api.constrains('post_type', 'forum_id')
  379      def _check_post_type(self):
  ...
  522          return True
  523  
  524:     @api.one
  525      def validate(self):
  526          if not self.can_moderate:
  ...
  539          return True
  540  
  541:     @api.one
  542      def refuse(self):
  543          if not self.can_moderate:
  ...
  547          return True
  548  
  549:     @api.one
  550      def flag(self):
  551          if not self.can_flag:
  ...
  563              return {'error': 'post_non_flaggable'}
  564  
  565:     @api.one
  566      def mark_as_offensive(self, reason_id):
  567          if not self.can_moderate:
  ...
  622          return {'vote_count': self.vote_count, 'user_vote': new_vote}
  623  
  624:     @api.one
  625      def convert_answer_to_comment(self):
  626          """ Tools to convert an answer (forum.post) to a comment (mail.message).
  ...
  687          return new_post
  688  
  689:     @api.one
  690      def unlink_comment(self, message_id):
  691          user = self.env.user

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/res_users.py:
   62              email)).hexdigest()
   63  
   64:     @api.one
   65      def send_forum_validation_email(self, forum_id=None):
   66          if not self.email:
   ..
   80          return True
   81  
   82:     @api.one
   83      def process_forum_validation_token(self, token, email, forum_id=None, context=None):
   84          validation_token = self._generate_forum_token(self.id, email)

/home/shivamm/Desktop/odoo-9.0/addons/website_hr_recruitment/models/hr_recruitment_source.py:
    9  
   10      @api.depends('source_id', 'source_id.name', 'job_id')
   11:     @api.one
   12      def _compute_url(self):
   13          base_url = self.env['ir.config_parameter'].get_param('web.base.url')

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/slides.py:
  108      can_upload = fields.Boolean('Can Upload', compute='_compute_access')
  109  
  110:     @api.one
  111      @api.depends('visibility', 'group_ids', 'upload_group_ids')
  112      def _compute_access(self):
  ...
  402          return True
  403  
  404:     @api.one
  405      def send_share_email(self, email):
  406          base_url = self.env['ir.config_parameter'].get_param('web.base.url')

237 matches across 78 files
