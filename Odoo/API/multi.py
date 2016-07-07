Searching 18994 files for "@api.multi"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
   47      _order = "code"
   48  
   49:     #@api.multi
   50      #def _compute_has_unreconciled_entries(self):
   51      #    print "ici dedans"
   ..
   89      #                account.has_unreconciled_entries = True
   90  
   91:     @api.multi
   92      @api.constrains('internal_type', 'reconcile')
   93      def _check_reconcile(self):
   ..
  138              self.reconcile = True
  139  
  140:     @api.multi
  141      @api.depends('name', 'code')
  142      def name_get(self):
  ...
  153          return super(AccountAccount, self).copy(default)
  154  
  155:     @api.multi
  156      def write(self, vals):
  157          # Dont allow changing the company_id when account_move_line already exist
  ...
  163          return super(AccountAccount, self).write(vals)
  164  
  165:     @api.multi
  166      def unlink(self):
  167          if self.env['account.move.line'].search([('account_id', 'in', self.ids)], limit=1):
  ...
  174          return super(AccountAccount, self).unlink()
  175  
  176:     @api.multi
  177      def mark_as_reconciled(self):
  178          return self.write({'last_time_entries_checked': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)})
  ...
  282              self.default_debit_account_id = self.default_credit_account_id
  283  
  284:     @api.multi
  285      def unlink(self):
  286          bank_accounts = self.mapped('bank_account_id')
  ...
  297          return super(AccountJournal, self).copy(default)
  298  
  299:     @api.multi
  300      def write(self, vals):
  301          for journal in self:
  ...
  439          }).id
  440  
  441:     @api.multi
  442      @api.depends('name', 'currency_id', 'company_id', 'company_id.currency_id')
  443      def name_get(self):
  ...
  449          return res
  450  
  451:     @api.multi
  452      @api.depends('inbound_payment_method_ids', 'outbound_payment_method_ids')
  453      def _methods_compute(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
   39      cashbox_lines_ids = fields.One2many('account.cashbox.line', 'cashbox_id', string='Cashbox Lines')
   40  
   41:     @api.multi
   42      def validate(self):
   43          bnk_stmt_id = self.env.context.get('bank_statement_id', False) or self.env.context.get('active_id', False)
   ..
   62      _description = 'Account Bank Statement closing balance'
   63  
   64:     @api.multi
   65      def validate(self):
   66          bnk_stmt_id = self.env.context.get('active_id', False)
   ..
  100          return False
  101  
  102:     @api.multi
  103      def _set_opening_balance(self, journal_id):
  104          last_bnk_stmt = self.search([('journal_id', '=', journal_id), ('state', '=', 'confirm')], order="date_done desc", limit=1)
  ...
  156          self._set_opening_balance(self.journal_id.id)
  157  
  158:     @api.multi
  159      def _balance_check(self):
  160          for stmt in self:
  ...
  193          return super(AccountBankStatement, self).create(vals)
  194  
  195:     @api.multi
  196      def unlink(self):
  197          for statement in self:
  ...
  202          return super(AccountBankStatement, self).unlink()
  203  
  204:     @api.multi
  205      def open_cashbox_id(self):
  206          context = dict(self.env.context or {})
  ...
  219              }
  220  
  221:     @api.multi
  222      def button_cancel(self):
  223          for statement in self:
  ...
  226          self.state = 'open'
  227  
  228:     @api.multi
  229      def check_confirm_bank(self):
  230          if self.journal_type == 'cash' and not self.currency_id.is_zero(self.difference):
  ...
  235          return self.button_confirm_bank()
  236  
  237:     @api.multi
  238      def button_confirm_bank(self):
  239          self._balance_check()
  ...
  253          statements.write({'state': 'confirm', 'date_done': time.strftime("%Y-%m-%d %H:%M:%S")})
  254  
  255:     @api.multi
  256      def button_journal_entries(self):
  257          context = dict(self._context or {})
  ...
  268          }
  269  
  270:     @api.multi
  271      def button_open(self):
  272          """ Changes statement state to Running."""
  ...
  282              statement.state = 'open'
  283  
  284:     @api.multi
  285      def reconciliation_widget_preprocess(self):
  286          """ Get statement lines of the specified statements or all unreconciled statement lines and try to automatically reconcile them / find them a partner.
  ...
  343          }
  344  
  345:     @api.multi
  346      def link_bank_to_partner(self):
  347          for statement in self:
  ...
  393              raise ValidationError(_('If "Amount Currency" is specified, then "Amount" must be as well.'))
  394  
  395:     @api.multi
  396      def unlink(self):
  397          for line in self:
  ...
  404          return [('journal_entry_ids', '=', False), ('account_id', '=', False)]
  405  
  406:     @api.multi
  407      def button_cancel_reconciliation(self):
  408          # TOCKECK : might not behave as expected in case of reconciliations (match statement line with already
  ...
  422      ####################################################
  423  
  424:     @api.multi
  425      def get_data_for_reconciliation_widget(self, excluded_ids=None):
  426          """ Returns the data required to display a reconciliation widget, for each statement line in self """
  ...
  480          return data
  481  
  482:     @api.multi
  483      def get_move_lines_for_reconciliation_widget(self, excluded_ids=None, str=False, offset=0, limit=None):
  484          """ Returns move lines for the bank statement reconciliation widget, formatted as a list of dicts
  ...
  600          pass
  601  
  602:     @api.multi
  603      def auto_reconcile(self):
  604          """ Try to automatically reconcile the statement.line ; return the counterpart journal entry/ies if the automatic reconciliation succeeded, False otherwise.

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
  338          return super(AccountInvoice, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
  339  
  340:     @api.multi
  341      def invoice_print(self):
  342          """ Print the invoice and mark it as sent, so that we can see more
  ...
  347          return self.env['report'].get_action(self, 'account.report_invoice')
  348  
  349:     @api.multi
  350      def action_invoice_sent(self):
  351          """ Open a window to compose an email, with the edi invoice template
  ...
  375          }
  376  
  377:     @api.multi
  378      def compute_taxes(self):
  379          """Function used in other module to compute the taxes on a fresh invoice created (onchanges did not applied)"""
  ...
  395          return self.with_context(ctx).write({'invoice_line_ids': []})
  396  
  397:     @api.multi
  398      def confirm_paid(self):
  399          return self.write({'state': 'paid'})
  400  
  401:     @api.multi
  402      def unlink(self):
  403          for invoice in self:
  ...
  481              self.date_due = max(line[0] for line in pterm_list)
  482  
  483:     @api.multi
  484      def action_cancel_draft(self):
  485          # go from canceled state to draft state
  ...
  489          return True
  490  
  491:     @api.multi
  492      def get_taxes_values(self):
  493          tax_grouped = {}
  ...
  521          return tax_grouped
  522  
  523:     @api.multi
  524      def register_payment(self, payment_line, writeoff_acc_id=False, writeoff_journal_id=False):
  525          """ Reconcile payable/receivable lines from the invoice with payment_line """
  ...
  533          return self.browse(cr, uid, id, context).register_payment(self.pool.get('account.move.line').browse(cr, uid, payment_id, context))
  534  
  535:     @api.multi
  536      def action_date_assign(self):
  537          for inv in self:
  ...
  540          return True
  541  
  542:     @api.multi
  543      def finalize_invoice_move_lines(self, move_lines):
  544          """ finalize_invoice_move_lines(move_lines) -> move_lines
  ...
  552          return move_lines
  553  
  554:     @api.multi
  555      def compute_invoice_totals(self, company_currency, invoice_move_lines):
  556          total = 0
  ...
  652          return line
  653  
  654:     @api.multi
  655      def action_move_create(self):
  656          """ Creates invoice related analytics and financial move lines """
  ...
  750          return True
  751  
  752:     @api.multi
  753      def invoice_validate(self):
  754          for invoice in self:
  ...
  781          }
  782  
  783:     @api.multi
  784      def action_cancel(self):
  785          moves = self.env['account.move']
  ...
  803      ###################
  804  
  805:     @api.multi
  806      def name_get(self):
  807          TYPES = {
  ...
  895          return values
  896  
  897:     @api.multi
  898      @api.returns('self')
  899      def refund(self, date_invoice=None, date=None, description=None, journal_id=None):
  ...
  948          return recs.pay_and_reconcile(pay_journal, pay_amount, date, writeoff_acc)
  949  
  950:     @api.multi
  951      def _track_subtype(self, init_values):
  952          self.ensure_one()
  ...
  959          return super(AccountInvoice, self)._track_subtype(init_values)
  960  
  961:     @api.multi
  962      def _get_tax_amount_by_group(self):
  963          self.ensure_one()
  ...
  977      _order = "invoice_id,sequence,id"
  978  
  979:     @api.multi
  980      def _get_analytic_line(self):
  981          ref = self.invoice_id.number
  ...
 1282      _inherit = 'mail.compose.message'
 1283  
 1284:     @api.multi
 1285      def send_mail(self, auto_commit=False):
 1286          context = self._context

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_journal_dashboard.py:
   26      show_on_dashboard = fields.Boolean(string='Show journal on dashboard', help="Whether this journal should be displayed on the dashboard or not", default=True)
   27  
   28:     @api.multi
   29      def toggle_favorite(self):
   30          self.write({'show_on_dashboard': False if self.show_on_dashboard else True})
   31          return False
   32  
   33:     @api.multi
   34      def get_line_graph_datas(self):
   35          data = []
   ..
   90          return [{'values': data, 'area': True}]
   91  
   92:     @api.multi
   93      def get_bar_graph_datas(self):
   94          data = []
   ..
  133          return [{'values': data}]
  134  
  135:     @api.multi
  136      def get_journal_dashboard_datas(self):
  137          number_to_reconcile = last_balance = account_sum = 0
  ...
  192          }
  193  
  194:     @api.multi
  195      def action_create_new(self):
  196          ctx = self._context.copy()
  ...
  220          }
  221  
  222:     @api.multi
  223      def create_cash_statement(self):
  224          ctx = self._context.copy()
  ...
  233          }
  234  
  235:     @api.multi
  236      def action_open_reconcile(self):
  237          if self.type in ['bank', 'cash']:
  ...
  256              }
  257  
  258:     @api.multi
  259      def open_action(self):
  260          """return action based on type for related journals"""
  ...
  295          return action
  296  
  297:     @api.multi
  298      def open_spend_money(self):
  299          return self.open_payments_action('outbound')
  300  
  301:     @api.multi
  302      def open_collect_money(self):
  303          return self.open_payments_action('inbound')
  304  
  305:     @api.multi
  306      def open_transfer_money(self):
  307          return self.open_payments_action('transfer')
  308  
  309:     @api.multi
  310      def open_payments_action(self, payment_type):
  311          ctx = self._context.copy()
  ...
  321              return action
  322  
  323:     @api.multi
  324      def open_action_with_context(self):
  325          action_name = self.env.context.get('action_name', False)
  ...
  338          return action
  339  
  340:     @api.multi
  341      def create_bank_statement(self):
  342          """return action to create a bank statements. This button should be called only on journals with type =='bank'"""

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_move.py:
   20      _order = 'date desc, id desc'
   21  
   22:     @api.multi
   23      @api.depends('name', 'state')
   24      def name_get(self):
   ..
   32          return result
   33  
   34:     @api.multi
   35      @api.depends('line_ids.debit', 'line_ids.credit')
   36      def _amount_compute(self):
   ..
   65          self.currency_id = self.company_id.currency_id or self.env.user.company_id.currency_id
   66  
   67:     @api.multi
   68      def _get_default_journal(self):
   69          if self.env.context.get('default_journal_type'):
   ..
  101          return move
  102  
  103:     @api.multi
  104      def write(self, vals):
  105          if 'line_ids' in vals:
  ...
  110          return res
  111  
  112:     @api.multi
  113      def post(self):
  114          invoice = self._context.get('invoice', False)
  ...
  137          return self.write({'state': 'posted'})
  138  
  139:     @api.multi
  140      def button_cancel(self):
  141          for move in self:
  ...
  149          return True
  150  
  151:     @api.multi
  152      def unlink(self):
  153          for move in self:
  ...
  157          return super(AccountMove, self).unlink()
  158  
  159:     @api.multi
  160      def _post_validate(self):
  161          for move in self:
  ...
  166          return self._check_lock_date()
  167  
  168:     @api.multi
  169      def _check_lock_date(self):
  170          for move in self:
  ...
  176          return True
  177  
  178:     @api.multi
  179      def assert_balanced(self):
  180          if not self.ids:
  ...
  193          return True
  194  
  195:     @api.multi
  196      def reverse_moves(self, date=None, journal_id=None):
  197          date = date or fields.Date.today()
  ...
  369      ]
  370  
  371:     @api.multi
  372      @api.constrains('currency_id', 'account_id')
  373      def _check_currency(self):
  ...
  377                      raise UserError(_('The selected account of your Journal Entry forces to provide a secondary currency. You should remove the secondary currency on the account or select a multi-currency view on the journal.'))
  378  
  379:     @api.multi
  380      @api.constrains('currency_id', 'amount_currency')
  381      def _check_currency_and_amount(self):
  ...
  384                  raise UserError(_("You cannot create journal items with a secondary currency without filling both 'currency' and 'amount currency' field."))
  385  
  386:     @api.multi
  387      @api.constrains('amount_currency')
  388      def _check_currency_amount(self):
  ...
  765          return self.auto_reconcile_lines()
  766  
  767:     @api.multi
  768      def reconcile(self, writeoff_acc_id=False, writeoff_journal_id=False):
  769          #Perform all checks on lines
  ...
  848          return writeoff_move.line_ids.filtered(lambda r: r.account_id == self[0].account_id)
  849  
  850:     @api.multi
  851      def remove_move_reconcile(self):
  852          """ Undo a reconciliation """
  ...
  986          return new_line
  987  
  988:     @api.multi
  989      def unlink(self):
  990          self._update_check()
  ...
  998          return result
  999  
 1000:     @api.multi
 1001      def write(self, vals):
 1002          if vals.get('tax_line_id') or vals.get('tax_ids'):
 ....
 1025          return result
 1026  
 1027:     @api.multi
 1028      def _update_check(self):
 1029          """ Raise Warning to cause rollback if the move is posted, some entries are reconciled or the move is older than the lock date"""
 ....
 1044      ####################################################
 1045  
 1046:     @api.multi
 1047      @api.depends('ref', 'move_id')
 1048      def name_get(self):
 ....
 1066          return debit, credit, amount_currency
 1067  
 1068:     @api.multi
 1069      def create_analytic_lines(self):
 1070          """ Create analytic items upon validation of an account.move.line having an analytic account. This
 ....
 1203          return res
 1204  
 1205:     @api.multi
 1206      def unlink(self):
 1207          """ When removing a link between entries, we need to revert the eventual journal entries we created to book the

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
  153          }
  154  
  155:     @api.multi
  156      def create_payment(self):
  157          payment = self.env['account.payment'].create(self.get_payment_vals())
  ...
  254          return self.invoice_ids
  255  
  256:     @api.multi
  257      def button_journal_entries(self):
  258          return {
  ...
  266          }
  267  
  268:     @api.multi
  269      def button_invoices(self):
  270          return {
  ...
  278          }
  279  
  280:     @api.multi
  281      def button_dummy(self):
  282          return True
  283  
  284:     @api.multi
  285      def cancel(self):
  286          for rec in self:
  ...
  292              rec.state = 'draft'
  293  
  294:     @api.multi
  295      def unlink(self):
  296          if any(rec.state != 'draft' for rec in self):
  ...
  298          return super(account_payment, self).unlink()
  299  
  300:     @api.multi
  301      def post(self):
  302          """ Create the journal items for the payment and update the payment's state to 'posted'.

/home/shivamm/Desktop/odoo-9.0/addons/account/models/chart_template.py:
   42      tag_ids = fields.Many2many('account.account.tag', 'account_account_template_account_tag', string='Account tag', help="Optional tags you may want to assign for custom reporting")
   43  
   44:     @api.multi
   45      @api.depends('name', 'code')
   46      def name_get(self):
   ..
  110              wizard.execute()
  111  
  112:     @api.multi
  113      def open_select_template_wizard(self):
  114          # Add action to open wizard to select between several templates
  ...
  137          return True
  138  
  139:     @api.multi
  140      def _prepare_all_journals(self, acc_template_ref, company, journals_dict=None):
  141          def _get_default_account(journal_vals, type='debit'):
  ...
  176          return journal_data
  177  
  178:     @api.multi
  179      def generate_properties(self, acc_template_ref, company):
  180          """
  ...
  226          return True
  227  
  228:     @api.multi
  229      def _install_template(self, company, code_digits=None, transfer_account_id=None, obj_wizard=None, acc_ref=None, taxes_ref=None):
  230          """ Recursively load the template objects and create the real objects from them.
  ...
  256          return acc_ref, taxes_ref
  257  
  258:     @api.multi
  259      def _load_template(self, company, code_digits=None, transfer_account_id=None, account_ref=None, taxes_ref=None):
  260          """ Generate all the objects from the templates
  ...
  310          return account_ref, taxes_ref
  311  
  312:     @api.multi
  313      def generate_account(self, tax_template_ref, acc_template_ref, code_digits, company):
  314          """ This method for generating accounts from templates.
  ...
  348          return acc_template_ref
  349  
  350:     @api.multi
  351      def generate_fiscal_position(self, tax_template_ref, acc_template_ref, company):
  352          """ This method generate Fiscal Position, Fiscal Position Accounts and Fiscal Position Taxes from templates.
  ...
  411      ]
  412  
  413:     @api.multi
  414      @api.depends('name', 'description')
  415      def name_get(self):
  ...
  439          }
  440  
  441:     @api.multi
  442      def _generate_tax(self, company):
  443          """ This method generate taxes from templates.
  ...
  684          return True
  685  
  686:     @api.multi
  687      def execute(self):
  688          '''
  ...
  741          return {}
  742  
  743:     @api.multi
  744      def _create_bank_journals_from_o2m(self, company, acc_template_ref):
  745          '''

/home/shivamm/Desktop/odoo-9.0/addons/account/models/company.py:
   46  Best Regards,''')
   47  
   48:     @api.multi
   49      def compute_fiscalyear_dates(self, date):
   50          """ Computes the start and end dates of the fiscalyear where the given 'date' belongs to
   ..
   76                  account.write({'code': self.get_new_account_code(account.code, old_code, new_code, digits)})
   77  
   78:     @api.multi
   79      def write(self, values):
   80          # Reflect the change on accounts

