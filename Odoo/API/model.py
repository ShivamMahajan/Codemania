Searching 18994 files for "@api.model"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
  122      ]
  123  
  124:     @api.model
  125      def name_search(self, name, args=None, operator='ilike', limit=100):
  126          args = args or []
  ...
  325          return result
  326  
  327:     @api.model
  328      def _get_sequence_prefix(self, code, refund=False):
  329          prefix = code.upper()
  ...
  332          return prefix + '/%(range_year)s/'
  333  
  334:     @api.model
  335      def _create_sequence(self, vals, refund=False):
  336          """ Create new no_gap entry sequence for every new Journal"""
  ...
  348          return self.env['ir.sequence'].create(seq)
  349  
  350:     @api.model
  351      def _prepare_liquidity_account(self, name, company, currency_id, type):
  352          '''
  ...
  385          }
  386  
  387:     @api.model
  388      def create(self, vals):
  389          company_id = vals.get('company_id', self.env.user.company_id.id)
  ...
  486      _order = 'sequence'
  487  
  488:     @api.model
  489      def _default_tax_group(self):
  490          return self.env['account.tax.group'].search([], limit=1)
  ...
  529          return super(AccountTax, self).copy(default=default)
  530  
  531:     @api.model
  532      def name_search(self, name, args=None, operator='ilike', limit=80):
  533          """ Returns a list of tupples containing id, name, as internally it is called {def name_get}
  ...
  542          return taxes.name_get()
  543  
  544:     @api.model
  545      def search(self, args, offset=0, limit=None, order=None, count=False):
  546          context = self._context or {}
  ...
  676          return recs.compute_all(price_unit, currency, quantity, product, partner)
  677  
  678:     @api.model
  679      def _fix_tax_included_price(self, price, prod_taxes, line_taxes):
  680          """Subtract tax amount from price when corresponding "price included" taxes do not apply"""

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_analytic_line.py:
   47          self.product_uom_id = unit
   48  
   49:     @api.model
   50      def view_header_get(self, view_id, view_type):
   51          context = (self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
   90          self.all_lines_reconciled = all([line.journal_entry_ids.ids or line.account_id.id for line in self.line_ids])
   91  
   92:     @api.model
   93      def _default_journal(self):
   94          journal_type = self.env.context.get('journal_type', False)
   ..
  109                  bank_stmt.balance_start = 0
  110  
  111:     @api.model
  112      def _default_opening_balance(self):
  113          #Search last bank statement and set current opening balance as closing balance of previous one
  ...
  185          return True
  186  
  187:     @api.model
  188      def create(self, vals):
  189          if not vals.get('name'):
  ...
  400          return super(AccountBankStatementLine, self).unlink()
  401  
  402:     @api.model
  403      def _needaction_domain_get(self):
  404          return [('journal_entry_ids', '=', False), ('account_id', '=', False)]

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
   55          self.amount_untaxed_signed = amount_untaxed_signed * sign
   56  
   57:     @api.model
   58      def _default_journal(self):
   59          inv_type = self._context.get('type', 'out_invoice')
   ..
   66          return self.env['account.journal'].search(domain, limit=1)
   67  
   68:     @api.model
   69      def _default_currency(self):
   70          journal = self._default_journal()
   71          return journal.currency_id or journal.company_id.currency_id
   72  
   73:     @api.model
   74      def _get_reference_type(self):
   75          return [('none', _('Free Reference'))]
   ..
  308      ]
  309  
  310:     @api.model
  311      def create(self, vals):
  312          if not vals.get('account_id',False):
  ...
  314          return super(AccountInvoice, self.with_context(mail_create_nolog=True)).create(vals)
  315  
  316:     @api.model
  317      def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
  318          def get_view_id(xid, name):
  ...
  575          return total, total_currency, invoice_move_lines
  576  
  577:     @api.model
  578      def invoice_line_move_line_get(self):
  579          res = []
  ...
  605          return res
  606  
  607:     @api.model
  608      def tax_line_move_line_get(self):
  609          res = []
  ...
  760          return self.write({'state': 'open'})
  761  
  762:     @api.model
  763      def line_get_convert(self, line, part):
  764          return {
  ...
  816          return result
  817  
  818:     @api.model
  819      def name_search(self, name, args=None, operator='ilike', limit=100):
  820          args = args or []
  ...
  826          return recs.name_get()
  827  
  828:     @api.model
  829      def _refund_cleanup_lines(self, lines):
  830          """ Convert records to dict of values suitable for one2many line creation
  ...
  848          return result
  849  
  850:     @api.model
  851      def _prepare_refund(self, invoice, date_invoice=None, date=None, description=None, journal_id=None):
  852          """ Prepare the dict of values to create the new refund from the invoice.
  ...
 1007          self.price_subtotal_signed = price_subtotal_signed * sign
 1008  
 1009:     @api.model
 1010      def _default_account(self):
 1011          if self._context.get('journal_id'):
 ....
 1052      company_currency_id = fields.Many2one('res.currency', related='invoice_id.company_currency_id', readonly=True)
 1053  
 1054:     @api.model
 1055      def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
 1056          res = super(AccountInvoiceLine, self).fields_view_get(

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_move.py:
   95      dummy_account_id = fields.Many2one('account.account', related='line_ids.account_id', string='Account', store=False)
   96  
   97:     @api.model
   98      def create(self, vals):
   99          move = super(AccountMove, self.with_context(check_move_validity=False)).create(vals)
  ...
  263              line.balance = line.debit - line.credit
  264  
  265:     @api.model
  266      def _get_currency(self):
  267          currency = False
  ...
  271          return currency
  272  
  273:     @api.model
  274      def _get_journal(self):
  275          """ Return journal based on the journal type """
  ...
  396      ####################################################
  397  
  398:     @api.model
  399      def get_data_for_manual_reconciliation_widget(self, partner_ids, account_ids):
  400          """ Returns the data required for the invoices & payments matching of partners/accounts.
  ...
  407          }
  408  
  409:     @api.model
  410      def get_data_for_manual_reconciliation(self, res_type, res_ids=None, account_type=None):
  411          """ Returns the data required for the invoices & payments matching of partners/accounts (list of dicts).
  ...
  494          return rows
  495  
  496:     @api.model
  497      def get_reconciliation_proposition(self, account_id, partner_id=False):
  498          """ Returns two lines whose amount are opposite """
  ...
  524          return []
  525  
  526:     @api.model
  527      def domain_move_lines_for_reconciliation(self, excluded_ids=None, str=False):
  528          """ Returns the domain which is common to both manual and bank statement reconciliation.
  ...
  569          return expression.AND([generic_domain, domain])
  570  
  571:     @api.model
  572      def get_move_lines_for_manual_reconciliation(self, account_id, partner_id=False, excluded_ids=None, str=False, offset=0, limit=None, target_currency_id=False):
  573          """ Returns unreconciled move lines for an account or a partner+account, formatted for the manual reconciliation widget """
  ...
  864  
  865      #TODO: to check/refactor
  866:     @api.model
  867      def create(self, vals, apply_taxes=True):
  868          """ :param apply_taxes: set to False if you don't want vals['tax_ids'] to result in the creation of move lines for taxes and eventual
  ...
 1055          return result
 1056  
 1057:     @api.model
 1058      def compute_amount_fields(self, amount, src_currency, company_currency):
 1059          """ Helper function to compute value for fields debit/credit/amount_currency based on an amount and the currencies given in parameter"""
 ....
 1097          }
 1098  
 1099:     @api.model
 1100      def _query_get(self, domain=None):
 1101          context = dict(self._context or {})
 ....
 1196                      move.post()
 1197  
 1198:     @api.model
 1199      def create(self, vals):
 1200          res = super(AccountPartialReconcile, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
  104          return self.env['account.invoice'].browse(self._context.get('active_ids'))
  105  
  106:     @api.model
  107      def default_get(self, fields):
  108          rec = super(account_register_payments, self).default_get(fields)
  ...
  237          return res
  238  
  239:     @api.model
  240      def default_get(self, fields):
  241          rec = super(account_payment, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/account/models/chart_template.py:
  120          return True
  121  
  122:     @api.model
  123      def generate_journals(self, acc_template_ref, company, journals_dict=None):
  124          """
  ...
  547              "the usual m2o fields. This last choice assumes that the set of tax defined for the chosen template is complete")
  548  
  549:     @api.model
  550      def _get_chart_parent_ids(self, chart_template):
  551          """ Returns the IDs of all ancestor charts, including the chart itself.
  ...
  596          return res
  597  
  598:     @api.model
  599      def default_get(self, fields):
  600          context = self._context or {}
  ...
  641          return res
  642  
  643:     @api.model
  644      def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
  645          context = self._context or {}

/home/shivamm/Desktop/odoo-9.0/addons/account/models/partner.py:
  119              self.state_ids = [(5,)]
  120  
  121:     @api.model
  122      def _get_fpos_by_region(self, country_id=False, state_id=False, zipcode=False, vat_required=False):
  123          if not country_id:
  ...
  149          return False
  150  
  151:     @api.model
  152      def get_fiscal_position(self, partner_id, delivery_id=None):
  153          if not partner_id:
  ...
  463          return partner.commercial_partner_id
  464  
  465:     @api.model
  466      def _commercial_fields(self):
  467          return super(ResPartner, self)._commercial_fields() + \

/home/shivamm/Desktop/odoo-9.0/addons/account/models/res_config.py:
  131  
  132  
  133:     @api.model
  134      def _default_has_default_company(self):
  135          count = self.env['res.company'].search_count([])

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_financial_report.py:
    9      _description = "Accounting Report"
   10  
   11:     @api.model
   12      def _get_account_report(self):
   13          reports = []

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_invoice_refund.py:
   12      _description = "Invoice Refund"
   13  
   14:     @api.model
   15      def _get_reason(self):
   16          context = dict(self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_reconcile.py:
   16      company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.user.company_id)
   17  
   18:     @api.model
   19      def default_get(self, fields):
   20          res = super(AccountMoveLineReconcile, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
  118          return result
  119  
  120:     @api.model
  121      def _cron_generate_entries(self):
  122          assets = self.env['account.asset.asset'].search([('state', '=', 'open')])
  ...
  358          return depreciation_ids.create_move()
  359  
  360:     @api.model
  361      def create(self, vals):
  362          asset = super(AccountAssetAsset, self.with_context(mail_create_nolog=True)).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/wizard/account_asset_change_duration.py:
   22              self.asset_method_time = asset.method_time
   23  
   24:     @api.model
   25      def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
   26          result = super(AssetModify, self).fields_view_get(view_id, view_type, toolbar=toolbar, submenu=submenu)
   ..
   41          return result
   42  
   43:     @api.model
   44      def default_get(self, fields):
   45          res = super(AssetModify, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_journal.py:
   37          help="Technical feature used to know whether check printing was enabled as payment method.")
   38  
   39:     @api.model
   40      def create(self, vals):
   41          rec = super(AccountJournal, self).create(vals)
   ..
   65          return methods + self.env.ref('account_check_printing.account_payment_method_check')
   66  
   67:     @api.model
   68      def _enable_check_printing_on_bank_journals(self):
   69          """ Enables check printing payment method and add a check sequence on bank journals.

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_payment.py:
   81                  raise ValidationError(_("A check memo cannot exceed 60 characters."))
   82  
   83:     @api.model
   84      def create(self, vals):
   85          if vals['payment_method_id'] == self.env.ref('account_check_printing.account_payment_method_check').id\

/home/shivamm/Desktop/odoo-9.0/addons/account_tax_cash_basis/tax_cash_basis.py:
   90              move.post()
   91  
   92:     @api.model
   93      def create(self, vals):
   94          aml = []

/home/shivamm/Desktop/odoo-9.0/addons/account_test/report/account_test_report.py:
   11      _name = 'report.account_test.report_accounttest'
   12  
   13:     @api.model
   14      def execute_code(self, code_exec):
   15          def reconciled_inv():

/home/shivamm/Desktop/odoo-9.0/addons/account_voucher/account_voucher.py:
   16          self.paid = any([((line.account_id.internal_type, 'in', ('receivable', 'payable')) and line.reconciled) for line in self.move_id.line_ids])
   17  
   18:     @api.model
   19      def _get_currency(self):
   20          journal = self.env['account.journal'].browse(self._context.get('journal_id', False))
   ..
   33          self.currency_id = self.journal_id.currency_id.id or self.company_id.currency_id.id
   34  
   35:     @api.model
   36      def _default_journal(self):
   37          voucher_type = self._context.get('voucher_type', 'sale')

/home/shivamm/Desktop/odoo-9.0/addons/analytic/models/analytic.py:
   73          return res
   74  
   75:     @api.model
   76      def name_search(self, name='', args=None, operator='ilike', limit=100):
   77          args = args or []
   ..
   85      _order = 'date desc, id desc'
   86  
   87:     @api.model
   88      def _default_user(self):
   89          return self.env.user.id

/home/shivamm/Desktop/odoo-9.0/addons/barcodes/barcodes.py:
  178      _order = 'sequence asc'
  179  
  180:     @api.model
  181      def _encoding_selection_list(self):
  182          return [
  ...
  187          ]
  188  
  189:     @api.model
  190      def _get_type_selection(self):
  191          return [('alias','Alias'),('product','Unit Product')]

/home/shivamm/Desktop/odoo-9.0/addons/base_gengo/ir_translation.py:
   86          return (query, params)
   87  
   88:     @api.model
   89      def _get_terms_query(self, field, records):
   90          query, params = super(ir_translation, self)._get_terms_query(field, records)

/home/shivamm/Desktop/odoo-9.0/addons/base_iban/base_iban.py:
   58          return get_bban_from_iban(self.acc_number)
   59  
   60:     @api.model
   61      def create(self, vals):
   62          if (vals.get('acc_type') == 'iban') and vals.get('acc_number'):

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/bus.py:
   37      message = fields.Char('Message')
   38  
   39:     @api.model
   40      def gc(self):
   41          timeout_ago = datetime.datetime.utcnow()-datetime.timedelta(seconds=TIMEOUT*2)
   ..
   43          return self.sudo().search(domain).unlink()
   44  
   45:     @api.model
   46      def sendmany(self, notifications):
   47          channels = set()
   ..
   66                  cr2.execute("notify imbus, %s", (json_dump(list(channels)),))
   67  
   68:     @api.model
   69      def sendone(self, channel, message):
   70          self.sendmany([[channel, message]])
   71  
   72:     @api.model
   73      def poll(self, channels, last=0):
   74          # first poll return the notification in the 'buffer'

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/bus_presence.py:
   32  
   33  
   34:     @api.model
   35      def update(self, user_presence=True):
   36          """ Register the given presence of the current user, and trigger a im_status change if necessary.
   ..
   76          return True
   77  
   78:     @api.model
   79      def check_users_disconnection(self):
   80          """ Disconnect the users having a too old last_poll """

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/res_partner.py:
   21              partner.im_status = result.get(partner.id, 'offline')
   22  
   23:     @api.model
   24      def im_search(self, name, limit=20):
   25          """ Search partner with a name and return its id, name and im_status.

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/res_users.py:
   19              user.im_status = res.get(user.id)
   20  
   21:     @api.model
   22      def im_search(self, name, limit=20):
   23          """ Search users with a name and return its id, name and im_status.

/home/shivamm/Desktop/odoo-9.0/addons/crm/models/crm_activity.py:
   34      activity_3_id = fields.Many2one('crm.activity', string="Next Activity 3")
   35  
   36:     @api.model
   37      def create(self, values):
   38          ''' Override to set the res_model of inherited subtype to crm.lead.