/home/shivamm/Desktop/odoo-9.0/addons/account/models/partner.py:
  229      _description = 'Partner'
  230  
  231:     @api.multi
  232      def onchange_state(self, state_id):
  233          res = super(ResPartner, self).onchange_state(state_id=state_id)
  ...
  241                  country_id=self.country_id.id, state_id=self.state_id.id, zipcode=self.zip)
  242  
  243:     @api.multi
  244      def _credit_debit_get(self):
  245          tables, where_clause, where_params = self.env['account.move.line']._query_get()
  ...
  262                  partner.debit = -val
  263  
  264:     @api.multi
  265      def _asset_difference_search(self, type, args):
  266          if not args:
  ...
  290          return [('id', 'in', map(itemgetter(0), res))]
  291  
  292:     @api.multi
  293      def _credit_search(self, args):
  294          return self._asset_difference_search('receivable', args)
  295  
  296:     @api.multi
  297      def _debit_search(self, args):
  298          return self._asset_difference_search('payable', args)
  299  
  300:     @api.multi
  301      def _invoice_total(self):
  302          account_invoice_report = self.env['account.invoice.report']
  ...
  331              partner.total_invoiced = self.env.cr.fetchone()[0]
  332  
  333:     @api.multi
  334      def _journal_item_count(self):
  335          for partner in self:
  ...
  349          return domain
  350  
  351:     @api.multi
  352      def _compute_issued_total(self):
  353          """ Returns the issued total as will be displayed on partner view """
  ...
  396          self.has_unreconciled_entries = self.env.cr.rowcount == 1
  397  
  398:     @api.multi
  399      def mark_as_reconciled(self):
  400          return self.write({'last_time_entries_checked': time.strftime(DEFAULT_SERVER_DATETIME_FORMAT)})
  ...
  452      bank_account_count = fields.Integer(compute='_compute_bank_count', string="Bank")
  453  
  454:     @api.multi
  455      def _compute_bank_count(self):
  456          bank_data = self.env['res.partner.bank'].read_group([('partner_id', 'in', self.ids)], ['partner_id'], ['partner_id'])

/home/shivamm/Desktop/odoo-9.0/addons/account/models/product.py:
   38          help="This account will be used for invoices instead of the default one to value expenses for the current product.")
   39  
   40:     @api.multi
   41      def write(self, vals):
   42          #TODO: really? i don't see the reason we'd need that constraint..
   ..
   54          return res
   55  
   56:     @api.multi
   57      def _get_product_accounts(self):
   58          return {
   ..
   61          }
   62  
   63:     @api.multi
   64      def get_product_accounts(self, fiscal_pos=None):
   65          accounts = self._get_product_accounts()

/home/shivamm/Desktop/odoo-9.0/addons/account/models/res_config.py:
  196          self.purchase_tax_rate = self.sale_tax_rate or False
  197  
  198:     @api.multi
  199      def set_group_multi_currency(self):
  200          ir_model = self.env['ir.model.data']
  ...
  205          return True
  206  
  207:     @api.multi
  208      def open_bank_accounts(self):
  209          action_rec = self.env['ir.model.data'].xmlid_to_object('account.action_account_bank_journal_form')
  210          return action_rec.read([])[0]
  211  
  212:     @api.multi
  213      def set_transfer_account(self):
  214          if self.transfer_account_id and self.transfer_account_id != self.company_id.transfer_account_id:
  215              self.company_id.write({'transfer_account_id': self.transfer_account_id.id})
  216  
  217:     @api.multi
  218      def set_product_taxes(self):
  219          """ Set the product taxes if they have changed """
  ...
  222          ir_values_obj.sudo().set_default('product.template', "supplier_taxes_id", [self.default_purchase_tax_id.id] if self.default_purchase_tax_id else False, for_all_users=True, company_id=self.company_id.id)
  223  
  224:     @api.multi
  225      def set_chart_of_accounts(self):
  226          """ install a chart of accounts for the given company (if required) """
  ...
  249              self.module_account_accountant = True
  250  
  251:     @api.multi
  252      def open_company(self):
  253          return {

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_aged_partner_balance.py:
  269          return res
  270  
  271:     @api.multi
  272      def render_html(self, data):
  273          self.total_account = []

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_balance.py:
   56  
   57  
   58:     @api.multi
   59      def render_html(self, data):
   60          self.model = self.env.context.get('active_model')

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_financial_report.py:
   13      _description = "Account Report"
   14  
   15:     @api.multi
   16      @api.depends('parent_id', 'parent_id.level')
   17      def _get_level(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_general_ledger.py:
  108          return account_res
  109  
  110:     @api.multi
  111      def render_html(self, data):
  112          self.model = self.env.context.get('active_model')

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_invoice_report.py:
   11      _rec_name = 'date'
   12  
   13:     @api.multi
   14      @api.depends('currency_id', 'date', 'price_total', 'price_average', 'residual')
   15      def _compute_amounts_in_user_currency(self):

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_overdue_report.py:
   31          return res
   32  
   33:     @api.multi
   34      def render_html(self, data):
   35          totals = {}

/home/shivamm/Desktop/odoo-9.0/addons/account/report/account_report_financial.py:
  141          return lines
  142  
  143:     @api.multi
  144      def render_html(self, data):
  145          self.model = self.env.context.get('active_model')

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_financial_report.py:
   35          return result
   36  
   37:     @api.multi
   38      def check_report(self):
   39          res = super(AccountingReport, self).check_report()

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_invoice_refund.py:
   38  
   39  
   40:     @api.multi
   41      def compute_refund(self, mode='refund'):
   42          inv_obj = self.env['account.invoice']
   ..
  122          return True
  123  
  124:     @api.multi
  125      def invoice_refund(self):
  126          data_refund = self.read(['filter_refund'])[0]['filter_refund']

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_invoice_state.py:
   12      _description = "Confirm the selected invoices"
   13  
   14:     @api.multi
   15      def invoice_confirm(self):
   16          context = dict(self._context or {})
   ..
   33      _description = "Cancel the Selected Invoices"
   34  
   35:     @api.multi
   36      def invoice_cancel(self):
   37          context = dict(self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_move_reversal.py:
   12      journal_id = fields.Many2one('account.journal', string='Use Specific Journal', help='If empty, uses the journal of the journal entry to be reversed.')
   13  
   14:     @api.multi
   15      def reverse_moves(self):
   16          ac_move_ids = self._context.get('active_ids', False)

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_reconcile.py:
   30          return res
   31  
   32:     @api.multi
   33      def trans_rec_get(self):
   34          context = self._context or {}
   ..
   45          return {'trans_nbr': len(lines), 'credit': credit, 'debit': debit, 'writeoff': writeoff}
   46  
   47:     @api.multi
   48      def trans_rec_addendum_writeoff(self):
   49          return self.env['account.move.line.reconcile.writeoff'].trans_rec_addendum()
   50  
   51:     @api.multi
   52      def trans_rec_reconcile_partial_reconcile(self):
   53          return self.env['account.move.line.reconcile.writeoff'].trans_rec_reconcile_partial()
   54  
   55:     @api.multi
   56      def trans_rec_reconcile_full(self):
   57          move_lines = self.env['account.move.line'].browse(self._context.get('active_ids', []))
   ..
   73      analytic_id = fields.Many2one('account.analytic.account', string='Analytic Account')
   74  
   75:     @api.multi
   76      def trans_rec_addendum(self):
   77          view = self.env.ref('account.account_move_line_reconcile_writeoff')
   ..
   87          }
   88  
   89:     @api.multi
   90      def trans_rec_reconcile_partial(self):
   91          context = self._context or {}
   ..
   93          return {'type': 'ir.actions.act_window_close'}
   94  
   95:     @api.multi
   96      def trans_rec_reconcile(self):
   97          context = dict(self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_report_common.py:
   28          raise (_('Error!'), _('Not implemented.'))
   29  
   30:     @api.multi
   31      def check_report(self):
   32          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_report_common_account.py:
   13                                          string='Display Accounts', required=True, default='movement')
   14  
   15:     @api.multi
   16      def pre_print_report(self, data):
   17          data['form'].update(self.read(['display_account'])[0])

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_unreconcile.py:
    6      _description = "Account Unreconcile"
    7  
    8:     @api.multi
    9      def trans_unrec(self):
   10          context = dict(self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/account_validate_account_move.py:
    7      _description = "Validate Account Move"
    8  
    9:     @api.multi
   10      def validate_move(self):
   11          context = dict(self._context or {})

/home/shivamm/Desktop/odoo-9.0/addons/account/wizard/pos_box.py:
   10      amount = fields.Float(string='Amount', digits=0, required=True)
   11  
   12:     @api.multi
   13      def run(self):
   14          context = dict(self._context or {})
   ..
   20          return self._run(records)
   21  
   22:     @api.multi
   23      def _run(self, records):
   24          for box in self:

/home/shivamm/Desktop/odoo-9.0/addons/account_analytic_default/account_analytic_default.py:
   88      _inherit = "sale.order.line"
   89  
   90:     @api.multi
   91      def _prepare_invoice_line(self, qty):
   92          res = super(sale_order_line, self)._prepare_invoice_line(qty)

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
   94      type = fields.Selection(related="category_id.type", string='Type', required=True)
   95  
   96:     @api.multi
   97      def unlink(self):
   98          for asset in self:
   ..
  103          return super(AccountAssetAsset, self).unlink()
  104  
  105:     @api.multi
  106      def _get_last_depreciation_date(self):
  107          """
  ...
  159          return undone_dotation_number
  160  
  161:     @api.multi
  162      def compute_depreciation_board(self):
  163          self.ensure_one()
  ...
  213          return True
  214  
  215:     @api.multi
  216      def validate(self):
  217          self.write({'state': 'open'})
  ...
  238              asset.message_post(subject=_('Asset created'), tracking_value_ids=tracking_value_ids)
  239  
  240:     @api.multi
  241      def set_to_close(self):
  242          move_ids = []
  ...
  287              }
  288  
  289:     @api.multi
  290      def set_to_draft(self):
  291          self.write({'state': 'draft'})
  ...
  304          self.currency_id = self.company_id.currency_id.id
  305  
  306:     @api.multi
  307      @api.depends('account_move_ids')
  308      def _entry_count(self):
  ...
  344              self.prorata = False
  345  
  346:     @api.multi
  347      def copy_data(self, default=None):
  348          if default is None:
  ...
  351          return super(AccountAssetAsset, self).copy_data(default)[0]
  352  
  353:     @api.multi
  354      def _compute_entries(self, date):
  355          depreciation_ids = self.env['account.asset.depreciation.line'].search([
  ...
  364          return asset
  365  
  366:     @api.multi
  367      def write(self, vals):
  368          res = super(AccountAssetAsset, self).write(vals)
  ...
  371          return res
  372  
  373:     @api.multi
  374      def open_entries(self):
  375          return {
  ...
  404          self.move_check = bool(self.move_id)
  405  
  406:     @api.multi
  407      def create_move(self, post_move=True):
  408          created_moves = self.env['account.move']
  ...
  459          return [x.id for x in created_moves]
  460  
  461:     @api.multi
  462      def post_lines_and_close_asset(self):
  463          # we re-evaluate the assets to determine whether we can close them
  ...
  469                  asset.write({'state': 'close'})
  470  
  471:     @api.multi
  472      def log_message_when_posted(self):
  473          def _format_message(message_description, tracked_values):
  ...
  490                  line.asset_id.message_post(body=msg)
  491  
  492:     @api.multi
  493      def unlink(self):
  494          for record in self:
  ...
  507      asset_id = fields.Many2one('account.asset.asset', string='Asset', ondelete="restrict")
  508  
  509:     @api.multi
  510      def post(self):
  511          for move in self:

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset_invoice.py:
   11      _inherit = 'account.invoice'
   12  
   13:     @api.multi
   14      def action_move_create(self):
   15          result = super(AccountInvoice, self).action_move_create()

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/wizard/account_asset_change_duration.py:
   58          return res
   59  
   60:     @api.multi
   61      def modify(self):
   62          """ Modifies the duration of asset for calculating depreciation

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/wizard/wizard_asset_compute.py:
    9      date = fields.Date('Account Date', required=True, help="Choose the period for which you want to automatically post the depreciation lines of running assets", default=fields.Date.context_today)
   10  
   11:     @api.multi
   12      def asset_compute(self):
   13          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/account_bank_statement_import/account_bank_statement_import.py:
   28      data_file = fields.Binary(string='Bank Statement File', required=True, help='Get you bank statements in electronic format from your bank and select them here.')
   29  
   30:     @api.multi
   31      def import_file(self):
   32          """ Process the file chosen in the wizard, create bank statement(s) and go to reconciliation. """

/home/shivamm/Desktop/odoo-9.0/addons/account_bank_statement_import/account_journal.py:
    8      bank_statements_source = fields.Selection(selection_add=[("file_import", "File Import")])
    9  
   10:     @api.multi
   11      def import_statement(self):
   12          """return action to import bank/cash statements. This button should be called only on journals with type =='bank'"""

/home/shivamm/Desktop/odoo-9.0/addons/account_bank_statement_import/wizard/journal_creation.py:
    9      journal_id = fields.Many2one('account.journal', delegate=True, required=True, ondelete='cascade')
   10  
   11:     @api.multi
   12      def create_journal(self):
   13          """ Create the journal (the record is automatically created in the process of calling this method) and reprocess the statement """

/home/shivamm/Desktop/odoo-9.0/addons/account_cancel/models/account_bank_statement.py:
    9      _inherit = 'account.bank.statement'
   10  
   11:     @api.multi
   12      def button_draft(self):
   13          self.state = 'open'
   14  
   15:     @api.multi
   16      def button_cancel(self):
   17          return super(BankStatement, self.with_context(bank_statement_cancel=True)).button_cancel()
   ..
   21      _inherit = 'account.bank.statement.line'
   22  
   23:     @api.multi
   24      def cancel(self):
   25          if not self.env.context.get('bank_statement_cancel'):

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_journal_dashboard.py:
    6      _inherit = "account.journal"
    7  
    8:     @api.multi
    9      def get_journal_dashboard_datas(self):
   10          domain_checks_to_print = [
   ..
   18          )
   19  
   20:     @api.multi
   21      def action_checks_to_print(self):
   22          return {

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/account_payment.py:
   89          return super(account_payment, self.sudo()).create(vals)
   90  
   91:     @api.multi
   92      def print_checks(self):
   93          """ Check that the recordset is valid, set the payments state to sent and call print_checks() """
   ..
  126              return self.do_print_checks()
  127  
  128:     @api.multi
  129      def unmark_sent(self):
  130          self.write({'state': 'posted'})
  131  
  132:     @api.multi
  133      def do_print_checks(self):
  134          """ This method is a hook for l10n_xx_check_printing modules to implement actual check printing capabilities """

/home/shivamm/Desktop/odoo-9.0/addons/account_check_printing/wizard/print_pre_numbered_checks.py:
    9      next_check_number = fields.Integer('Next Check Number', required=True)
   10  
   11:     @api.multi
   12      def print_checks(self):
   13          check_number = self.next_check_number

/home/shivamm/Desktop/odoo-9.0/addons/account_tax_cash_basis/tax_cash_basis.py:
  109          return res
  110  
  111:     @api.multi
  112      def unlink(self):
  113          move = self.env['account.move'].search([('tax_cash_basis_rec_id', 'in', self._ids)])

/home/shivamm/Desktop/odoo-9.0/addons/account_test/report/account_test_report.py:
   58          return result
   59  
   60:     @api.multi
   61      def render_html(self, data=None):
   62          Report = self.env['report']

/home/shivamm/Desktop/odoo-9.0/addons/account_voucher/account_voucher.py:
   23          return self.env.user.company_id.currency_id.id
   24  
   25:     @api.multi
   26      @api.depends('name', 'number')
   27      def name_get(self):
   ..
   43          return self.env['account.journal'].search(domain, limit=1)
   44  
   45:     @api.multi
   46      @api.depends('tax_correction', 'line_ids.price_subtotal')
   47      def _compute_total(self):
   ..
  117                      if self.voucher_type == 'sale' else self.journal_id.default_credit_account_id
  118  
  119:     @api.multi
  120      def button_proforma_voucher(self):
  121          self.signal_workflow('proforma_voucher')
  122          return {'type': 'ir.actions.act_window_close'}
  123  
  124:     @api.multi
  125      def proforma_voucher(self):
  126          self.action_move_line_create()
  127  
  128:     @api.multi
  129      def action_cancel_draft(self):
  130          self.create_workflow()
  131          self.write({'state': 'draft'})
  132  
  133:     @api.multi
  134      def cancel_voucher(self):
  135          for voucher in self:
  ...
  138          self.write({'state': 'cancel', 'move_id': False})
  139  
  140:     @api.multi
  141      def unlink(self):
  142          for voucher in self:
  ...
  145          return super(AccountVoucher, self).unlink()
  146  
  147:     @api.multi
  148      def first_move_line_get(self, move_id, company_currency, current_currency):
  149          debit = credit = 0.0
  ...
  172          return move_line
  173  
  174:     @api.multi
  175      def account_move_get(self):
  176          if self.number:
  ...
  192          return move
  193  
  194:     @api.multi
  195      def _convert_amount(self, amount):
  196          '''
  ...
  207              return voucher.currency_id.compute(amount, voucher.company_id.currency_id)
  208  
  209:     @api.multi
  210      def voucher_move_line_create(self, line_total, move_id, company_currency, current_currency):
  211          '''
  ...
  247          return line_total
  248  
  249:     @api.multi
  250      def action_move_line_create(self):
  251          '''
  ...
  292          return True
  293  
  294:     @api.multi
  295      def _track_subtype(self, init_values):
  296          if 'state' in init_values:
  ...
  336          return accounts['expense']
  337  
  338:     @api.multi
  339      def product_id_change(self, product_id, partner_id=False, price_unit=False, company_id=None, currency_id=None, type=None):
  340          context = self._context

/home/shivamm/Desktop/odoo-9.0/addons/analytic/models/analytic.py:
   18      _order = 'code, name asc'
   19  
   20:     @api.multi
   21      def _compute_debit_credit_balance(self):
   22          analytic_line_obj = self.env['account.analytic.line']
   ..
   61      currency_id = fields.Many2one(related="company_id.currency_id", string="Currency", readonly=True)
   62  
   63:     @api.multi
   64      def name_get(self):
   65          res = []

/home/shivamm/Desktop/odoo-9.0/addons/base_iban/base_iban.py:
   64          return super(ResPartnerBank, self).create(vals)
   65  
   66:     @api.multi
   67      def write(self, vals):
   68          if (vals.get('acc_type') == 'iban') and vals.get('acc_number'):

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/res_partner.py:
    7      im_status = fields.Char('IM Status', compute='_compute_im_status')
    8  
    9:     @api.multi
   10      def _compute_im_status(self):
   11          self.env.cr.execute("""

/home/shivamm/Desktop/odoo-9.0/addons/bus/models/res_users.py:
    9      im_status = fields.Char('IM Status', compute='_compute_im_status')
   10  
   11:     @api.multi
   12      def _compute_im_status(self):
   13          """ Compute the im_status of the users """

/home/shivamm/Desktop/odoo-9.0/addons/crm/wizard/crm_lead_lost.py:
   10      lost_reason_id = fields.Many2one('crm.lost.reason', 'Lost Reason')
   11  
   12:     @api.multi
   13      def action_lost_reason_apply(self):
   14          res = False

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/delivery_carrier.py:
  150          self.state_ids = [(6, 0, self.state_ids.filtered(lambda state: state.id in self.country_ids.mapped('state_ids').ids).ids)]
  151  
  152:     @api.multi
  153      def verify_carrier(self, contact):
  154          self.ensure_one()
  ...
  163          return self
  164  
  165:     @api.multi
  166      def create_price_rules(self):
  167          PriceRule = self.env['delivery.price.rule']
  ...
  210          return res
  211  
  212:     @api.multi
  213      def write(self, vals):
  214          res = super(DeliveryCarrier, self).write(vals)
  ...
  216          return res
  217  
  218:     @api.multi
  219      def get_price_available(self, order):
  220          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/product_template.py:
    8      _inherit = 'product.template'
    9  
   10:     @api.multi
   11      def write(self, vals):
   12          res = super(ProductTemplate, self).write(vals)

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/sale_order.py:
   30              self.carrier_id = self.partner_id.property_delivery_carrier_id
   31  
   32:     @api.multi
   33      def action_confirm(self):
   34          res = super(SaleOrder, self).action_confirm()
   ..
   37          return res
   38  
   39:     @api.multi
   40      def _delivery_unset(self):
   41          self.env['sale.order.line'].search([('order_id', 'in', self.ids), ('is_delivery', '=', True)]).unlink()
   42  
   43:     @api.multi
   44      def delivery_set(self):
   45  

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/stock_move.py:
   22              move.weight = (move.product_qty * move.product_id.weight)
   23  
   24:     @api.multi
   25      def action_confirm(self):
   26          """

/home/shivamm/Desktop/odoo-9.0/addons/delivery/models/stock_picking.py:
   69              picking.weight = sum(move.weight for move in picking.move_lines if move.state != 'cancel')
   70  
   71:     @api.multi
   72      def do_transfer(self):
   73          self.ensure_one()
   ..
   80          return res
   81  
   82:     @api.multi
   83      def send_to_shipper(self):
   84          self.ensure_one()
   ..
   89          self.message_post(body=msg)
   90  
   91:     @api.multi
   92      def _add_delivery_cost_to_so(self):
   93          self.ensure_one()
   ..
   96              sale_order._create_delivery_line(self.carrier_id, self.carrier_price)
   97  
   98:     @api.multi
   99      def open_website_url(self):
  100          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
   86          readonly=True, compute='_compute_seats')
   87  
   88:     @api.multi
   89      @api.depends('seats_max', 'registration_ids.state')
   90      def _compute_seats(self):
   ..
  182      event_logo = fields.Html(string='Event Logo')
  183  
  184:     @api.multi
  185      @api.depends('name', 'date_begin', 'date_end')
  186      def name_get(self):
  ...
  213          return res
  214  
  215:     @api.multi
  216      def write(self, vals):
  217          res = super(event_event, self).write(vals)
  ...
  247              self.reply_to = self.event_type_id.default_reply_to
  248  
  249:     @api.multi
  250      def action_event_registration_report(self):
  251          res = self.env['ir.actions.act_window'].for_xml_id('event', 'action_report_event_registration')
  ...
  298              raise UserError(_('No more seats available for this event.'))
  299  
  300:     @api.multi
  301      def _check_auto_confirmation(self):
  302          if self._context.get('registration_force_draft'):
  ...
  369                  self.phone = self.phone or contact.phone
  370  
  371:     @api.multi
  372      def message_get_suggested_recipients(self):
  373          recipients = super(event_registration, self).message_get_suggested_recipients()
  ...
  379          return recipients
  380  
  381:     @api.multi
  382      def action_send_badge_email(self):
  383          """ Open a window to compose an email, with the template - 'event_badge'

/home/shivamm/Desktop/odoo-9.0/addons/event/wizard/event_confirm.py:
    9      _name = "event.confirm"
   10  
   11:     @api.multi
   12      def confirm(self):
   13          events = self.env['event.event'].browse(self._context.get('event_ids', []))

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
   96      seats_used = fields.Integer(compute='_compute_seats', store=True)
   97  
   98:     @api.multi
   99      @api.depends('seats_max', 'registration_ids.state')
  100      def _compute_seats(self):
  ...
  153              raise UserError(_('No more available seats for this ticket'))
  154  
  155:     @api.multi
  156      def _check_auto_confirmation(self):
  157          res = super(event_registration, self)._check_auto_confirmation()

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/sale_order.py:
   51          self.update(values)
   52  
   53:     @api.multi
   54      def _update_registrations(self, confirm=True, registration_data=None):
   55          """ Create or update registrations linked to a sale order line. A sale

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/wizard/event_edit_registration.py:
   46          return res
   47  
   48:     @api.multi
   49      def action_make_registration(self):
   50          Registration = self.env['event.registration']

/home/shivamm/Desktop/odoo-9.0/addons/exam/models/exam.py:
   33      day_of_week = fields.Char('Week Day')
   34  
   35:     @api.multi
   36      def on_change_date_day(self, exm_date):
   37          val = {}
   ..
   41          return {'value': val}
   42  
   43:     @api.multi
   44      def _check_date(self):
   45          for line in self:
   ..
   81                               readonly=True, default='draft')
   82  
   83:     @api.multi
   84      def set_to_draft(self):
   85          self.write({'state': 'draft'})
   86  
   87:     @api.multi
   88      def set_running(self):
   89          if self.exam_timetable_ids:
   ..
   93                               _('You must add one Exam Schedule'))
   94  
   95:     @api.multi
   96      def set_finish(self):
   97          self.write({'state': 'finished'})
   98  
   99:     @api.multi
  100      def set_cancel(self):
  101          self.write({'state': 'cancelled'})
  102  
  103:     @api.multi
  104      def _validate_date(self):
  105          for exm in self:
  ...
  127      write_date = fields.Date("Updated date", help="Exam Updated Date")
  128  
  129:     @api.multi
  130      def on_change_stadard_name(self, standard_id):
  131          val = {}
  ...
  158              self.total = total
  159  
  160:     @api.multi
  161      def _compute_per(self):
  162          res = {}
  ...
  202              self.result = 'Fail'
  203  
  204:     @api.multi
  205      def on_change_student(self, student, exam_id, standard_id):
  206          val = {}
  ...
  241      color = fields.Integer('Color')
  242  
  243:     @api.multi
  244      def result_confirm(self):
  245          vals = {}
  ...
  254          return True
  255  
  256:     @api.multi
  257      def result_re_access(self):
  258          self.write({'state': 're-access'})
  259  
  260:     @api.multi
  261      def re_result_confirm(self):
  262          res = {}
  ...
  286          return True
  287  
  288:     @api.multi
  289      def re_evaluation_confirm(self):
  290          res = {}
  ...
  315          return True
  316  
  317:     @api.multi
  318      def result_re_evaluation(self):
  319          self.write({'state': 're-evaluation'})
  ...
  419                  self.result = 'Fail'
  420  
  421:     @api.multi
  422      def on_change_student(self, student):
  423          val = {}

/home/shivamm/Desktop/odoo-9.0/addons/exam/wizard/exam_class_result.py:
   13      year_id = fields.Many2one('academic.year', 'Academic Year', required=True)
   14  
   15:     @api.multi
   16      def get_result(self):
   17          domain = []

/home/shivamm/Desktop/odoo-9.0/addons/exam/wizard/exam_create_result.py:
    9      _name = 'exam.create.result'
   10  
   11:     @api.multi
   12      def generate_result(self):
   13          if not self._context.get('active_ids'):

/home/shivamm/Desktop/odoo-9.0/addons/exam_test_quiz/etq_exam.py:
   18      questions = fields.One2many('etq.question','exam_id', string="Questions")
   19  
   20:     @api.multi
   21      def view_quiz(self):
   22          quiz_url = request.httprequest.host_url + "exam/" + str(self.slug)

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/hr_equipment.py:
   44      fold = fields.Boolean(string='Folded in Maintenance Pipe', compute='_compute_fold', store=True)
   45  
   46:     @api.multi
   47      def _compute_equipment_count(self):
   48          equipment_data = self.env['hr.equipment'].read_group([('category_id', 'in', self.ids)], ['category_id'], ['category_id'])
   ..
   51              category.equipment_count = mapped_data.get(category.id, 0)
   52  
   53:     @api.multi
   54      def _compute_maintenance_count(self):
   55          maintenance_data = self.env['hr.equipment.request'].read_group([('category_id', 'in', self.ids)], ['category_id'], ['category_id'])
   ..
   65          return category_id
   66  
   67:     @api.multi
   68      def unlink(self):
   69          for category in self:
   ..
   79      _description = 'Equipment'
   80  
   81:     @api.multi
   82      def _track_subtype(self, init_values):
   83          self.ensure_one()
   ..
   86          return super(HrEquipment, self)._track_subtype(init_values)
   87  
   88:     @api.multi
   89      def name_get(self):
   90          result = []
   ..
  167          return equipment
  168  
  169:     @api.multi
  170      def write(self, vals):
  171          user_ids = []
  ...
  183          return super(HrEquipment, self).write(vals)
  184  
  185:     @api.multi
  186      def _read_group_category_ids(self, domain, read_group_order=None, access_rights_uid=None):
  187          """ Read group customization in order to display all the category in the
  ...
  222          return self.env['hr.equipment.stage'].search([], limit=1)
  223  
  224:     @api.multi
  225      def _track_subtype(self, init_values):
  226          self.ensure_one()
  ...
  248  
  249  
  250:     @api.multi
  251      def archive_equipment_request(self):
  252          self.write({'active': False})
  253  
  254:     @api.multi
  255      def reset_equipment_request(self):
  256          """ Reinsert the equipment request into the maintenance pipe in the first stage"""
  ...
  291          return result
  292  
  293:     @api.multi
  294      def write(self, vals):
  295          # Overridden to reset the kanban_state to normal whenever
  ...
  303          return super(HrEquipmentRequest, self).write(vals)
  304  
  305:     @api.multi
  306      def _read_group_stage_ids(self, domain, read_group_order=None, access_rights_uid=None):
  307          """ Read group customization in order to display all the stages in the

/home/shivamm/Desktop/odoo-9.0/addons/hr_equipment/models/res_config.py:
   12      alias_domain = fields.Char("Alias Domain")
   13  
   14:     @api.multi
   15      def get_default_alias_equipment(self):
   16          alias_name = False
   ..
   20          return {'equipment_alias_prefix': alias_name}
   21  
   22:     @api.multi
   23      def set_default_alias_equipment(self):
   24          for record in self:
   ..
   30          return True
   31  
   32:     @api.multi
   33      def get_default_alias_domain(self):
   34          alias_domain = self.env['ir.config_parameter'].get_param("mail.catchall.domain")

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/models/account_move_line.py:
    8      _inherit = "account.move.line"
    9  
   10:     @api.multi
   11      def reconcile(self, writeoff_acc_id=False, writeoff_journal_id=False):
   12          res = super(AccountMoveLine, self).reconcile(writeoff_acc_id=writeoff_acc_id, writeoff_journal_id=writeoff_journal_id)

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/models/hr_expense.py:
   52              expense.total_amount = taxes.get('total_included')
   53  
   54:     @api.multi
   55      def _compute_attachment_number(self):
   56          attachment_data = self.env['ir.attachment'].read_group([('res_model', '=', 'hr.expense'), ('res_id', 'in', self.ids)], ['res_id'], ['res_id'])
   ..
   95          return hr_expense
   96  
   97:     @api.multi
   98      def write(self, vals):
   99          res = super(HrExpense, self).write(vals)
  ...
  102          return res
  103  
  104:     @api.multi
  105      def unlink(self):
  106          if any(expense.state not in ['draft', 'cancel'] for expense in self):
  ...
  108          return super(HrExpense, self).unlink()
  109  
  110:     @api.multi
  111      def submit_expenses(self):
  112          if any(expense.state != 'draft' for expense in self):
  ...
  114          self.write({'state': 'submit'})
  115  
  116:     @api.multi
  117      def approve_expenses(self):
  118          self.write({'state': 'approve'})
  119  
  120:     @api.multi
  121      def refuse_expenses(self, reason):
  122          self.write({'state': 'cancel'})
  ...
  125              self.message_post(body=body, partner_ids=[self.employee_id.user_id.partner_id.id])
  126  
  127:     @api.multi
  128      def paid_expenses(self):
  129          self.write({'state': 'done'})
  130  
  131:     @api.multi
  132      def reset_expenses(self):
  133          return self.write({'state': 'draft'})
  134  
  135:     @api.multi
  136      def _track_subtype(self, init_values):
  137          self.ensure_one()
  ...
  168          }
  169  
  170:     @api.multi
  171      def _compute_expense_totals(self, company_currency, account_move_lines):
  172          '''
  ...
  195          return total, total_currency, account_move_lines
  196  
  197:     @api.multi
  198      def action_move_create(self):
  199          '''
  ...
  251          return move.post()
  252  
  253:     @api.multi
  254      def _move_line_get(self):
  255          account_move = []
  ...
  292          return account_move
  293  
  294:     @api.multi
  295      def action_get_attachment_view(self):
  296          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/hr_expense/wizard/hr_expense_refuse_reason.py:
   12      description = fields.Char(string='Reason', required=True)
   13  
   14:     @api.multi
   15      def expense_refuse_reason(self):
   16          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/hr_holidays/hr_department.py:
   10      _inherit = 'hr.department'
   11  
   12:     @api.multi
   13      def _compute_leave_count(self):
   14          Holiday = self.env['hr.holidays']
   ..
   40  
   41  
   42:     @api.multi
   43      def _compute_total_employee(self):
   44          emp_data = self.env['hr.employee'].read_group([('department_id', 'in', self.ids)], ['department_id'], ['department_id'])

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_department.py:
   13          compute='_compute_recruitment_stats', string='Expected Employee')
   14  
   15:     @api.multi
   16      def _compute_new_applicant_count(self):
   17          applicant_data = self.env['hr.applicant'].read_group(
   ..
   22              department.new_applicant_count = result.get(department.id, 0)
   23  
   24:     @api.multi
   25      def _compute_recruitment_stats(self):
   26          job_data = self.env['hr.job'].read_group(

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_employee.py:
   10                                            search='_search_newly_hired_employee')
   11  
   12:     @api.multi
   13      def _compute_newly_hired_employee(self):
   14          read_group_result = self.env['hr.applicant'].read_group(
   ..
   23          return [('id', 'in', applicants.ids)]
   24  
   25:     @api.multi
   26      def _broadcast_welcome(self):
   27          """ Broadcast the welcome message to all users in the employee company. """

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_job.py:
   54              job.documents_count = len(job.document_ids)
   55  
   56:     @api.multi
   57      def _compute_application_count(self):
   58          read_group_result = self.env['hr.applicant'].read_group([('job_id', '=', self.id)], ['job_id'], ['job_id'])
   ..
   69          return job
   70  
   71:     @api.multi
   72      def unlink(self):
   73          # Cascade-delete mail aliases as well, as they should not exist without the job position.
   ..
   84              alias_prefix='job+', alias_defaults={'job_id': 'id'}, context=context)
   85  
   86:     @api.multi
   87      def _track_subtype(self, init_values):
   88          if 'state' in init_values and self.state == 'open':
   ..
   90          return super(Job, self)._track_subtype(init_values)
   91  
   92:     @api.multi
   93      def action_print_survey(self):
   94          return self.survey_id.action_print_survey()
   95  
   96:     @api.multi
   97      def action_get_attachment_tree_view(self):
   98          action = self.env.ref('base.action_attachment').read()[0]
   ..
  104          return action
  105  
  106:     @api.multi
  107      def action_set_no_of_recruitment(self, value):
  108          return self.write({'no_of_recruitment': value})

/home/shivamm/Desktop/odoo-9.0/addons/hr_recruitment/models/hr_recruitment.py:
   26      alias_id = fields.Many2one('mail.alias', "Alias ID")
   27  
   28:     @api.multi
   29      def create_alias(self):
   30          campaign = self.env.ref('hr_recruitment.utm_campaign_job')
   ..
  162              self.day_close = (date_closed - date_create).total_seconds() / (24.0 * 3600)
  163  
  164:     @api.multi
  165      def _get_attachment_number(self):
  166          read_group_res = self.env['ir.attachment'].read_group(
  ...
  273          return super(Applicant, self.with_context(mail_create_nolog=True)).create(vals)
  274  
  275:     @api.multi
  276      def write(self, vals):
  277          # user_id change: update date_open
  ...
  300                                                    empty_list_help_document_name=_("job applicants"))).get_empty_list_help(help)
  301  
  302:     @api.multi
  303      def action_get_created_employee(self):
  304          self.ensure_one()
  ...
  307          return action
  308  
  309:     @api.multi
  310      def action_makeMeeting(self):
  311          """ This opens Meeting's calendar view to schedule meeting on current applicant
  ...
  326          return res
  327  
  328:     @api.multi
  329      def action_start_survey(self):
  330          self.ensure_one()
  ...
  338          return self.survey.with_context(survey_token=response.token).action_start_survey()
  339  
  340:     @api.multi
  341      def action_print_survey(self):
  342          """ If response is available then print this response otherwise print survey form (print template of the survey) """
  ...
  348              return self.survey.with_context(survey_token=response.token).action_print_survey()
  349  
  350:     @api.multi
  351      def action_get_attachment_tree_view(self):
  352          attachment_action = self.env.ref('base.action_attachment')
  ...
  356          return action
  357  
  358:     @api.multi
  359      def _track_subtype(self, init_values):
  360          record = self[0]
  ...
  374          return dict((applicant.id, aliases.get(applicant.job_id and applicant.job_id.id or 0, False)) for applicant in applicants)
  375  
  376:     @api.multi
  377      def message_get_suggested_recipients(self):
  378          recipients = super(Applicant, self).message_get_suggested_recipients()
  ...
  405          return super(Applicant, self).message_new(msg, custom_values=defaults)
  406  
  407:     @api.multi
  408      def create_employee_from_applicant(self):
  409          """ Create an hr.employee from the hr.applicants """
  ...
  438          return dict_act_window
  439  
  440:     @api.multi
  441      def archive_applicant(self):
  442          self.write({'active': False})
  443  
  444:     @api.multi
  445      def reset_applicant(self):
  446          """ Reinsert the applicant into the recruitment pipe in the first stage"""

/home/shivamm/Desktop/odoo-9.0/addons/hr_timesheet_sheet/hr_department.py:
    6      _inherit = 'hr.department'
    7  
    8:     @api.multi
    9      def _compute_timesheet_to_approve(self):
   10          timesheet_data = self.env['hr_timesheet_sheet.sheet'].read_group(

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/im_livechat_channel.py:
   73          self.image_small = tools.image_resize_image_small(self.image)
   74  
   75:     @api.multi
   76      def _compute_script_external(self):
   77          view = self.env['ir.model.data'].get_object('im_livechat', 'external_loader')
   ..
   84              record.script_external = view.render(values)
   85  
   86:     @api.multi
   87      def _compute_web_page_link(self):
   88          base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
   ..
   90              record.web_page = "%s/im_livechat/support/%i" % (base_url, record.id)
   91  
   92:     @api.multi
   93      @api.depends('channel_ids')
   94      def _compute_nbr_channel(self):
   ..
   96              record.nbr_channel = len(record.channel_ids)
   97  
   98:     @api.multi
   99      @api.depends('channel_ids.rating_ids')
  100      def _compute_percentage_satisfaction(self):
  ...
  111      # Action Methods
  112      # --------------------------
  113:     @api.multi
  114      def action_join(self):
  115          self.ensure_one()
  116          return self.write({'user_ids': [(4, self._uid)]})
  117  
  118:     @api.multi
  119      def action_quit(self):
  120          self.ensure_one()
  121          return self.write({'user_ids': [(3, self._uid)]})
  122  
  123:     @api.multi
  124      def action_view_rating(self):
  125          """ Action to display the rating relative to the channel, so all rating of the
  ...
  135      # Channel Methods
  136      # --------------------------
  137:     @api.multi
  138      def get_available_users(self):
  139          """ get available user of a given channel

/home/shivamm/Desktop/odoo-9.0/addons/im_livechat/models/mail_channel.py:
   18      livechat_channel_id = fields.Many2one('im_livechat.channel', 'Channel')
   19  
   20:     @api.multi
   21      def _channel_message_notifications(self, message):
   22          """ When a anonymous user create a mail.channel, the operator is not notify (to avoid massive polling when
   ..
   32          return notifications
   33  
   34:     @api.multi
   35      def channel_info(self):
   36          """ Extends the channel header by adding the livechat operator and the 'anonymous' profile

/home/shivamm/Desktop/odoo-9.0/addons/l10n_eu_service/wizard/wizard.py:
   73          string='EU Customers From', required=True)
   74  
   75:     @api.multi
   76      def generate_eu_service(self):
   77          tax_rate = self.env["l10n_eu_service.service_tax_rate"]

/home/shivamm/Desktop/odoo-9.0/addons/l10n_multilang/l10n_multilang.py:
    9      _inherit = 'account.chart.template'
   10  
   11:     @api.multi
   12      def process_translations(self, langs, in_field, in_ids, out_ids):
   13          """
   ..
   43          return True
   44  
   45:     @api.multi
   46      def process_coa_translations(self):
   47          installed_lang_ids = self.env['res.lang'].search([])
   ..
   68          return True
   69  
   70:     @api.multi
   71      def _process_accounts_translations(self, company_id, langs, field):
   72          in_ids = self.env['account.account.template'].search([('chart_template_id', '=', self.id)], order='id')
   ..
   74          return self.process_translations(langs, field, in_ids, out_ids)
   75  
   76:     @api.multi
   77      def _process_taxes_translations(self, company_id, langs, field):
   78          in_ids = self.env['account.tax.template'].search([('chart_template_id', '=', self.id)], order='id')
   ..
   80          return self.process_translations(langs, field, in_ids, out_ids)
   81  
   82:     @api.multi
   83      def _process_fiscal_pos_translations(self, company_id, langs, field):
   84          in_ids = self.env['account.fiscal.position.template'].search([('chart_template_id', '=', self.id)], order='id')

/home/shivamm/Desktop/odoo-9.0/addons/link_tracker/models/link_tracker.py:
  127          self.favicon = icon_base64
  128  
  129:     @api.multi
  130      def action_view_statistics(self):
  131          action = self.env['ir.actions.act_window'].for_xml_id('link_tracker', 'action_view_click_statistics')
  ...
  133          return action
  134  
  135:     @api.multi
  136      def action_visit_page(self):
  137          return {

/home/shivamm/Desktop/odoo-9.0/addons/lunch/models/lunch.py:
   58              orderline.price for orderline in self.order_line_ids)
   59  
   60:     @api.multi
   61      def name_get(self):
   62          return [(order.id, '%s %s' % (_('Lunch Order'), '#%d' % order.id)) for order in self]
   ..
  219                               'Is an order or a payment', default='payment')
  220  
  221:     @api.multi
  222      def name_get(self):
  223          return [(cashmove.id, '%s %s' % (_('Lunch Cashmove'), '#%d' % cashmove.id)) for cashmove in self]
  ...
  247      end_hour = fields.Float('And', oldname='active_to', required=True, default=23)
  248  
  249:     @api.multi
  250      def name_get(self):
  251          return [(alert.id, '%s %s' % (_('Alert'), '#%d' % alert.id)) for alert in self]

/home/shivamm/Desktop/odoo-9.0/addons/lunch/wizard/lucky_order.py:
   25      max_budget = fields.Float('Max Budget', store=True)
   26      
   27:     @api.multi
   28      def random_pick(self):
   29          """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_alias.py:
   85      ]
   86  
   87:     @api.multi
   88      def _get_alias_domain(self):
   89          alias_domain = self.env["ir.config_parameter"].get_param("mail.catchall.domain")
   ..
  119          return super(Alias, self).create(vals)
  120  
  121:     @api.multi
  122      def write(self, vals):
  123          """"give a unique alias name if given alias name is already assigned"""
  ...
  126          return super(Alias, self).write(vals)
  127  
  128:     @api.multi
  129      def name_get(self):
  130          """Return the mail alias display alias_name, including the implicit
  ...
  227          return res
  228  
  229:     @api.multi
  230      def open_document(self):
  231          if not self.alias_model_id or not self.alias_force_thread_id:
  ...
  239          }
  240  
  241:     @api.multi
  242      def open_parent_document(self):
  243          if not self.alias_parent_model_id or not self.alias_parent_thread_id:

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_channel.py:
  113          return channel
  114  
  115:     @api.multi
  116      def unlink(self):
  117          aliases = self.mapped('alias_id')
  ...
  129          return res
  130  
  131:     @api.multi
  132      def write(self, vals):
  133          result = super(Channel, self).write(vals)
  ...
  140              mail_channel.write({'channel_partner_ids': [(4, pid) for pid in mail_channel.mapped('group_ids').mapped('users').mapped('partner_id').ids]})
  141  
  142:     @api.multi
  143      def action_follow(self):
  144          return self.write({'channel_last_seen_partner_ids': [(0, 0, {'partner_id': self.env.user.partner_id.id})]})
  145  
  146:     @api.multi
  147      def action_unfollow(self):
  148          result = self.write({'channel_partner_ids': [(3, self.env.user.partner_id.id)]})
  ...
  153  
  154  
  155:     @api.multi
  156      def message_get_email_values(self, notif_mail=None):
  157          self.ensure_one()
  ...
  177          return res
  178  
  179:     @api.multi
  180      @api.returns('self', lambda value: value.id)
  181      def message_post(self, body='', subject=None, message_type='notification', subtype=None, parent_id=False, attachments=None, content_subtype='html', **kwargs):
  ...
  197  
  198      # Anonymous method
  199:     @api.multi
  200      def _broadcast(self, partner_ids):
  201          """ Broadcast the current channel header to the given partner ids
  ...
  205          self.env['bus.bus'].sendmany(notifications)
  206  
  207:     @api.multi
  208      def _channel_channel_notifications(self, partner_ids):
  209          """ Generate the bus notifications of current channel for the given partner ids
  ...
  219          return notifications
  220  
  221:     @api.multi
  222      def _notify(self, message):
  223          """ Broadcast the given message on the current channels.
  ...
  231          self.env['bus.bus'].sendmany(notifications)
  232  
  233:     @api.multi
  234      def _channel_message_notifications(self, message):
  235          """ Generate the bus notifications for the given message
  ...
  247          return notifications
  248  
  249:     @api.multi
  250      def channel_info(self):
  251          """ Get the informations header for the current channels
  ...
  286          return channel_infos
  287  
  288:     @api.multi
  289      def channel_fetch_message(self, last_id=False, limit=20):
  290          """ Return message values of the current channel.
  ...
  385              channel_partners.write({'is_pinned': pinned})
  386  
  387:     @api.multi
  388      def channel_seen(self):
  389          self.ensure_one()
  ...
  392              self.env['mail.channel.partner'].search([('channel_id', 'in', self.ids), ('partner_id', '=', self.env.user.partner_id.id)]).write({'seen_message_id': last_message_id})
  393  
  394:     @api.multi
  395      def channel_invite(self, partner_ids):
  396          """ Add the given partner_ids to the current channels and broadcast the channel header to them.
  ...
  483          return self.search(domain).read(['name', 'public', 'uuid', 'channel_type'])
  484  
  485:     @api.multi
  486      def channel_join_and_get_info(self):
  487          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_followers.py:
  114          return res
  115  
  116:     @api.multi
  117      def write(self, vals):
  118          res = super(Followers, self).write(vals)
  ...
  120          return res
  121  
  122:     @api.multi
  123      def unlink(self):
  124          res = super(Followers, self).unlink()

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_mail.py:
   59          return super(MailMail, self).create(values)
   60  
   61:     @api.multi
   62      def unlink(self):
   63          # cascade-delete the parent message for all mails that are not created for a notification
   ..
   75          return super(MailMail, self).default_get(fields)
   76  
   77:     @api.multi
   78      def mark_outgoing(self):
   79          return self.write({'state': 'outgoing'})
   80  
   81:     @api.multi
   82      def cancel(self):
   83          return self.write({'state': 'cancel'})
   ..
  117          return True
  118  
  119:     @api.multi
  120      def _postprocess_sent_message_v9(self, mail_sent=True):
  121          """Perform any post-processing necessary after sending ``mail``
  ...
  139      # ------------------------------------------------------
  140  
  141:     @api.multi
  142      def send_get_mail_body(self, partner=None):
  143          """Return a specific ir_email body. The main purpose of this method
  ...
  147          return body
  148  
  149:     @api.multi
  150      def send_get_mail_to(self, partner=None):
  151          """Forge the email_to with the following heuristic:
  ...
  159          return email_to
  160  
  161:     @api.multi
  162      def send_get_email_dict(self, partner=None):
  163          """Return a dictionary for specific email values, depending on a
  ...
  177          return res
  178  
  179:     @api.multi
  180      def send(self, auto_commit=False, raise_exception=False):
  181          """ Sends the selected emails immediately, ignoring their current

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_message.py:
  112      mail_server_id = fields.Many2one('ir.mail_server', 'Outgoing mail server', readonly=1)
  113  
  114:     @api.multi
  115      def _get_needaction(self):
  116          """ Need action on a mail.message = notified on my channel """
  ...
  147      #------------------------------------------------------
  148  
  149:     @api.multi
  150      def set_message_needaction(self, partner_ids=None):
  151          if not partner_ids:
  ...
  156          return self.write({'needaction_partner_ids': [(4, pid) for pid in partner_ids]})
  157  
  158:     @api.multi
  159      def set_message_done(self, partner_ids=None):
  160          if not partner_ids:
  ...
  165          return self.write({'needaction_partner_ids': [(3, pid) for pid in partner_ids]})
  166  
  167:     @api.multi
  168      def set_message_starred(self, starred):
  169          """ Set messages as (un)starred. Technically, the notifications related
  ...
  265          return True
  266  
  267:     @api.multi
  268      def _message_read_dict(self, parent_id=False):
  269          """ Return a dict representation of the message. This representation is
  ...
  308                                   parent_id=parent_id, limit=limit, child_limit=child_limit)
  309  
  310:     @api.multi
  311      def message_read(self, domain=None, thread_level=0, context= None, parent_id=False, limit=None, child_limit=None):
  312          """ Read messages from mail.message, and get back a list of structured
  ...
  443          return self.search(domain, limit=limit).message_format()
  444  
  445:     @api.multi
  446      def message_format(self):
  447          """ Get the message values in the format for web client. Since message values can be broadcasted,
  ...
  599              return id_list
  600  
  601:     @api.multi
  602      def check_access_rule(self, operation):
  603          """ Access rules of mail.message:
  ...
  793          return message
  794  
  795:     @api.multi
  796      def read(self, fields=None, load='_classic_read'):
  797          """ Override to explicitely call check_access_rule, that is not called
  ...
  800          return super(Message, self).read(fields=fields, load=load)
  801  
  802:     @api.multi
  803      def unlink(self):
  804          # cascade-delete attachments that are directly attached to the message (should only happen
  ...
  814      #------------------------------------------------------
  815  
  816:     @api.multi
  817      def _notify(self, force_send=False, user_signature=True):
  818          """ Add the related record followers to the destination partner_ids if is not a private message.

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_shortcode.py:
   29          return super(MailShortcode, self).create(values)
   30  
   31:     @api.multi
   32      def write(self, values):
   33          if values.get('substitution'):

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_template.py:
  206              self.null_value = False
  207  
  208:     @api.multi
  209      def unlink(self):
  210          self.unlink_action()
  211          return super(MailTemplate, self).unlink()
  212  
  213:     @api.multi
  214      def copy(self, default=None):
  215          default = dict(default or {},
  ...
  217          return super(MailTemplate, self).copy(default=default)
  218  
  219:     @api.multi
  220      def unlink_action(self):
  221          for template in self:
  ...
  226          return True
  227  
  228:     @api.multi
  229      def create_action(self):
  230          ActWindowSudo = self.env['ir.actions.act_window'].sudo()
  ...
  362          return multi_mode and results or results[res_ids[0]]
  363  
  364:     @api.multi
  365      def get_email_template(self, res_ids):
  366          multi_mode = True
  ...
  387          return multi_mode and results or results[res_ids[0]]
  388  
  389:     @api.multi
  390      def generate_recipients(self, results, res_ids):
  391          """Generates the recipients of the template. Default values can ben generated
  ...
  416          return results
  417  
  418:     @api.multi
  419      def generate_email(self, res_ids, fields=None):
  420          """Generates an email from the template for given the given model based on
  ...
  502          return multi_mode and results or results[res_ids[0]]
  503  
  504:     @api.multi
  505      def send_mail(self, res_id, force_send=False, raise_exception=False):
  506          """Generates a new mail message for the given template and record,

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_thread.py:
  145          return [('id', 'in', followers.mapped('res_id'))]
  146  
  147:     @api.multi
  148      @api.depends('message_follower_ids')
  149      def _compute_is_follower(self):
  ...
  169              return [('id', 'not in', followers.mapped('res_id'))]
  170  
  171:     @api.multi
  172      def _get_message_unread(self):
  173          res = dict((res_id, 0) for res_id in self.ids)
  ...
  188              record.message_unread = bool(record.message_unread_counter)
  189  
  190:     @api.multi
  191      def _get_message_needaction(self):
  192          res = dict((res_id, 0) for res_id in self.ids)
  ...
  255          return thread
  256  
  257:     @api.multi
  258      def write(self, values):
  259          if self._context.get('tracking_disable'):
  ...
  285          return result
  286  
  287:     @api.multi
  288      def unlink(self):
  289          """ Override unlink to delete messages and followers. This cannot be
  ...
  404          return {}
  405  
  406:     @api.multi
  407      def _track_subtype(self, init_values):
  408          """ Give the subtypes triggered by the changes on the record according
  ...
  418          return False
  419  
  420:     @api.multi
  421      def _message_track(self, tracked_fields, initial):
  422          self.ensure_one()
  ...
  438          return changes, tracking_value_ids
  439  
  440:     @api.multi
  441      def message_track(self, tracked_fields, initial_values):
  442          if not tracked_fields:
  ...
  537          return 'mail.mail_channel_action_client_chat'
  538  
  539:     @api.multi
  540      def _notification_link_helper(self, link_type, **kwargs):
  541          if kwargs.get('message_id'):
  ...
  566          return link
  567  
  568:     @api.multi
  569      def _notification_group_recipients(self, message, recipients, done_ids, group_data):
  570          """ Given the categories of partners to emails in group_data, set the
  ...
  588          return group_data
  589  
  590:     @api.multi
  591      def _notification_get_recipient_groups(self, message, recipients):
  592          """ Give the categories of recipients for notification emails. As emails
  ...
  612          }
  613  
  614:     @api.multi
  615      def _message_notification_recipients(self, message, recipients):
  616          # At this point, all access rights should be ok. We sudo everything to
  ...
  666      # ------------------------------------------------------
  667  
  668:     @api.multi
  669      def message_get_default_recipients(self, res_model=None, res_ids=None):
  670          if res_model and res_ids:
  ...
  726          return res
  727  
  728:     @api.multi
  729      def message_get_email_values(self, notif_mail=None):
  730          """ Get specific notification email values to store on the notification
  ...
 1213          return res.id
 1214  
 1215:     @api.multi
 1216      def message_update(self, msg_dict, update_vals=None):
 1217          """Called by ``message_process`` when a new message is received
 ....
 1407      #------------------------------------------------------
 1408  
 1409:     @api.multi
 1410      def _message_add_suggested_recipient(self, result, partner=None, email=None, reason=''):
 1411          """ Called by message_get_suggested_recipients, to add a suggested
 ....
 1432          return result
 1433  
 1434:     @api.multi
 1435      def message_get_suggested_recipients(self):
 1436          """ Returns suggested recipients for ids. Those are a list of
 ....
 1444          return result
 1445  
 1446:     @api.multi
 1447      def _find_partner_from_emails(self, emails, res_model=None, res_id=None, check_followers=True, force_create=False):
 1448          """ Utility method to find partners from email addresses. The rules are :
 ....
 1509          return partner_ids
 1510  
 1511:     @api.multi
 1512      def message_partner_info_from_emails(self, emails, link_mail=False):
 1513          """ Convert a list of emails into a list partner_ids and a list
 ....
 1572          return m2m_attachment_ids
 1573  
 1574:     @api.multi
 1575      @api.returns('self', lambda value: value.id)
 1576      def message_post(self, body='', subject=None, message_type='notification',
 ....
 1718          return new_message
 1719  
 1720:     @api.multi
 1721      def message_post_with_template(self, template_id, **kwargs):
 1722          """ Helper method to send a mail with a template
 ....
 1749      # ------------------------------------------------------
 1750  
 1751:     @api.multi
 1752      def message_subscribe_users(self, user_ids=None, subtype_ids=None):
 1753          """ Wrapper on message_subscribe, using users. If user_ids is not
 ....
 1760          return result
 1761  
 1762:     @api.multi
 1763      def message_subscribe(self, partner_ids=None, channel_ids=None, subtype_ids=None, force=True):
 1764          """ Add partners to the records followers. """
 ....
 1792          return True
 1793  
 1794:     @api.multi
 1795      def message_unsubscribe_users(self, user_ids=None):
 1796          """ Wrapper on message_subscribe, using users. If user_ids is not
 ....
 1804          return result
 1805  
 1806:     @api.multi
 1807      def message_unsubscribe(self, partner_ids=None, channel_ids=None):
 1808          """ Remove partners from the records followers. """
 ....
 1845          return user_field_lst
 1846  
 1847:     @api.multi
 1848      def _message_auto_subscribe_notify(self, partner_ids):
 1849          """ Notify newly subscribed followers of the last posted message.
 ....
 1862                  messages.write({'needaction_partner_ids': [(4, pid) for pid in partner_ids]})
 1863  
 1864:     @api.multi
 1865      def message_auto_subscribe(self, updated_fields, values=None):
 1866          """ Handle auto subscription. Two methods for auto subscription exist:
 ....
 1952      # ------------------------------------------------------
 1953  
 1954:     @api.multi
 1955      def message_set_read(self):
 1956          messages = self.env['mail.message'].search([('model', '=', self._name), ('res_id', 'in', self.ids), ('needaction', '=', True)])
 ....
 1958          return messages.ids
 1959  
 1960:     @api.multi
 1961      def message_change_thread(self, new_thread):
 1962          """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_tracking_value.py:
   67          return {}
   68  
   69:     @api.multi
   70      def get_old_display_value(self):
   71          result = []
   ..
   87          return result
   88  
   89:     @api.multi
   90      def get_new_display_value(self):
   91          result = []

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/res_config.py:
   16                                 "the Odoo server, enter the domain name here.")
   17  
   18:     @api.multi
   19      def get_default_fail_counter(self):
   20          previous_date = datetime.datetime.now() - datetime.timedelta(days=30)
   ..
   23          }
   24  
   25:     @api.multi
   26      def get_default_alias_domain(self):
   27          alias_domain = self.env["ir.config_parameter"].get_param("mail.catchall.domain", default=None)
   ..
   34          return {'alias_domain': alias_domain or False}
   35  
   36:     @api.multi
   37      def set_alias_domain(self):
   38          for record in self:

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/res_partner.py:
   30      channel_ids = fields.Many2many('mail.channel', 'mail_channel_partner', 'partner_id', 'channel_id', string='Channels')
   31  
   32:     @api.multi
   33      def message_get_suggested_recipients(self):
   34          recipients = super(Partner, self).message_get_suggested_recipients()
   ..
   37          return recipients
   38  
   39:     @api.multi
   40      def message_get_default_recipients(self):
   41          return dict((res_id, {'partner_ids': [res_id], 'email_to': False, 'email_cc': False}) for res_id in self.ids)
   ..
  115          return emails, recipients_nbr
  116  
  117:     @api.multi
  118      def _notify(self, message, force_send=False, user_signature=True):
  119          # TDE TODO: model-dependant ? (like customer -> always email ?)
  ...
  129          return True
  130  
  131:     @api.multi
  132      def _notify_by_email(self, message, force_send=False, user_signature=True):
  133          """ Method to send email linked to notified messages. The recipients are
  ...
  191          return True
  192  
  193:     @api.multi
  194      def _notify_by_chat(self, message):
  195          """ Broadcast the message to all the partner since """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/res_users.py:
   58          return user
   59  
   60:     @api.multi
   61      def write(self, vals):
   62          write_res = super(Users, self).write(vals)
   ..
   83          return self.partner_id.sudo().message_post(body=body)
   84  
   85:     @api.multi
   86      def unlink(self):
   87          # Cascade-delete mail aliases as well, as they should not exist without the user.
   ..
   97          return self.partner_id.id
   98  
   99:     @api.multi
  100      def message_post(self, **kwargs):
  101          """ Redirect the posting of message on res.users as a private discussion.
  ...
  130          return self.pool.get('mail.thread').message_get_partner_info_from_emails(cr, uid, emails, link_mail=link_mail, context=context)
  131  
  132:     @api.multi
  133      def message_get_suggested_recipients(self):
  134          return dict((res_id, list()) for res_id in self._ids)
  ...
  143      _inherit = 'res.groups'
  144  
  145:     @api.multi
  146      def write(self, vals, context=None):
  147          write_res = super(res_groups_mail_channel, self).write(vals)

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/email_template_preview.py:
   37  
   38      @api.onchange('res_id')
   39:     @api.multi
   40      def on_change_res_id(self):
   41          mail_values = {}

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/invite.py:
   33      send_mail = fields.Boolean('Send Email', default=True, help="If checked, the partners will receive an email warning they have been added in the document's followers.")
   34  
   35:     @api.multi
   36      def add_followers(self):
   37          email_from = self.env['mail.message']._get_default_from()

/home/shivamm/Desktop/odoo-9.0/addons/mail/wizard/mail_compose_message.py:
  123          domain="[('model', '=', model)]")
  124  
  125:     @api.multi
  126      def check_access_rule(self, operation):
  127          """ Access rules of mail.compose.message:
  ...
  144          return super(MailComposer, self).check_access_rule(operation)
  145  
  146:     @api.multi
  147      def _notify(self, force_send=False, user_signature=True):
  148          """ Override specific notify method of mail.message, because we do
  ...
  186      # action buttons call with positionnal arguments only, so we need an intermediary function
  187      # to ensure the context is passed correctly
  188:     @api.multi
  189      def send_mail_action(self):
  190          # TDE/ ???
  191          return self.send_mail()
  192  
  193:     @api.multi
  194      def send_mail(self, auto_commit=False):
  195          """ Process the wizard content and proceed with sending the related
  ...
  251          return {'type': 'ir.actions.act_window_close'}
  252  
  253:     @api.multi
  254      def get_mail_values(self, res_ids):
  255          """Generate the values that will be used by send_mail to create mail_messages
  ...
  320      #------------------------------------------------------
  321  
  322:     @api.multi
  323      @api.onchange('template_id')
  324      def onchange_template_id_wrapper(self):
  ...
  328              setattr(self, fname, value)
  329  
  330:     @api.multi
  331      def onchange_template_id(self, template_id, composition_mode, model, res_id):
  332          """ - mass_mailing: we cannot render, so return the template values
  ...
  375          return {'value': values}
  376  
  377:     @api.multi
  378      def save_as_template(self):
  379          """ hit save as template button: current form value will be a new
  ...
  402      #------------------------------------------------------
  403  
  404:     @api.multi
  405      def render_message(self, res_ids):
  406          """Generate template-based values of wizard, for the document records given

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission.py:
  144              self.state = 'payment_process'
  145  
  146:     @api.multi
  147      def get_student_vals(self):
  148          return {
  ...
  206          self.state = 'fees_paid'
  207  
  208:     @api.multi
  209      def open_student(self):
  210          form_view = self.env.ref('openeducat_core.view_op_student_form')
  ...
  226          return value
  227  
  228:     @api.multi
  229      def create_invoice(self):
  230          """ Create invoice for fee payment process of student """

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/wizard/admission_analysis_wizard.py:
   35      end_date = fields.Date('End Date', required=True)
   36  
   37:     @api.multi
   38      def print_report(self):
   39          start_date = fields.Date.from_string(self.start_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/wizards/student_attendance_wizard.py:
   40              raise ValidationError("To Date cannot be set before From Date.")
   41  
   42:     @api.multi
   43      def print_report(self):
   44          data = self.read(['from_date', 'to_date'])[0]

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/res_company.py:
   36      user_line = fields.One2many('op.student', 'user_id', 'User Line')
   37  
   38:     @api.multi
   39      def create_user(self, records, user_group=None):
   40          for rec in records:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/wizard/student_hall_tickets_wizard.py:
   31          'op.exam.session', 'Exam Session', required=True)
   32  
   33:     @api.multi
   34      def print_report(self):
   35          data = self.read(['exam_session_id'])[0]

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_fees/models/student.py:
   26      _inherit = 'op.student'
   27  
   28:     @api.multi
   29      def action_view_invoice(self):
   30          '''

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_movement.py:
  107          self.write({'penalty': penalty_amt})
  108  
  109:     @api.multi
  110      def return_book(self):
  111          ''' function to return book '''
  ...
  121          return True
  122  
  123:     @api.multi
  124      def do_book_reservation(self):
  125          ''' function to reserve book '''

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/time_table_report.py:
   61          self.batch_id = False
   62  
   63:     @api.multi
   64      def gen_time_table_report(self):
   65          data = self.read(

/home/shivamm/Desktop/odoo-9.0/addons/payment_authorize/models/authorize.py:
   43          return hmac.new(str(values['x_trans_key']), data, hashlib.md5).hexdigest()
   44  
   45:     @api.multi
   46      def authorize_form_generate_values(self, values):
   47          self.ensure_one()
   ..
   77          return authorize_tx_values
   78  
   79:     @api.multi
   80      def authorize_get_form_action_url(self):
   81          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/payment_sips/models/sips.py:
   75          return shasign.hexdigest()
   76  
   77:     @api.multi
   78      def sips_form_generate_values(self, values):
   79          self.ensure_one()
   ..
  116          return sips_tx_values
  117  
  118:     @api.multi
  119      def sips_get_form_action_url(self):
  120          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/pos_cache/models/pos_cache.py:
   75              return None
   76  
   77:     @api.multi
   78      def get_products_from_cache(self, fields, domain):
   79          cache_for_user = self._get_cache_for_user()

/home/shivamm/Desktop/odoo-9.0/addons/procurement_jit/sale.py:
    7      _inherit = "sale.order.line"
    8  
    9:     @api.multi
   10      def _action_procurement_create(self):
   11          res = super(SaleOrderLine, self)._action_procurement_create()

/home/shivamm/Desktop/odoo-9.0/addons/product/product.py:
  152  class product_category(osv.osv):
  153  
  154:     @api.multi
  155      def name_get(self):
  156          def get_names(cat):

/home/shivamm/Desktop/odoo-9.0/addons/product_visible_discount/product_visible_discount.py:
   42          return product[field_name] * factor, currency_id
   43  
   44:     @api.multi
   45      @api.onchange('product_id')
   46      def product_id_change(self):

/home/shivamm/Desktop/odoo-9.0/addons/programmer/shivam.py:
   20  		return super(shivam, self).create(vals)
   21  
   22: 	@api.multi
   23  	def unlink(self):
   24  		return super(shivam, self).unlink()
   25  	
   26: 	@api.multi
   27  	def update(self):
   28  		return self.write({'fname': "Rakshya", 'lname': "Mahajan"})
   29  	
   30: 	@api.multi
   31  	def fetch(self):
   32  		print self.browse()

/home/shivamm/Desktop/odoo-9.0/addons/project/project.py:
  291              }
  292  
  293:     @api.multi
  294      def setActive(self, value=True):
  295          """ Set a project as active/inactive, and its tasks as well. """

/home/shivamm/Desktop/odoo-9.0/addons/project_issue/project_issue.py:
  443      }
  444  
  445:     @api.multi
  446      def write(self, vals):
  447          res = super(project, self).write(vals)

/home/shivamm/Desktop/odoo-9.0/addons/purchase/partner.py:
    8      _inherit = 'res.partner'
    9  
   10:     @api.multi
   11      def _purchase_invoice_count(self):
   12          PurchaseOrder = self.env['purchase.order']

/home/shivamm/Desktop/odoo-9.0/addons/purchase/purchase.py:
   30              })
   31  
   32:     @api.multi
   33      def _inverse_date_planned(self):
   34          for order in self:
   ..
  161          return pos.name_get()
  162  
  163:     @api.multi
  164      @api.depends('name', 'partner_ref')
  165      def name_get(self):
  ...
  178          return super(PurchaseOrder, self).create(vals)
  179  
  180:     @api.multi
  181      def unlink(self):
  182          for order in self:
  ...
  185          return super(PurchaseOrder, self).unlink()
  186  
  187:     @api.multi
  188      def _track_subtype(self, init_values):
  189          self.ensure_one()
  ...
  208          return {}
  209  
  210:     @api.multi
  211      def action_rfq_send(self):
  212          '''
  ...
  246          }
  247  
  248:     @api.multi
  249      def print_quotation(self):
  250          self.write({'state': "sent"})
  251          return self.env['report'].get_action(self, 'purchase.report_purchasequotation')
  252  
  253:     @api.multi
  254      def button_approve(self):
  255          self.write({'state': 'purchase'})
  ...
  257          return {}
  258  
  259:     @api.multi
  260      def button_draft(self):
  261          self.write({'state': 'draft'})
  262          return {}
  263  
  264:     @api.multi
  265      def button_confirm(self):
  266          for order in self:
  ...
  276          return {}
  277  
  278:     @api.multi
  279      def button_cancel(self):
  280          for order in self:
  ...
  297          self.write({'state': 'cancel'})
  298  
  299:     @api.multi
  300      def button_done(self):
  301          self.write({'state': 'done'})
  302  
  303:     @api.multi
  304      def _get_destination_location(self):
  305          self.ensure_one()
  ...
  324          }
  325  
  326:     @api.multi
  327      def _create_picking(self):
  328          for order in self:
  ...
  336          return True
  337  
  338:     @api.multi
  339      def _add_supplier_to_product(self):
  340          # Add the partner in the supplier list of the product if the supplier is not registered for
  ...
  360                      break
  361  
  362:     @api.multi
  363      def action_view_picking(self):
  364          '''
  ...
  381          return result
  382  
  383:     @api.multi
  384      def action_view_invoice(self):
  385          '''
  ...
  470      procurement_ids = fields.One2many('procurement.order', 'purchase_line_id', string='Associated Procurements', copy=False)
  471  
  472:     @api.multi
  473      def _create_stock_moves(self, picking):
  474          moves = self.env['stock.move']
  ...
  525          return done
  526  
  527:     @api.multi
  528      def unlink(self):
  529          for line in self:
  ...
  602      purchase_id = fields.Many2one(related='purchase_line_id.order_id', string='Purchase Order')
  603  
  604:     @api.multi
  605      def propagate_cancels(self):
  606          result = super(ProcurementOrder, self).propagate_cancels()
  ...
  689          return schedule_date - relativedelta(days=seller_delay)
  690  
  691:     @api.multi
  692      def _prepare_purchase_order_line(self, po, supplier):
  693          self.ensure_one()
  ...
  730          }
  731  
  732:     @api.multi
  733      def _prepare_purchase_order(self, partner):
  734          self.ensure_one()
  ...
  753          }
  754  
  755:     @api.multi
  756      def make_po(self):
  757          cache = {}
  ...
  819          return []
  820  
  821:     @api.multi
  822      def _purchase_count(self):
  823          for template in self:
  ...
  841      _inherit = 'product.product'
  842  
  843:     @api.multi
  844      def _purchase_count(self):
  845          domain = [
  ...
  868      _inherit = 'mail.compose.message'
  869  
  870:     @api.multi
  871      def send_mail(self, auto_commit=False):
  872          if self._context.get('default_model') == 'purchase.order' and self._context.get('default_res_id'):

/home/shivamm/Desktop/odoo-9.0/addons/rating/models/rating.py:
   59          return rating
   60  
   61:     @api.multi
   62      def reset(self):
   63          for record in self:
   ..
   76      rating_ids = fields.One2many('rating.rating', 'res_id', string='Rating', domain=lambda self: [('res_model', '=', self._name)])
   77  
   78:     @api.multi
   79      def rating_send_request(self, template, partner_id, rated_partner_id, reuse_rating=True):
   80          """ This method create (empty) rating objects for the current recordsets
   ..
  120              template.send_mail(rating.id, force_send=True)
  121  
  122:     @api.multi
  123      def rating_get_repartition(self, add_stats=False, domain=None):
  124          """ get the repatition of rating grade for the given res_ids.
  ...
  151          return values
  152  
  153:     @api.multi
  154      def rating_get_grades(self, domain=None):
  155          """ get the repatition of rating grade for the given res_ids.
  ...
  171          return res
  172  
  173:     @api.multi
  174      def rating_get_stats(self, domain=None):
  175          """ get the statistics of the rating repatition

/home/shivamm/Desktop/odoo-9.0/addons/rating_project/models/project.py:
   22      _inherit = ['project.task', 'rating.mixin']
   23  
   24:     @api.multi
   25      def write(self, values):
   26          if 'stage_id' in values and values.get('stage_id'):
   ..
   57  
   58  
   59:     @api.multi
   60      def action_view_task_rating(self):
   61          """ return the action to see all the rating about the tasks of the project """
   ..
   63          return dict(action, domain=[('rating', '!=', -1), ('res_id', 'in', self.tasks.ids), ('res_model', '=', 'project.task')])
   64  
   65:     @api.multi
   66      def action_view_all_rating(self):
   67          """ return the action to see all the rating about the all sort of activity of the project (tasks, issues, ...) """

/home/shivamm/Desktop/odoo-9.0/addons/rating_project_issue/models/project_issue.py:
    8      _inherit = ['project.issue', 'rating.mixin']
    9  
   10:     @api.multi
   11      def write(self, values):
   12          if 'stage_id' in values and values.get('stage_id'):
   ..
   24      _inherit = "project.project"
   25  
   26:     @api.multi
   27      @api.depends('percentage_satisfaction_task', 'percentage_satisfaction_issue')
   28      def _compute_percentage_satisfaction_project(self):
   ..
   71      percentage_satisfaction_issue = fields.Integer(compute='_compute_percentage_satisfaction_issue', string='% Happy', store=True, default=-1)
   72  
   73:     @api.multi
   74      def action_view_issue_rating(self):
   75          """ return the action to see all the rating about the issues of the project """
   ..
   78          return dict(action, domain=[('res_id', 'in', issues.ids), ('res_model', '=', 'project.issue')])
   79  
   80:     @api.multi
   81      def action_view_all_rating(self):
   82          action = super(Project, self).action_view_all_rating()

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale.py:
  143      product_id = fields.Many2one('product.product', related='order_line.product_id', string='Product')
  144  
  145:     @api.multi
  146      def button_dummy(self):
  147          return True
  148  
  149:     @api.multi
  150      def unlink(self):
  151          for order in self:
  ...
  154          return super(SaleOrder, self).unlink()
  155  
  156:     @api.multi
  157      def _track_subtype(self, init_values):
  158          self.ensure_one()
  ...
  163          return super(SaleOrder, self)._track_subtype(init_values)
  164  
  165:     @api.multi
  166      @api.onchange('partner_shipping_id')
  167      def onchange_partner_shipping_id(self):
  ...
  174          return {}
  175  
  176:     @api.multi
  177      @api.onchange('partner_id')
  178      def onchange_partner_id(self):
  ...
  223          return result
  224  
  225:     @api.multi
  226      def _prepare_invoice(self):
  227          """
  ...
  252          return invoice_vals
  253  
  254:     @api.multi
  255      def print_quotation(self):
  256          self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})
  257          return self.env['report'].get_action(self, 'sale.report_saleorder')
  258  
  259:     @api.multi
  260      def action_view_invoice(self):
  261          invoice_ids = self.mapped('invoice_ids')
  ...
  283          return result
  284  
  285:     @api.multi
  286      def action_invoice_create(self, grouped=False, final=False):
  287          """
  ...
  322          return [inv.id for inv in invoices.values()]
  323  
  324:     @api.multi
  325      def action_draft(self):
  326          self.filtered(lambda s: s.state in ['cancel', 'sent']).write({'state': 'draft'})
  327  
  328:     @api.multi
  329      def action_cancel(self):
  330          self.write({'state': 'cancel'})
  331  
  332:     @api.multi
  333      def action_quotation_send(self):
  334          '''
  ...
  365          }
  366  
  367:     @api.multi
  368      def force_quotation_send(self):
  369          for order in self:
  ...
  375          return True
  376  
  377:     @api.multi
  378      def action_done(self):
  379          self.write({'state': 'done'})
  ...
  383          return {'name': self.name}
  384  
  385:     @api.multi
  386      def action_confirm(self):
  387          for order in self:
  ...
  396              self.action_done()
  397  
  398:     @api.multi
  399      def _create_analytic_account(self, prefix=None):
  400          for order in self:
  ...
  500              line.price_reduce = line.price_subtotal / line.product_uom_qty if line.product_uom_qty else 0.0
  501  
  502:     @api.multi
  503      def _compute_tax_id(self):
  504          for line in self:
  ...
  516                  line.tax_id = line.product_id.taxes_id if line.product_id.taxes_id else False
  517  
  518:     @api.multi
  519      def _prepare_order_line_procurement(self, group_id=False):
  520          self.ensure_one()
  ...
  531          }
  532  
  533:     @api.multi
  534      def _action_procurement_create(self):
  535          """
  ...
  577          return line
  578  
  579:     @api.multi
  580      def write(self, values):
  581          lines = False
  ...
  643      procurement_ids = fields.One2many('procurement.order', 'sale_line_id', string='Procurements')
  644  
  645:     @api.multi
  646      def _prepare_invoice_line(self, qty):
  647          """
  ...
  676          return res
  677  
  678:     @api.multi
  679      def invoice_line_create(self, invoice_id, qty):
  680          """
  ...
  692                  self.env['account.invoice.line'].create(vals)
  693  
  694:     @api.multi
  695      @api.onchange('product_id')
  696      def product_id_change(self):
  ...
  740              self.price_unit = self.env['account.tax']._fix_tax_included_price(product.price, product.taxes_id, self.tax_id)
  741  
  742:     @api.multi
  743      def unlink(self):
  744          if self.filtered(lambda x: x.state in ('sale', 'done')):
  ...
  746          return super(SaleOrderLine, self).unlink()
  747  
  748:     @api.multi
  749      def _get_delivered_qty(self):
  750          '''
  ...
  759      _inherit = 'mail.compose.message'
  760  
  761:     @api.multi
  762      def send_mail(self, auto_commit=False):
  763          if self._context.get('default_model') == 'sale.order' and self._context.get('default_res_id') and self._context.get('mark_so_as_sent'):
  ...
  778      team_id = fields.Many2one('crm.team', string='Sales Team', default=_get_default_team)
  779  
  780:     @api.multi
  781      def confirm_paid(self):
  782          res = super(AccountInvoice, self).confirm_paid()
  ...
  804      _inherit = 'product.product'
  805  
  806:     @api.multi
  807      def _sales_count(self):
  808          r = {}
  ...
  824      track_service = fields.Selection([('manual', 'Manually set quantities on order')], string='Track Service', default='manual')
  825  
  826:     @api.multi
  827      @api.depends('product_variant_ids.sales_count')
  828      def _sales_count(self):
  ...
  830              product.sales_count = sum([p.sales_count for p in product.product_variant_ids])
  831  
  832:     @api.multi
  833      def action_view_sales(self):
  834          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/sale/sale_analytic.py:
    9      _inherit = "sale.order.line"
   10  
   11:     @api.multi
   12      def _compute_analytic(self, domain=None):
   13          lines = {}
   ..
   99          return result
  100  
  101:     @api.multi
  102      def write(self, values):
  103          if self._context.get('create', False):

/home/shivamm/Desktop/odoo-9.0/addons/sale/wizard/sale_make_invoice_advance.py:
   44          return {}
   45  
   46:     @api.multi
   47      def _create_invoice(self, order, so_line, amount):
   48          inv_obj = self.env['account.invoice']
   ..
   98          return invoice
   99  
  100:     @api.multi
  101      def create_invoices(self):
  102          sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))

/home/shivamm/Desktop/odoo-9.0/addons/sale_margin/sale_margin.py:
    8      _inherit = "sale.order.line"
    9  
   10:     @api.multi
   11      @api.onchange('product_id', 'product_uom_qty')
   12      def product_id_change_margin(self):

/home/shivamm/Desktop/odoo-9.0/addons/sale_mrp/sale_mrp.py:
   12      sale_ref = fields.Char(compute='_compute_sale_name_sale_ref', string='Sale Reference', help='Indicate the Customer Reference from sales order.')
   13  
   14:     @api.multi
   15      def _compute_sale_name_sale_ref(self):
   16          def get_parent_move(move):
   ..
   30      property_ids = fields.Many2many('mrp.property', 'sale_order_line_property_rel', 'order_id', 'property_id', 'Properties', readonly=True, states={'draft': [('readonly', False)]})
   31  
   32:     @api.multi
   33      def _get_delivered_qty(self):
   34          self.ensure_one()
   ..
   60          return super(SaleOrderLine, self)._get_delivered_qty()
   61  
   62:     @api.multi
   63      def _prepare_order_line_procurement(self, group_id=False):
   64          vals = super(SaleOrderLine, self)._prepare_order_line_procurement(group_id=group_id)

/home/shivamm/Desktop/odoo-9.0/addons/sale_service/models/timesheet.py:
   12      tasks_count = fields.Integer(string='Tasks', compute='_compute_tasks_ids')
   13  
   14:     @api.multi
   15      @api.depends('order_line.product_id.project_id')
   16      def _compute_tasks_ids(self):
   ..
   19              order.tasks_count = len(order.tasks_ids)
   20  
   21:     @api.multi
   22      def action_view_task(self):
   23          self.ensure_one()
   ..
   67          return result
   68  
   69:     @api.multi
   70      def write(self, values):
   71          self._update_values(values)

/home/shivamm/Desktop/odoo-9.0/addons/sale_stock/res_config.py:
   29          implied_group='sale_stock.group_route_so_lines')
   30  
   31:     @api.multi
   32      def get_default_sale_config(self):
   33          default_picking_policy = self.env['ir.values'].get_default('sale.order', 'picking_policy')
   ..
   36          }
   37  
   38:     @api.multi
   39      def set_sale_defaults(self):
   40          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/sale_stock/sale_stock.py:
   28      delivery_count = fields.Integer(string='Delivery Orders', compute='_compute_picking_ids')
   29  
   30:     @api.multi
   31      @api.depends('procurement_group_id')
   32      def _compute_picking_ids(self):
   ..
   40              self.company_id = self.warehouse_id.company_id.id
   41  
   42:     @api.multi
   43      def action_view_delivery(self):
   44          '''
   ..
   71          return result
   72  
   73:     @api.multi
   74      def action_cancel(self):
   75          self.order_line.mapped('procurement_ids').cancel()
   76          super(SaleOrder, self).action_cancel()
   77  
   78:     @api.multi
   79      def _prepare_invoice(self):
   80          invoice_vals = super(SaleOrder, self)._prepare_invoice()
   ..
   95      product_tmpl_id = fields.Many2one('product.template', related='product_id.product_tmpl_id', string='Product Template')
   96  
   97:     @api.multi
   98      @api.depends('product_id')
   99      def _compute_qty_delivered_updateable(self):
  ...
  156          return {}
  157  
  158:     @api.multi
  159      def _prepare_order_line_procurement(self, group_id=False):
  160          vals = super(SaleOrderLine, self)._prepare_order_line_procurement(group_id=group_id)
  ...
  171          return vals
  172  
  173:     @api.multi
  174      def _get_delivered_qty(self):
  175          self.ensure_one()
  ...
  181          return qty
  182  
  183:     @api.multi
  184      def _check_package(self):
  185          default_uom = self.product_id.uom_id
  ...
  226      _inherit = "stock.move"
  227  
  228:     @api.multi
  229      def action_done(self):
  230          result = super(StockMove, self).action_done()

/home/shivamm/Desktop/odoo-9.0/addons/sale_timesheet/models/sale_timesheet.py:
   80      timesheet_count = fields.Float(string='Timesheet activities', compute='_compute_timesheet_ids')
   81  
   82:     @api.multi
   83      @api.depends('project_id.line_ids')
   84      def _compute_timesheet_ids(self):
   ..
   87              order.timesheet_count = round(sum([line.unit_amount for line in order.timesheet_ids]), 2)
   88  
   89:     @api.multi
   90      @api.constrains('order_line')
   91      def _check_multi_timesheet(self):
   ..
   99          return {}
  100  
  101:     @api.multi
  102      def action_confirm(self):
  103          result = super(SaleOrder, self).action_confirm()
  ...
  110          return result
  111  
  112:     @api.multi
  113      def action_view_timesheet(self):
  114          self.ensure_one()
  ...
  136      _inherit = "sale.order.line"
  137  
  138:     @api.multi
  139      def _compute_analytic(self, domain=None):
  140          if not domain:

/home/shivamm/Desktop/odoo-9.0/addons/stock/wizard/stock_backorder_confirmation.py:
   19          return res
   20  
   21:     @api.multi
   22      def _process(self, cancel_backorder=False):
   23          self.ensure_one()
   ..
   33              self.pick_id.message_post(body=_("Back order <em>%s</em> <b>cancelled</b>.") % (backorder_pick.name))
   34  
   35:     @api.multi
   36      def process(self):
   37          self.ensure_one()
   38          self._process()
   39  
   40:     @api.multi
   41      def process_cancel_backorder(self):
   42          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/stock/wizard/stock_immediate_transfer.py:
   19          return res
   20  
   21:     @api.multi
   22      def process(self):
   23          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/stock_account/product.py:
   82          return {}
   83  
   84:     @api.multi
   85      def _get_product_accounts(self):
   86          """ Add the stock accounts related to product to the result of super()
   ..
   95          return accounts
   96  
   97:     @api.multi
   98      def get_product_accounts(self, fiscal_pos=None):
   99          """ Add the stock journal related to product to the result of super()

/home/shivamm/Desktop/odoo-9.0/addons/stock_account/stock_account.py:
  426          super(AccountChartTemplate, self).generate_journals(acc_template_ref=acc_template_ref, company=company, journals_dict=journal_to_add)
  427  
  428:     @api.multi
  429      def generate_properties(self, acc_template_ref, company, property_list=None):
  430          super(AccountChartTemplate, self).generate_properties(acc_template_ref=acc_template_ref, company=company)

/home/shivamm/Desktop/odoo-9.0/addons/web_tip/web_tip.py:
   28      is_consumed = fields.Boolean(string='Tip consumed', compute='_is_consumed')
   29  
   30:     @api.multi
   31      def consume(self):
   32         self.write({'user_ids': [(4, self.env.uid)]})

/home/shivamm/Desktop/odoo-9.0/addons/website_event/models/event.py:
   24      )
   25  
   26:     @api.multi
   27      @api.depends('name')
   28      def _website_url(self, name, arg):
   ..
   88          return None
   89  
   90:     @api.multi
   91      def _track_subtype(self, init_values):
   92          self.ensure_one()
   ..
   97          return super(event, self)._track_subtype(init_values)
   98  
   99:     @api.multi
  100      def action_open_badge_editor(self):
  101          """ open the event badge editor : redirect to the report page of event badge report """

/home/shivamm/Desktop/odoo-9.0/addons/website_event_track/models/event.py:
   87          return res
   88  
   89:     @api.multi
   90      def write(self, vals):
   91          if vals.get('state') == 'published':
   ..
   96          return res
   97  
   98:     @api.multi
   99      @api.depends('name')
  100      def _website_url(self, field_name, arg):
  ...
  147      _inherit = "event.event"
  148  
  149:     @api.multi
  150      def _count_tracks(self):
  151          track_data = self.env['event.track'].read_group([('state', '!=', 'cancel')],

/home/shivamm/Desktop/odoo-9.0/addons/website_form/models/models.py:
   21          return [self.id] + [m.all_inherited_model_ids() for m in self.inherited_model_ids]
   22  
   23:     @api.multi
   24      def get_authorized_fields(self):
   25          model = self.env[self.model]

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/forum.py:
  292              self.relevancy = 0
  293  
  294:     @api.multi
  295      def _get_user_vote(self):
  296          votes = self.env['forum.post.vote'].search_read([('post_id', 'in', self._ids), ('user_id', '=', self._uid)], ['vote', 'post_id'])
  ...
  299              vote.user_vote = mapped_vote.get(vote.id, 0)
  300  
  301:     @api.multi
  302      @api.depends('vote_ids.vote')
  303      def _get_vote_count(self):
  ...
  343  
  344  
  345:     @api.multi
  346      def _get_post_karma_rights(self):
  347          user = self.env.user
  ...
  438          return super(Post, self).check_mail_message_access(res_ids, operation, model_name=model_name)
  439  
  440:     @api.multi
  441      @api.depends('name', 'post_type')
  442      def name_get(self):
  ...
  449          return result
  450  
  451:     @api.multi
  452      def write(self, vals):
  453          if 'content' in vals:
  ...
  484          return res
  485  
  486:     @api.multi
  487      def reopen(self):
  488          if any(post.parent_id or post.state != 'close' for post in self):
  ...
  500          self.sudo().write({'state': 'active'})
  501  
  502:     @api.multi
  503      def close(self, reason_id):
  504          if any(post.parent_id for post in self):
  ...
  582          return True
  583  
  584:     @api.multi
  585      def unlink(self):
  586          if any(not post.can_unlink for post in self):
  ...
  593          return super(Post, self).unlink()
  594  
  595:     @api.multi
  596      def bump(self):
  597          """ Bump a question: trigger a write_date by writing on a dummy bump_date
  ...
  603          return False
  604  
  605:     @api.multi
  606      def vote(self, upvote=True):
  607          Vote = self.env['forum.post.vote']
  ...
  700          return comment.unlink()
  701  
  702:     @api.multi
  703      def set_viewed(self):
  704          self._cr.execute("""UPDATE forum_post SET views = views+1 WHERE id IN %s""", (self._ids,))
  705          return True
  706  
  707:     @api.multi
  708      def get_access_action(self):
  709          """ Override method that generated the link to access the document. Instead
  ...
  717          }
  718  
  719:     @api.multi
  720      def _notification_get_recipient_groups(self, message, recipients):
  721          """ Override to set the access button: everyone can see an access button
  ...
  794          return vote
  795  
  796:     @api.multi
  797      def write(self, values):
  798          if 'vote' in values:
  ...
  832      ]
  833  
  834:     @api.multi
  835      @api.depends("post_ids.tag_ids")
  836      def _get_posts_count(self):

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/res_users.py:
   26      bronze_badge = fields.Integer('Bronze badges count', compute="_get_user_badge_level")
   27  
   28:     @api.multi
   29      @api.depends('badge_ids')
   30      def _get_user_badge_level(self):
   ..
   98          return False
   99  
  100:     @api.multi
  101      def add_karma(self, karma):
  102          for user in self:
  ...
  114  
  115      # Wrapper for call_kw with inherits
  116:     @api.multi
  117      def open_website_url(self):
  118          return self.mapped('partner_id').open_website_url()