/home/shivamm/Desktop/odoo-9.0/addons/crm/web_planner.py:
    7      _inherit = 'web.planner'
    8  
    9:     @api.model
   10      def _get_planner_application(self):
   11          planner = super(PlannerCrm, self)._get_planner_application()
   ..
   13          return planner
   14  
   15:     @api.model
   16      def _prepare_planner_crm_data(self):
   17          menu = self.env.ref('crm.menu_crm_opportunities', raise_if_not_found=False)

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_carrier.py:
  204          return True
  205  
  206:     @api.model
  207      def create(self, vals):
  208          res = super(DeliveryCarrier, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
   51      event_mail_ids = fields.One2many('event.mail', 'event_id', string='Mail Schedule', default=lambda self: self._default_event_mail_ids())
   52  
   53:     @api.model
   54      def _default_event_mail_ids(self):
   55          return [(0, 0, {
   ..
  130      date_end_located = fields.Datetime(string='End Date Located', compute='_compute_date_end_tz')
  131  
  132:     @api.model
  133      def _tz_get(self):
  134          return [(x, x) for x in pytz.all_timezones]
  ...
  204              raise UserError(_('Closing Date cannot be set before Beginning Date.'))
  205  
  206:     @api.model
  207      def create(self, vals):
  208          res = super(event_event, self).create(vals)
  ...
  308          return True
  309  
  310:     @api.model
  311      def create(self, vals):
  312          registration = super(event_registration, self).create(vals)
  ...
  315          return registration
  316  
  317:     @api.model
  318      def _prepare_attendee_values(self, registration):
  319          """ Method preparing the values to create new attendees based on a

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event_mail.py:
   84          return True
   85  
   86:     @api.model
   87      def run(self, autocommit=False):
   88          schedulers = self.search([('done', '=', False), ('scheduled_date', '<=', datetime.strftime(fields.datetime.now(), tools.DEFAULT_SERVER_DATETIME_FORMAT))])

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
   14          default=lambda rec: rec._default_tickets(), copy=True)
   15  
   16:     @api.model
   17      def _default_tickets(self):
   18          try:
   ..
   42      is_expired = fields.Boolean('Is Expired', compute='_is_expired')
   43  
   44:     @api.model
   45      def _default_product_id(self):
   46          try:
   ..
  162          return res
  163  
  164:     @api.model
  165      def create(self, vals):
  166          res = super(event_registration, self).create(vals)
  ...
  173          return res
  174  
  175:     @api.model
  176      def _prepare_attendee_values(self, registration):
  177          """ Override to add sale related stuff """

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/wizard/event_edit_registration.py:
   10      event_registration_ids = fields.One2many('registration.editor.line', 'editor_id', string='Registrations to Edit')
   11  
   12:     @api.model
   13      def default_get(self, fields):
   14          res = super(SaleOrderEventRegistration, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/exam/models/exam.py:
  452      _description = 'Student Information'
  453  
  454:     @api.model
  455      def search(self, args, offset=0, limit=None, order=None, count=False):
  456          if self._context.get('exam'):

/home/shivamm/Desktop/odoo-9.0/addons/hr/hr.py:
  109      # TDE note: done in new api, because called with new api -> context is a
  110      # frozendict -> error when tryign to manipulate it
  111:     @api.model
  112      def create(self, values):
  113          return super(hr_job, self.with_context(mail_create_nosubscribe=True)).create(values)

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
   58              category.maintenance_count = mapped_data.get(category.id, 0)
   59  
   60:     @api.model
   61      def create(self, vals):
   62          self = self.with_context(alias_model_name='hr.equipment.request', alias_parent_model_name=self._name)
   ..
   96          return result
   97  
   98:     @api.model
   99      def name_search(self, name, args=None, operator='ilike', limit=100):
  100          args = args or []
  ...
  154      ]
  155  
  156:     @api.model
  157      def create(self, vals):
  158          equipment = super(HrEquipment, self).create(vals)
  ...
  282              self.user_id = self.category_id.user_id
  283  
  284:     @api.model
  285      def create(self, vals):
  286          # context: no_log, because subtype already handle this
  ...
  330      }
  331  
  332:     @api.model
  333      def message_new(self, msg, custom_values=None):
  334          """ Overrides mail_thread message_new that is called by the mailgateway

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/models/hr_expense.py:
   88          self.message_subscribe_users(user_ids=user_ids)
   89  
   90:     @api.model
   91      def create(self, vals):
   92          hr_expense = super(HrExpense, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_job.py:
    9      _inherits = {'mail.alias': 'alias_id'}
   10  
   11:     @api.model
   12      def _default_address_id(self):
   13          return self.env.user.company_id.partner_id
   ..
   61              job.application_count = result.get(job.id, 0)
   62  
   63:     @api.model
   64      def create(self, vals):
   65          job = super(Job, self.with_context(alias_model_name='hr.applicant',

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_recruitment.py:
  171              record.attachment_number = attach_data.get(record.id, 0)
  172  
  173:     @api.model
  174      def _read_group_stage_ids(self, ids, domain, read_group_order=None, access_rights_uid=None):
  175          access_rights_uid = access_rights_uid or self.env.uid
  ...
  258          return {'value': {'date_closed': False}}
  259  
  260:     @api.model
  261      def create(self, vals):
  262          if vals.get('department_id') and not self._context.get('default_department_id'):
  ...
  294          return res
  295  
  296:     @api.model
  297      def get_empty_list_help(self, help):
  298          return super(Applicant, self.with_context(empty_list_help_model='hr.job',
  ...
  367          return super(Applicant, self)._track_subtype(init_values)
  368  
  369:     @api.model
  370      def message_get_reply_to(self, ids, default=None):
  371          """ Override to get the reply_to of the parent project. """
  ...
  384          return recipients
  385  
  386:     @api.model
  387      def message_new(self, msg, custom_values=None):
  388          """ Overrides mail_thread message_new that is called by the mailgateway

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/im_livechat_channel.py:
  143          return self.sudo().user_ids.filtered(lambda user: user.im_status == 'online')
  144  
  145:     @api.model
  146      def get_mail_channel(self, livechat_channel_id, anonymous_name):
  147          """ Return a mail.channel given a livechat channel. It creates one with a connected operator, or return false otherwise
  ...
  176          return mail_channel.sudo().with_context(im_livechat_operator_partner_id=operator_partner_id).channel_info()[0]
  177  
  178:     @api.model
  179      def get_channel_infos(self, channel_id):
  180          channel = self.browse(channel_id)
  ...
  187          }
  188  
  189:     @api.model
  190      def match_rules(self, request, channel_id, username='Visitor'):
  191          info = {

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/mail_channel.py:
   50          return channel_infos_dict.values()
   51  
   52:     @api.model
   53      def channel_fetch_slot(self):
   54          values = super(MailChannel, self).channel_fetch_slot()
   ..
   57          return values
   58  
   59:     @api.model
   60      def cron_remove_empty_session(self):
   61          self.env.cr.execute("""

/home/shivamm/Desktop/odoo-9.0/addons/link_tracker/models/link_tracker.py:
   45      icon_src = fields.Char(string='Favicon Source', compute='_compute_icon_src')
   46  
   47:     @api.model
   48      def convert_links(self, html, vals, blacklist=None):
   49          for match in re.findall(URL_REGEX, html):
   ..
  104          self.redirected_url = '%s://%s%s?%s&%s#%s' % (parsed.scheme, parsed.netloc, parsed.path, urlencode(utms), parsed.query, parsed.fragment)
  105  
  106:     @api.model
  107      @api.depends('url')
  108      def _get_title_from_url(self, url):
  ...
  142          }
  143  
  144:     @api.model
  145      def recent_links(self, filter, limit):
  146          if filter == 'newest':
  ...
  153              return {'Error': "This filter doesn't exist."}
  154  
  155:     @api.model
  156      def create(self, vals):
  157          create_vals = vals.copy()
  ...
  186          return link
  187  
  188:     @api.model
  189      def get_url_from_code(self, code, context=None):
  190          code_rec = self.env['link.tracker.code'].sudo().search([('code', '=', code)])
  ...
  206      link_id = fields.Many2one('link.tracker', 'Link', required=True, ondelete='cascade')
  207  
  208:     @api.model
  209      def get_random_code_string(self):
  210          size = 3
  ...
  231      country_id = fields.Many2one('res.country', 'Country')
  232  
  233:     @api.model
  234      def add_click(self, code, ip, country_code, stat_id=False):
  235          self = self.sudo()

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/ir_actions.py:
   10      _inherit = ['ir.actions.server']
   11  
   12:     @api.model
   13      def _get_states(self):
   14          res = super(ServerActions, self)._get_states()
   ..
   32              raise UserError(_('Your template should define email_from'))
   33  
   34:     @api.model
   35      def run_action_email(self, action, eval_context=None):
   36          # TDE CLEANME: when going to new api with server action, remove action
   ..
   40          return False
   41  
   42:     @api.model
   43      def _get_eval_context(self, action=None):
   44          """ Override the method giving the evaluation context but also the

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_alias.py:
   99              raise UserError(_('Invalid expression, it must be a literal python dictionary definition e.g. "{\'field\': \'value\'}"'))
  100  
  101:     @api.model
  102      def create(self, vals):
  103          """ Creates an email.alias record according to the values provided in ``vals``,
  ...
  142          return res
  143  
  144:     @api.model
  145      def _find_unique(self, name, alias_ids=False):
  146          """Find a unique alias name similar to ``name``. If ``name`` is
  ...
  159          return new_name
  160  
  161:     @api.model
  162      def _clean_and_make_unique(self, name, alias_ids=False):
  163          # when an alias name appears to already be an email, we keep the local part only

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_channel.py:
   96          self.image = tools.image_resize_image_big(self.image_small)
   97  
   98:     @api.model
   99      def create(self, vals):
  100          # Create channel and alias
  ...
  301  
  302      # User methods
  303:     @api.model
  304      def channel_get(self, partners_to, pin=True):
  305          """ Get the canonical private channel between some partners, create it if needed.
  ...
  345          return False
  346  
  347:     @api.model
  348      def channel_fold(self, uuid, state=None):
  349          """ Update the fold_state of the given session. In order to syncronize web browser
  ...
  366              self.env['bus.bus'].sendone((self._cr.dbname, 'res.partner', self.env.user.partner_id.id), session_state.channel_id.channel_info()[0])
  367  
  368:     @api.model
  369      def channel_minimize(self, uuid, minimized=True):
  370          values = {
  ...
  377          self.env['bus.bus'].sendone((self._cr.dbname, 'res.partner', self.env.user.partner_id.id), channel_partners.channel_id.channel_info()[0])
  378  
  379:     @api.model
  380      def channel_pin(self, uuid, pinned=False):
  381          # add the person in the channel, and pin it (or unpin it)
  ...
  408      # Instant Messaging View Specific (Slack Client Action)
  409      #------------------------------------------------------
  410:     @api.model
  411      def get_init_notifications(self):
  412          """ Get unread messages and old messages received less than AWAY_TIMER
  ...
  442          return notifications
  443  
  444:     @api.model
  445      def channel_fetch_slot(self):
  446          """ Return the channels of the user grouped by 'slot' (channel, direct_message or private_group), and
  ...
  469          return values
  470  
  471:     @api.model
  472      def channel_search_to_join(self, name=None, domain=None):
  473          """ Return the channel info of the channel the current partner can join
  ...
  494          return channel_info
  495  
  496:     @api.model
  497      def channel_create(self, name, privacy='public'):
  498          """ Create a channel and add the current partner, broadcast it (to make the user directly

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_followers.py:
   30          help="Message subtypes followed, meaning subtypes that will be pushed onto the user's Wall.")
   31  
   32:     @api.model
   33      def _add_follower_command(self, res_model, res_ids, partner_data, channel_data, force=True):
   34          """ Please upate me
   ..
  108      # cache may contain accessible/inaccessible data, one has to refresh it.
  109      #
  110:     @api.model
  111      def create(self, vals):
  112          res = super(Followers, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_mail.py:
   52          help="Failure reason. This is usually the exception thrown by the email server, stored to ease the debugging of mailing issues.")
   53  
   54:     @api.model
   55      def create(self, values):
   56          # notification field: if not set, set if mail comes from an existing mail.message
   ..
   67          return res
   68  
   69:     @api.model
   70      def default_get(self, fields):
   71          # protection for `default_type` values leaking from menu action context (e.g. for invoices)
   ..
   83          return self.write({'state': 'cancel'})
   84  
   85:     @api.model
   86      def process_email_queue(self, ids=None):
   87          """Send immediately queued messages, committing after each

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_message.py:
   34      _message_read_limit = 30
   35  
   36:     @api.model
   37      def _get_default_from(self):
   38          if self.env.user.alias_name and self.env.user.alias_domain:
   ..
   42          raise UserError(_("Unable to send email, please configure the sender's email address or alias."))
   43  
   44:     @api.model
   45      def _get_default_author(self):
   46          return self.env.user.partner_id
   ..
  119              message.needaction = message in my_messages
  120  
  121:     @api.model
  122      def _search_needaction(self, operator, operand):
  123          if operator == '=' and operand:
  ...
  133              message.starred = message in starred
  134  
  135:     @api.model
  136      def _search_starred(self, operator, operand):
  137          if operator == '=' and operand:
  ...
  139          return [('starred_partner_ids', 'not in', [self.env.user.partner_id.id])]
  140  
  141:     @api.model
  142      def _needaction_domain_get(self):
  143          return [('needaction', '=', True)]
  ...
  186      #------------------------------------------------------
  187  
  188:     @api.model
  189      def _message_read_dict_postprocess(self, messages, message_tree):
  190          """ Post-processing on values given by message_read. This method will
  ...
  439  
  440  
  441:     @api.model
  442      def message_fetch(self, domain, limit=20):
  443          return self.search(domain, limit=limit).message_format()
  ...
  511              cr.execute("""CREATE INDEX mail_message_model_res_id_idx ON mail_message (model, res_id)""")
  512  
  513:     @api.model
  514      def _find_allowed_model_wise(self, doc_model, doc_dict):
  515          doc_ids = doc_dict.keys()
  ...
  517          return set([message_id for allowed_doc_id in allowed_doc_ids for message_id in doc_dict[allowed_doc_id]])
  518  
  519:     @api.model
  520      def _find_allowed_doc_ids(self, model_ids):
  521          IrModelAccess = self.env['ir.model.access']
  ...
  527          return allowed_ids
  528  
  529:     @api.model
  530      def _search(self, args, offset=0, limit=None, order=None, count=False, access_rights_uid=None):
  531          """ Override that adds specific access rights of mail.message, to remove
  ...
  740              (self._description, operation))
  741  
  742:     @api.model
  743      def _get_record_name(self, values):
  744          """ Return the related document name, using name_get. It is done using
  ...
  750          return self.env[model].sudo().browse(res_id).name_get()[0][1]
  751  
  752:     @api.model
  753      def _get_reply_to(self, values):
  754          """ Return a specific reply_to: alias of the document through
  ...
  762              return self.env['mail.thread'].message_get_reply_to([None], default=email_from)[None]
  763  
  764:     @api.model
  765      def _get_message_id(self, values):
  766          if values.get('no_auto_thread', False) is True:
  ...
  772          return message_id
  773  
  774:     @api.model
  775      def create(self, values):
  776          # coming from mail.js that does not have pid in its values

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_shortcode.py:
   23               "* Text (default value) is use to substitute text with another text")
   24  
   25:     @api.model
   26      def create(self, values):
   27          if values.get('substitution'):
   ..
   45          return cgi.escape(substitution)
   46  
   47:     @api.model
   48      def apply_shortcode(self, message, shortcode_type=None):
   49          """ Apply the substitution on the given text

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_template.py:
   94      _order = 'name'
   95  
   96:     @api.model
   97      def default_get(self, fields):
   98          res = super(MailTemplate, self).default_get(fields)
   ..
  263      # ----------------------------------------
  264  
  265:     @api.model
  266      def _replace_local_links(self, html):
  267          """ Post-processing of html content to replace local links to absolute
  ...
  301          return html
  302  
  303:     @api.model
  304      def render_post_process(self, html):
  305          html = self._replace_local_links(html)
  306          return html
  307  
  308:     @api.model
  309      def render_template(self, template_txt, model, res_ids, post_process=False):
  310          """ Render the given template text, replace mako expressions ``${expr}``

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_thread.py:
  119          self.message_channel_ids = self.message_follower_ids.mapped('channel_id')
  120  
  121:     @api.model
  122      def _search_follower_partners(self, operator, operand):
  123          """Search function for message_follower_ids
  ...
  132          return [('id', 'in', followers.mapped('res_id'))]
  133  
  134:     @api.model
  135      def _search_follower_channels(self, operator, operand):
  136          """Search function for message_follower_ids
  ...
  157              record.message_is_follower = record.id in following_ids
  158  
  159:     @api.model
  160      def _search_is_follower(self, operator, operand):
  161          followers = self.env['mail.followers'].sudo().search([
  ...
  205              record.message_needaction = bool(record.message_needaction_counter)
  206  
  207:     @api.model
  208      def _search_message_needaction(self, operator, operand):
  209          return [('message_ids.needaction', operator, operand)]
  ...
  213      # ------------------------------------------------------
  214  
  215:     @api.model
  216      def create(self, values):
  217          """ Chatter override :
  ...
  305      # ------------------------------------------------------
  306  
  307:     @api.model
  308      def get_empty_list_help(self, help):
  309          """ Override of BaseModel.get_empty_list_help() to generate an help message
  ...
  360          return help
  361  
  362:     @api.model
  363      def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
  364          res = super(MailThread, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
  ...
  388      # ------------------------------------------------------
  389  
  390:     @api.model
  391      def _get_tracked_fields(self, updated_fields):
  392          """ Return a structure of tracked fields for the current model.
  ...
  478      #------------------------------------------------------
  479  
  480:     @api.model
  481      def _needaction_domain_get(self):
  482          if self._needaction:
  ...
  484          return []
  485  
  486:     @api.model
  487      def _garbage_collect_attachments(self):
  488          """ Garbage collect lost mail attachments. Those are attachments
  ...
  503          return True
  504  
  505:     @api.model
  506      def check_mail_message_access(self, res_ids, operation, model_name=None):
  507          """ mail.message check permission rules for related document. This method is
  ...
  530          DocModel.browse(res_ids).check_access_rule(check_operation)
  531  
  532:     @api.model
  533      def _get_inbox_action_xml_id(self):
  534          """ When redirecting towards the Inbox, choose which action xml_id has
  ...
  686          return res
  687  
  688:     @api.model
  689      def message_get_reply_to(self, res_ids, default=None):
  690          """ Returns the preferred reply-to email address that is basically the
  ...
  738      # ------------------------------------------------------
  739  
  740:     @api.model
  741      def message_capable_models(self):
  742          """ Used by the plugin addon, based for plugin_outlook and others. """
  ...
  755          return filter(lambda x: x, self._find_partner_from_emails(tools.email_split(s)))
  756  
  757:     @api.model
  758      def message_route_verify(self, message, message_dict, route, update_author=True, assert_model=True, create_fallback=True, allow_private=False):
  759          """ Verify route validity. Check and rules:
  ...
  884          return (model, thread_id, route[2], route[3], None if self._context.get('drop_alias', False) else route[4])
  885  
  886:     @api.model
  887      def message_route(self, message, message_dict, model=None, thread_id=None, custom_values=None):
  888          """Attempt to figure out the correct target model, thread_id,
  ...
 1077          )
 1078  
 1079:     @api.model
 1080      def message_route_process(self, message, message_dict, routes):
 1081          # postpone setting message_dict.partner_ids after message_post, to avoid double notifications
 ....
 1114          return thread_id
 1115  
 1116:     @api.model
 1117      def message_process(self, model, message, custom_values=None,
 1118                          save_original=False, strip_attachments=False,
 ....
 1177          return thread_id
 1178  
 1179:     @api.model
 1180      def message_new(self, msg_dict, custom_values=None):
 1181          """Called by ``message_process`` when a new message is received
 ....
 1317          return body, attachments
 1318  
 1319:     @api.model
 1320      def message_parse(self, message, save_original=False):
 1321          """Parses a string or email.message.Message representing an
 ....
 1538          return result
 1539  
 1540:     @api.model
 1541      def _message_preprocess_attachments(self, attachments, attachment_ids, attach_model, attach_res_id):
 1542          """ Preprocess attachments for mail_thread.message_post() or mail_mail.create().
 ....
 1825          ]).unlink()
 1826  
 1827:     @api.model
 1828      def _message_get_auto_subscribe_fields(self, updated_fields, auto_follow_fields=None):
 1829          """ Returns the list of relational fields linking to res.users that should

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_tracking_value.py:
   28      mail_message_id = fields.Many2one('mail.message', 'Message ID', required=True, select=True, ondelete='cascade')
   29  
   30:     @api.model
   31      def create_tracking_values(self, initial_value, new_value, col_name, col_info):
   32          tracked = True

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/res_partner.py:
   41          return dict((res_id, {'partner_ids': [res_id], 'email_to': False, 'email_cc': False}) for res_id in self.ids)
   42  
   43:     @api.model
   44      def _notify_prepare_template_context(self, message):
   45          # compute signature
   ..
   82          }
   83  
   84:     @api.model
   85      def _notify_prepare_email_values(self, message):
   86          # compute email references
   ..
  100          return mail_values
  101  
  102:     @api.model
  103      def _notify_send(self, body, subject, recipients, **mail_values):
  104          emails = self.env['mail.mail']
  ...
  200          self.env['bus.bus'].sendmany(notifications)
  201  
  202:     @api.model
  203      def get_needaction_count(self):
  204          """ compute the number of needaction of the current user """
  ...
  212          return 0
  213  
  214:     @api.model
  215      def get_mention_suggestions(self, search, channel, exclude=None, limit=8):
  216          """ Return 'limit'-first partners' id, name and email such that the name or email matches a

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/res_users.py:
   41          return self.pool.get('mail.alias').migrate_to_alias(cr, self._name, self._table, super(Users, self)._auto_init, self._name, self._columns['alias_id'], 'login', alias_force_key='id', context=context)
   42  
   43:     @api.model
   44      def create(self, values):
   45          if not values.get('login', False):

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/email_template_preview.py:
    9      _description = "Email Template Preview"
   10  
   11:     @api.model
   12      def _get_records(self):
   13          """ Return Records of particular Email Template's Model """
   ..
   22          return records.name_get()
   23  
   24:     @api.model
   25      def default_get(self, fields):
   26          result = super(TemplatePreview, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/invite.py:
    9      _description = 'Invite wizard'
   10  
   11:     @api.model
   12      def default_get(self, fields):
   13          result = super(Invite, self).default_get(fields)

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/mail_compose_message.py:
   44      _batch_size = 500
   45  
   46:     @api.model
   47      def default_get(self, fields):
   48          """ Handle composition mode. Some details about context keys:
   ..
   99          return result
  100  
  101:     @api.model
  102      def _get_composition_mode_selection(self):
  103          return [('comment', 'Post on a document'),
  ...
  150          return
  151  
  152:     @api.model
  153      def get_record_data(self, values):
  154          """ Returns a defaults-like dict with initial values for the composition
  ...
  468          return multi_mode and template_values or template_values[res_ids[0]]
  469  
  470:     @api.model
  471      def generate_email_for_composer(self, template_id, res_ids, fields=None):
  472          """ Call email_template.generate_email(), get fields relevant for
  ...
  490          return multi_mode and values or values[res_ids[0]]
  491  
  492:     @api.model
  493      def render_template(self, template, model, res_ids, post_process=False):
  494          return self.env['mail.template'].render_template(template, model, res_ids, post_process=post_process)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/batch.py:
   42              raise ValidationError("End Date cannot be set before Start Date.")
   43  
   44:     @api.model
   45      def name_search(self, name, args=None, operator='ilike', limit=100):
   46          if self.env.context.get('get_parent_batch', False):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_queue.py:
   53              raise ValidationError('To Date cannot be set before From Date.')
   54  
   55:     @api.model
   56      def create(self, vals):
   57          if vals.get('name', '/') == '/':

/home/shivamm/Desktop/odoo-9.0/addons/payment_authorize/models/authorize.py:
   25              return {'authorize_form_url': 'https://test.authorize.net/gateway/transact.dll'}
   26  
   27:     @api.model
   28      def _get_providers(self):
   29          providers = super(PaymentAcquirerAuthorize, self)._get_providers()
   ..
   94      # --------------------------------------------------
   95  
   96:     @api.model
   97      def _authorize_form_get_tx_from_data(self, data):
   98          """ Given a data dict coming from authorize, verify it and find the related
   ..
  114          return tx[0]
  115  
  116:     @api.model
  117      def _authorize_form_get_invalid_parameters(self, tx, data):
  118          invalid_parameters = []
  ...
  125          return invalid_parameters
  126  
  127:     @api.model
  128      def _authorize_form_validate(self, tx, data):
  129          if tx.state == 'done':

/home/shivamm/Desktop/odoo-9.0/addons/payment_sips/models/sips.py:
   51          return {'sips_form_url': url.get(environment, url['test']), }
   52  
   53:     @api.model
   54      def _get_providers(self):
   55          providers = super(AcquirerSips, self)._get_providers()
   ..
  143          return res
  144  
  145:     @api.model
  146      def _sips_form_get_tx_from_data(self, data):
  147          """ Given a data dict coming from sips, verify it and find the related
  ...
  166          return payment_tx
  167  
  168:     @api.model
  169      def _sips_form_get_invalid_parameters(self, tx, data):
  170          invalid_parameters = []
  ...
  183          return invalid_parameters
  184  
  185:     @api.model
  186      def _sips_form_validate(self, tx, data):
  187          data = self._sips_data_to_object(data.get('Data'))

/home/shivamm/Desktop/odoo-9.0/addons/pos_cache/models/pos_cache.py:
   17      compute_user_id = fields.Many2one('res.users', 'Cache compute user', required=True)
   18  
   19:     @api.model
   20      def refresh_all_caches(self):
   21          self.env['pos.cache'].search([]).refresh_cache()
   ..
   33          self.write(datas)
   34  
   35:     @api.model
   36      def get_product_domain(self):
   37          return literal_eval(self.product_domain)
   38  
   39:     @api.model
   40      def get_product_fields(self):
   41          return literal_eval(self.product_fields)
   42  
   43:     @api.model
   44      def get_cache(self, domain, fields):
   45          if not self.cache or domain != self.get_product_domain() or fields != self.get_product_fields():

/home/shivamm/Desktop/odoo-9.0/addons/pos_mercury/models/pos_mercury.py:
   54      _inherit = "pos.order"
   55  
   56:     @api.model
   57      def _payment_fields(self, ui_paymentline):
   58          fields = super(pos_order_card, self)._payment_fields(ui_paymentline)
   ..
   69          return fields
   70  
   71:     @api.model
   72      def add_payment(self, order_id, data):
   73          statement_id = super(pos_order_card, self).add_payment(order_id, data)

/home/shivamm/Desktop/odoo-9.0/addons/pos_mercury/models/pos_mercury_transaction.py:
   79          return response
   80  
   81:     @api.model
   82      def do_payment(self, data):
   83          try:
   ..
   89          return response
   90  
   91:     @api.model
   92      def do_reversal(self, data):
   93          return self._do_reversal_or_voidsale(data, False)
   94  
   95:     @api.model
   96      def do_voidsale(self, data):
   97          return self._do_reversal_or_voidsale(data, True)
   ..
  108      # One time (the ones we use) Mercury tokens are required to be
  109      # deleted after 6 months
  110:     @api.model
  111      def cleanup_old_tokens(self):
  112          expired_creation_date = (date.today() - timedelta(days=6 * 30)).strftime(DEFAULT_SERVER_DATETIME_FORMAT)

/home/shivamm/Desktop/odoo-9.0/addons/programmer/shivam.py:
   14  
   15  
   16: 	@api.model
   17  	def create(self, vals):
   18  		print vals

/home/shivamm/Desktop/odoo-9.0/addons/purchase/invoice.py:
   69          return {}
   70  
   71:     @api.model
   72      def invoice_line_move_line_get(self):
   73          res = super(AccountInvoice, self).invoice_line_move_line_get()
   ..
   79          return res
   80  
   81:     @api.model
   82      def _anglo_saxon_purchase_move_lines(self, i_line, res):
   83          """Return the additional move lines for purchase invoices and refunds.

/home/shivamm/Desktop/odoo-9.0/addons/purchase/partner.py:
   16              partner.supplier_invoice_count = Invoice.search_count([('partner_id', 'child_of', partner.id), ('type', '=', 'in_invoice')])
   17  
   18:     @api.model
   19      def _commercial_fields(self):
   20          return super(res_partner, self)._commercial_fields()

/home/shivamm/Desktop/odoo-9.0/addons/purchase/purchase.py:
   69              order.invoice_count = len(invoices)
   70  
   71:     @api.model
   72      def _default_picking_type(self):
   73          type_obj = self.env['stock.picking.type']
   ..
  152      group_id = fields.Many2one('procurement.group', string="Procurement Group")
  153  
  154:     @api.model
  155      def name_search(self, name, args=None, operator='ilike', limit=100):
  156          args = args or []
  ...
  172          return result
  173  
  174:     @api.model
  175      def create(self, vals):
  176          if vals.get('name', 'New') == 'New':
  ...
  308          return self.picking_type_id.default_location_dest_id.id
  309  
  310:     @api.model
  311      def _prepare_picking(self):
  312          if not self.group_id:
  ...
  534          return super(PurchaseOrderLine, self).unlink()
  535  
  536:     @api.model
  537      def _get_date_planned(self, seller, po=False):
  538          """Return the datetime value to use as Schedule Date (``date_planned``) for
  ...
  591  class ProcurementRule(models.Model):
  592      _inherit = 'procurement.rule'
  593:     @api.model
  594      def _get_action(self):
  595          return [('buy', _('Buy'))] + super(ProcurementRule, self)._get_action()
  ...
  636          return result
  637  
  638:     @api.model
  639      def _run(self, procurement):
  640          if procurement.rule_id and procurement.rule_id.action == 'buy':
  ...
  642          return super(ProcurementOrder, self)._run(procurement)
  643  
  644:     @api.model
  645      def _check(self, procurement):
  646          if procurement.purchase_line_id:
  ...
  812      _inherit = 'product.template'
  813  
  814:     @api.model
  815      def _get_buy_route(self):
  816          buy_route = self.env.ref('purchase.route_warehouse0_buy')

/home/shivamm/Desktop/odoo-9.0/addons/rating/models/rating.py:
   19          self.res_name = name and name[0][1] or ('%s/%s') % (self.res_model, self.res_id)
   20  
   21:     @api.model
   22      def new_access_token(self):
   23          return uuid.uuid4().hex
   ..
   34      message_id = fields.Many2one('mail.message', string="Linked message", help="Associated message when posting a review. Mainly used in website addons.", index=True)
   35  
   36:     @api.model
   37      def apply_rating(self, rate, res_model=None, res_id=None, token=None):
   38          """ apply a rating for given res_model/res_id or token. If the res_model is a mail.thread

/home/shivamm/Desktop/odoo-9.0/addons/rating_project/models/project.py:
   74      _inherit = "rating.rating"
   75  
   76:     @api.model
   77      def apply_rating(self, rate, res_model=None, res_id=None, token=None):
   78          """ check if the auto_validation_kanban_state is activated. If so, apply the modification of the

/home/shivamm/Desktop/odoo-9.0/addons/rating_project_issue/models/project_issue.py:
   99      _inherit = "rating.rating"
  100  
  101:     @api.model
  102      def apply_rating(self, rate, res_model=None, res_id=None, token=None):
  103          """ check if the auto_validation_kanban_state is activated. If so, apply the modification of the

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale.py:
   77              })
   78  
   79:     @api.model
   80      def _default_note(self):
   81          return self.env.user.company_id.sale_note
   82  
   83:     @api.model
   84      def _get_default_team(self):
   85          default_team_id = self.env['crm.team']._get_default_team_id()
   ..
  208          self.update(values)
  209  
  210:     @api.model
  211      def create(self, vals):
  212          if vals.get('name', 'New') == 'New':
  ...
  379          self.write({'state': 'done'})
  380  
  381:     @api.model
  382      def _prepare_procurement_group(self):
  383          return {'name': self.name}
  ...
  559          return new_procs
  560  
  561:     @api.model
  562      def _get_analytic_invoice_policy(self):
  563          return ['cost']
  564  
  565:     @api.model
  566      def _get_analytic_track_service(self):
  567          return []
  568  
  569:     @api.model
  570      def create(self, values):
  571          line = super(SaleOrderLine, self).create(values)
  ...
  771      _inherit = 'account.invoice'
  772  
  773:     @api.model
  774      def _get_default_team(self):
  775          default_team_id = self.env['crm.team']._get_default_team_id()

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale_analytic.py:
  118          return result
  119  
  120:     @api.model
  121      def create(self, values):
  122          line = super(AccountAnalyticLine, self).create(values)

/home/shivamm/Desktop/odoo-9.0/addons/sale/wizard/sale_make_invoice_advance.py:
   11      _description = "Sales Advance Payment Invoice"
   12  
   13:     @api.model
   14      def _count(self):
   15          return len(self._context.get('active_ids', []))
   16  
   17:     @api.model
   18      def _get_advance_payment_method(self):
   19          if self._count() == 1:

/home/shivamm/Desktop/odoo-9.0/addons/sale_mrp/sale_mrp.py:
   70      _inherit = 'stock.move'
   71  
   72:     @api.model
   73      def _prepare_procurement_from_move(self, move):
   74          res = super(StockMove, self)._prepare_procurement_from_move(move)
   ..
   77          return res
   78  
   79:     @api.model
   80      def _action_explode(self, move):
   81          """ Explodes pickings.

/home/shivamm/Desktop/odoo-9.0/addons/sale_service/models/timesheet.py:
   55      _inherit = 'account.analytic.line'
   56  
   57:     @api.model
   58      def _update_values(self, values):
   59          if values.get('task_id', False):
   ..
   61              values['so_line'] = task.sale_line_id and task.sale_line_id.id or values.get('so_line', False)
   62  
   63:     @api.model
   64      def create(self, values):
   65          self._update_values(values)

/home/shivamm/Desktop/odoo-9.0/addons/sale_stock/sale_stock.py:
   10      _inherit = "sale.order"
   11  
   12:     @api.model
   13      def _default_warehouse_id(self):
   14          company = self.env.user.company_id.id
   ..
   82          return invoice_vals
   83  
   84:     @api.model
   85      def _prepare_procurement_group(self):
   86          res = super(SaleOrder, self)._prepare_procurement_group()
   ..
  215      _inherit = "procurement.order"
  216  
  217:     @api.model
  218      def _run_move_create(self, procurement):
  219          vals = super(ProcurementOrder, self)._run_move_create(procurement)

/home/shivamm/Desktop/odoo-9.0/addons/sale_timesheet/models/sale_timesheet.py:
   11      _inherit = 'res.company'
   12  
   13:     @api.model
   14      def _get_uom_hours(self):
   15          try:
   ..
  142          return super(SaleOrderLine, self)._compute_analytic(domain=domain)
  143  
  144:     @api.model
  145      def _get_analytic_track_service(self):
  146          return super(SaleOrderLine, self)._get_analytic_track_service() + ['timesheet']

/home/shivamm/Desktop/odoo-9.0/addons/stock/wizard/stock_backorder_confirmation.py:
   11      pick_id = fields.Many2one('stock.picking')
   12  
   13:     @api.model
   14      def default_get(self, fields):
   15          res = {}

/home/shivamm/Desktop/odoo-9.0/addons/stock/wizard/stock_immediate_transfer.py:
   11      pick_id = fields.Many2one('stock.picking')
   12  
   13:     @api.model
   14      def default_get(self, fields):
   15          res = {}

/home/shivamm/Desktop/odoo-9.0/addons/stock_account/stock_account.py:
   51      _inherit = "account.invoice"
   52  
   53:     @api.model
   54      def invoice_line_move_line_get(self):
   55          res = super(account_invoice,self).invoice_line_move_line_get()
   ..
   60          return res
   61  
   62:     @api.model
   63      def _anglo_saxon_sale_move_lines(self, i_line):
   64          """Return the additional move lines for sales invoices and refunds.
   ..
  421      _inherit = "account.chart.template"
  422  
  423:     @api.model
  424      def generate_journals(self, acc_template_ref, company, journals_dict=None):
  425          journal_to_add = [{'name': _('Stock Journal'), 'type': 'general', 'code': 'STJ', 'favorite': False, 'sequence': 8}]

/home/shivamm/Desktop/odoo-9.0/addons/web_editor/models/ir_translation.py:
    7      _inherit = 'ir.translation'
    8  
    9:     @api.model
   10      def _get_terms_mapping(self, field, records):
   11          if self._context.get('edit_translations'):

/home/shivamm/Desktop/odoo-9.0/addons/web_planner/models/web_planner.py:
   19      _description = 'Planner'
   20  
   21:     @api.model
   22      def _get_planner_application(self):
   23          return []
   ..
   33      active = fields.Boolean(string="Active", default=True, help="If the active field is set to False, it will allow you to hide the planner. This change requires a refreshing a your page.")
   34  
   35:     @api.model
   36      def render(self, template_id, planner_app):
   37          # prepare the planner data as per the planner application
   ..
   45          return self.env['ir.ui.view'].browse(template_id).render(values=values)
   46  
   47:     @api.model
   48      def prepare_backend_url(self, action_xml_id, view_type='list', module_name=None):
   49          """ prepare the backend url to the given action, or to the given module view.
   ..
   68          return "/web#%s" % (urlencode(params),)
   69  
   70:     @api.model
   71      def is_module_installed(self, module_name=None):
   72          return module_name in self.env['ir.module.module']._installed()

/home/shivamm/Desktop/odoo-9.0/addons/web_settings_dashboard/models/res_users.py:
    7      _inherit = 'res.users'
    8  
    9:     @api.model
   10      def web_dashboard_create_users(self, emails):
   11  

/home/shivamm/Desktop/odoo-9.0/addons/website/models/web_planner.py:
    8      _inherit = 'web.planner'
    9  
   10:     @api.model
   11      def _get_planner_application(self):
   12          planner = super(WebsitePlanner, self)._get_planner_application()

/home/shivamm/Desktop/odoo-9.0/addons/website_event_track/models/event.py:
   64              self.image = False
   65  
   66:     @api.model
   67      def create(self, vals):
   68          res = super(event_track, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/forum.py:
   39              self.pool['ir.config_parameter'].set_param(cr, SUPERUSER_ID, 'website_forum.uuid', str(uuid.uuid4()), ['base.group_system'])
   40  
   41:     @api.model
   42      def _get_default_faq(self):
   43          fname = modules.get_module_resource('website_forum', 'data', 'forum_default_faq.html')
   ..
  156          self.count_flagged_posts = self.env['forum.post'].search_count(domain)
  157  
  158:     @api.model
  159      def create(self, values):
  160          return super(Forum, self.with_context(mail_create_nolog=True)).create(values)
  161  
  162:     @api.model
  163      def _tag_to_write_vals(self, tags=''):
  164          User = self.env['res.users']
  ...
  396          return content
  397  
  398:     @api.model
  399      def create(self, vals):
  400          if 'content' in vals and vals.get('forum_id'):
  ...
  430          return post
  431  
  432:     @api.model
  433      def check_mail_message_access(self, res_ids, operation, model_name=None):
  434          if operation in ('write', 'unlink') and (not model_name or model_name == 'forum.post'):
  ...
  650          return new_message
  651  
  652:     @api.model
  653      def convert_comment_to_answer(self, message_id, default=None):
  654          """ Tool to convert a comment (mail.message) into an answer (forum.post).
  ...
  774          return _karma_upd[old_vote][new_vote]
  775  
  776:     @api.model
  777      def create(self, vals):
  778          vote = super(Vote, self).create(vals)

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/gamification.py:
    7      _inherit = 'gamification.challenge'
    8  
    9:     @api.model
   10      def _get_categories(self):
   11          res = super(gamification_challenge, self)._get_categories()

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/res_users.py:
   50              self.browse(user_id)['{}_badge'.format(level)] = count
   51  
   52:     @api.model
   53      def _generate_forum_token(self, user_id, email):
   54          """Return a token for email validation. This token is valid for the day
   ..
  104          return True
  105  
  106:     @api.model
  107      def get_serialised_gamification_summary(self, excluded_categories=None):
  108          if isinstance(excluded_categories, list):

/home/shivamm/Desktop/odoo-9.0/addons/website_payment/models/res_config.py:
   11                                         )
   12  
   13:     @api.model
   14      def get_default_acquirer(self, fields):
   15          default_acquirer = False

/home/shivamm/Desktop/odoo-9.0/addons/website_payment/models/website.py:
    5      _inherit = "website"
    6  
    7:     @api.model
    8      def payment_acquirers(self):
    9          return list(self.env['payment.acquirer'].sudo().search([('website_published', '=', True)]))

/home/shivamm/Desktop/odoo-9.0/addons/website_sale_digital/product.py:
   18              ptemplate.attachment_count = prod_tmpl_result.get(ptemplate.id, 0) + sum(prod_attach_result.get(p.id, 0) for p in ptemplate.product_variant_ids)
   19  
   20:     @api.model
   21      def _get_product_template_type(self):
   22          res = super(product_template, self)._get_product_template_type()

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/res_config.py:
   10      website_slide_google_app_key = fields.Char(string='Google Doc Key')
   11  
   12:     @api.model
   13      def get_default_website_slide_google_app_key(self, fields):
   14          website_slide_google_app_key = False

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/slides.py:
  324  
  325  
  326:     @api.model
  327      def create(self, values):
  328          if not values.get('index_content'):
  ...
  356          return res
  357  
  358:     @api.model
  359      def check_field_access_rights(self, operation, fields):
  360          """ As per channel access configuration (visibility)
  ...
  411      # --------------------------------------------------
  412  
  413:     @api.model
  414      def _fetch_data(self, base_url, data, content_type=False):
  415          result = {'values': dict()}
  ...
  477          return {'values': values}
  478  
  479:     @api.model
  480      def _parse_google_document(self, document_id, only_preview_fields):
  481          def get_slide_type(vals):

284 matches across 95 files