/home/shivamm/Desktop/odoo-9.0/addons/website_payment/models/res_config.py:
   20          }
   21  
   22:     @api.multi
   23      def set_default_acquirer(self):
   24          for wizard in self:

/home/shivamm/Desktop/odoo-9.0/addons/website_portal_sale/models/sale_order.py:
    8      _inherit = 'sale.order'
    9  
   10:     @api.multi
   11      def get_access_action(self):
   12          """ Override method that generated the link to access the document. Instead

/home/shivamm/Desktop/odoo-9.0/addons/website_project_issue/models/project_issue.py:
    9      _inherit = ['project.issue']
   10  
   11:     @api.multi
   12      def get_access_action(self):
   13          """ Override method that generated the link to access the document. Instead
   ..
   21          }
   22  
   23:     @api.multi
   24      def _notification_get_recipient_groups(self, message, recipients):
   25          """ Override to set the access button: everyone can see an access button

/home/shivamm/Desktop/odoo-9.0/addons/website_rating_project_issue/project_project.py:
    8      _inherit = ['project.project', 'website.published.mixin']
    9  
   10:     @api.multi
   11      def action_view_all_rating(self):
   12          """ Override this method without calling parent to redirect to rating website project page """
   ..
   19          }
   20  
   21:     @api.multi
   22      def _website_url(self, field_name, arg):
   23          res = dict()

/home/shivamm/Desktop/odoo-9.0/addons/website_sale_digital/product.py:
    8      attachment_count = fields.Integer(compute='_compute_attachment_count', string="File")
    9  
   10:     @api.multi
   11      def _compute_attachment_count(self):
   12          IrAttachment = self.env['ir.attachment']
   ..
   25          return res
   26  
   27:     @api.multi
   28      def action_open_attachments(self):
   29          self.ensure_one()
   ..
   46      attachment_count = fields.Integer(compute='_compute_attachment_count', string="File")
   47  
   48:     @api.multi
   49      def _compute_attachment_count(self):
   50          IrAttachment = self.env['ir.attachment']
   ..
   54              product.attachment_count = result.get(product.id, 0)
   55  
   56:     @api.multi
   57      def action_open_attachments(self):
   58          self.ensure_one()

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/res_config.py:
   19          }
   20  
   21:     @api.multi
   22      def set_website_slide_google_app_key(self):
   23          for wizard in self:

/home/shivamm/Desktop/odoo-9.0/addons/website_slides/models/slides.py:
  115          self.can_upload = self.can_see and (not self.upload_group_ids or bool(self.upload_group_ids & self.env.user.groups_id))
  116  
  117:     @api.multi
  118      @api.depends('name')
  119      def _website_url(self, name, arg):
  ...
  310                  record.embed_code = False
  311  
  312:     @api.multi
  313      @api.depends('name')
  314      def _website_url(self, name, arg):
  ...
  344          return slide
  345  
  346:     @api.multi
  347      def write(self, values):
  348          if values.get('url'):

597 matches across 143 files
