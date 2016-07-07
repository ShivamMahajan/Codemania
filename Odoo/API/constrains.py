Searching 18994 files for "@api.constrains"

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account.py:
   90  
   91      @api.multi
   92:     @api.constrains('internal_type', 'reconcile')
   93      def _check_reconcile(self):
   94          for account in self:
   ..
  253  
  254      @api.one
  255:     @api.constrains('currency_id', 'default_credit_account_id', 'default_debit_account_id')
  256      def _check_currency(self):
  257          if self.currency_id:
  ...
  262  
  263      @api.one
  264:     @api.constrains('type', 'bank_account_id')
  265      def _check_bank_account(self):
  266          if self.type == 'bank' and self.bank_account_id:
  ...
  464  
  465      @api.one
  466:     @api.constrains('journal_id')
  467      def _check_journal_id(self):
  468          if len(self.journal_id) > 1:
  ...
  519  
  520      @api.one
  521:     @api.constrains('children_tax_ids', 'type_tax_use')
  522      def _check_children_scope(self):
  523          if not all(child.type_tax_use in ('none', self.type_tax_use) for child in self.children_tax_ids):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_bank_statement.py:
  380  
  381      @api.one
  382:     @api.constrains('amount')
  383      def _check_amount(self):
  384          # This constraint could possibly underline flaws in bank statement import (eg. inability to
  ...
  388  
  389      @api.one
  390:     @api.constrains('amount', 'amount_currency')
  391      def _check_amount_currency(self):
  392          if self.amount_currency != 0 and self.amount == 0:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_invoice.py:
 1200      company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.user.company_id)
 1201  
 1202:     @api.constrains('line_ids')
 1203      @api.one
 1204      def _check_lines(self):
 ....
 1269  
 1270      @api.one
 1271:     @api.constrains('value', 'value_amount')
 1272      def _check_percent(self):
 1273          if self.value == 'percent' and (self.value_amount < 0.0 or self.value_amount > 100.0):

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_move.py:
  370  
  371      @api.multi
  372:     @api.constrains('currency_id', 'account_id')
  373      def _check_currency(self):
  374          for line in self:
  ...
  378  
  379      @api.multi
  380:     @api.constrains('currency_id', 'amount_currency')
  381      def _check_currency_and_amount(self):
  382          for line in self:
  ...
  385  
  386      @api.multi
  387:     @api.constrains('amount_currency')
  388      def _check_currency_amount(self):
  389          for line in self:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/account_payment.py:
   50  
   51      @api.one
   52:     @api.constrains('amount')
   53      def _check_amount(self):
   54          if not self.amount > 0.0:

/home/shivamm/Desktop/odoo-9.0/addons/account/models/partner.py:
   39  
   40      @api.one
   41:     @api.constrains('zip_from', 'zip_to')
   42      def _check_zip(self):
   43          if self.zip_from > self.zip_to:

/home/shivamm/Desktop/odoo-9.0/addons/account_asset/account_asset.py:
  311  
  312      @api.one
  313:     @api.constrains('prorata', 'method_time')
  314      def _check_prorata(self):
  315          if self.prorata and self.method_time != 'number':

/home/shivamm/Desktop/odoo-9.0/addons/barcodes/barcodes.py:
  209  
  210      @api.one
  211:     @api.constrains('pattern')
  212      def _check_pattern(self):
  213          p = self.pattern.replace("\\\\", "X").replace("\{", "X").replace("\}", "X")

/home/shivamm/Desktop/odoo-9.0/addons/base_iban/base_iban.py:
   71  
   72      @api.one
   73:     @api.constrains('acc_number')
   74      def _check_iban(self):
   75          if self.acc_type == 'iban':

/home/shivamm/Desktop/odoo-9.0/addons/event/models/event.py:
  193  
  194      @api.one
  195:     @api.constrains('seats_max', 'seats_available')
  196      def _check_seats_limit(self):
  197          if self.seats_availability == 'limited' and self.seats_max and self.seats_available < 0:
  ...
  199  
  200      @api.one
  201:     @api.constrains('date_begin', 'date_end')
  202      def _check_closing_date(self):
  203          if self.date_end < self.date_begin:
  ...
  293  
  294      @api.one
  295:     @api.constrains('event_id', 'state')
  296      def _check_seats_limit(self):
  297          if self.event_id.seats_availability == 'limited' and self.event_id.seats_max and self.event_id.seats_available < (1 if self.state == 'draft' else 0):

/home/shivamm/Desktop/odoo-9.0/addons/event_sale/models/event.py:
  126  
  127      @api.one
  128:     @api.constrains('registration_ids', 'seats_max')
  129      def _check_seats_limit(self):
  130          if self.seats_max and self.seats_available < 0:
  ...
  148  
  149      @api.one
  150:     @api.constrains('event_ticket_id', 'state')
  151      def _check_ticket_seats_limit(self):
  152          if self.event_ticket_id.seats_max and self.event_ticket_id.seats_available < 0:

/home/shivamm/Desktop/odoo-9.0/addons/exam/models/exam.py:
  336      _rec_name = 'subject_id'
  337  
  338:     @api.constrains('obtain_marks', 'minimum_marks')
  339      def _validate_marks(self):
  340          if (self.obtain_marks > self.maximum_marks
  ...
  428          return {'value': val}
  429  
  430:     @api.constrains('obtain_marks')
  431      def _validate_marks(self):
  432          if self.obtain_marks > self.a_exam_id.subject_id.maximum_marks:

/home/shivamm/Desktop/odoo-9.0/addons/lunch/models/lunch.py:
   88  
   89      @api.one
   90:     @api.constrains('date')
   91      def _check_date(self):
   92          """

/home/shivamm/Desktop/odoo-9.0/addons/mail/models/mail_alias.py:
   92  
   93      @api.one
   94:     @api.constrains('alias_defaults')
   95      def _check_alias_defaults(self):
   96          try:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_activity/wizard/student_migrate_wizard.py:
   36  
   37      @api.one
   38:     @api.constrains('course_from_id', 'course_to_id')
   39      def _check_admission_register(self):
   40          if self.course_from_id == self.course_to_id:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission.py:
  121  
  122      @api.one
  123:     @api.constrains('register_id', 'application_date')
  124      def _check_admission_register(self):
  125          start_date = fields.Date.from_string(self.register_id.start_date)
  ...
  132  
  133      @api.one
  134:     @api.constrains('birth_date')
  135      def _check_birthdate(self):
  136          if self.birth_date > fields.Date.today():

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_admission/models/admission_register.py:
   63  
   64      @api.one
   65:     @api.constrains('start_date', 'end_date')
   66      def check_dates(self):
   67          start_date = fields.Date.from_string(self.start_date)
   ..
   71  
   72      @api.one
   73:     @api.constrains('min_count', 'max_count')
   74      def check_no_of_admission(self):
   75          if (self.min_count < 0) or (self.max_count < 0):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_assignment/models/assignment.py:
   57  
   58      @api.one
   59:     @api.constrains('issued_date', 'submission_date')
   60      def check_dates(self):
   61          issued_date = fields.Date.from_string(self.issued_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_attendance/wizards/student_attendance_wizard.py:
   33  
   34      @api.one
   35:     @api.constrains('from_date', 'to_date')
   36      def check_dates(self):
   37          from_date = fields.Date.from_string(self.from_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/batch.py:
   35  
   36      @api.one
   37:     @api.constrains('start_date', 'end_date')
   38      def check_dates(self):
   39          start_date = fields.Date.from_string(self.start_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/faculty.py:
   54  
   55      @api.one
   56:     @api.constrains('birth_date')
   57      def _check_birthdate(self):
   58          if self.birth_date > fields.Date.today():

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_core/models/student.py:
   68  
   69      @api.one
   70:     @api.constrains('birth_date')
   71      def _check_birthdate(self):
   72          if self.birth_date > fields.Date.today():

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam.py:
   51      min_marks = fields.Float('Passing Marks', required=True)
   52  
   53:     @api.constrains('total_marks', 'min_marks')
   54      def _check_marks(self):
   55          if self.total_marks <= 0.0 or self.min_marks <= 0.0:
   ..
   59                  "Passing Marks can't be greater than Total Marks")
   60  
   61:     @api.constrains('start_time', 'end_time')
   62      def _check_date_time(self):
   63          if self.start_time > self.end_time:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_attendees.py:
   44          self.student_id = False
   45  
   46:     @api.constrains('marks')
   47      def _check_marks(self):
   48          if self.marks < 0.0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_room.py:
   33      student_ids = fields.Many2many('op.student', string='Student(s)')
   34  
   35:     @api.constrains('capacity')
   36      def check_capacity(self):
   37          if self.capacity < 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/exam_session.py:
   37      exam_ids = fields.One2many('op.exam', 'session_id', 'Exam(s)')
   38  
   39:     @api.constrains('start_date', 'end_date')
   40      def _check_date_time(self):
   41          if self.start_date > self.end_date:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/marksheet_line.py:
   38      result = fields.Char("Result", size=256)
   39  
   40:     @api.constrains('total_marks', 'total_per')
   41      def _check_marks(self):
   42          if (self.total_marks < 0.0) or (self.total_per < 0.0):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/marksheet_register.py:
   43      name = fields.Char('Marksheet Register', size=256, required=True)
   44  
   45:     @api.constrains('total_pass', 'total_failed')
   46      def _check_marks(self):
   47          if (self.total_pass < 0.0) or (self.total_failed < 0.0):

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_exam/models/result_line.py:
   41      total_marks = fields.Float('Total Marks')
   42  
   43:     @api.constrains('marks', 'per')
   44      def _check_marks(self):
   45          if (self.marks < 0.0) or (self.per < 0.0) or \

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_facility/models/facility_line.py:
   31      quantity = fields.Float('Quantity', required=True)
   32  
   33:     @api.constrains('quantity')
   34      def check_quantity(self):
   35          if self.quantity <= 0.0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_health/models/health.py:
   51          'op.health.line', 'health_id', 'Checkup Lines')
   52  
   53:     @api.constrains('height', 'weight')
   54      def check_height_weight(self):
   55          if self.height <= 0.0 or self.weight <= 0.0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/hostel.py:
   33  
   34      @api.one
   35:     @api.constrains('hostel_room_lines')
   36      def _check_hostel_capacity(self):
   37          if self.capacity <= 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/hostel_room.py:
   34      allocated_date = fields.Date('Allocated Date', default=fields.Date.today())
   35  
   36:     @api.constrains('students_per_room')
   37      def check_capacity(self):
   38          if self.students_per_room <= 0:
   ..
   50  
   51      @api.one
   52:     @api.constrains('student_ids', 'students_per_room')
   53      def _check_student_capacity(self):
   54          if len(self.student_ids) > self.students_per_room:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_hostel/models/room.py:
   33      facility_line = fields.One2many('op.facility.line', 'room_id', 'Facility')
   34  
   35:     @api.constrains('capacity')
   36      def check_capacity(self):
   37          if self.capacity <= 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_movement.py:
   62          default='available', track_visibility='onchange')
   63  
   64:     @api.constrains('issued_date', 'return_date')
   65      def _check_date(self):
   66          if self.issued_date > self.return_date:
   ..
   68                  'Return Date cannot be set before Issued Date.')
   69  
   70:     @api.constrains('issued_date', 'actual_return_date')
   71      def check_actual_return_date(self):
   72          if self.actual_return_date:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/book_queue.py:
   48          self.partner_id = self.user_id.partner_id.id
   49  
   50:     @api.constrains('date_from', 'date_to')
   51      def _check_date(self):
   52          if self.date_from > self.date_to:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/models/library.py:
   35      penalty_amt_per_day = fields.Float('Penalty Amount per Day', required=True)
   36  
   37:     @api.constrains('allow_book', 'duration', 'penalty_amt_per_day')
   38      def check_details(self):
   39          if self.allow_book < 0 or self.duration < 0.0 or \

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_library/wizards/issue_book.py:
   45      return_date = fields.Date('Return Date', required=True)
   46  
   47:     @api.constrains('issued_date', 'return_date')
   48      def _check_date(self):
   49          if self.issued_date > self.return_date:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_scholarship/models/scholarship_type.py:
   30      amount = fields.Integer('Amount')
   31  
   32:     @api.constrains('amount')
   33      def check_amount(self):
   34          if self.amount <= 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/models/timetable.py:
   45           ('Friday', 'Friday'), ('Saturday', 'Saturday')], 'Days')
   46  
   47:     @api.constrains('start_datetime', 'end_datetime')
   48      def _check_date_time(self):
   49          if self.start_datetime > self.end_datetime:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/generate_timetable.py:
   68      end_date = fields.Date('End Date', required=True)
   69  
   70:     @api.constrains('start_date', 'end_date')
   71      def check_dates(self):
   72          start_date = fields.Date.from_string(self.start_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_timetable/wizard/time_table_report.py:
   48  
   49      @api.one
   50:     @api.constrains('start_date', 'end_date')
   51      def _check_dates(self):
   52          start_date = fields.Date.from_string(self.start_date)

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_transportation/models/transportation.py:
   37      student_ids = fields.Many2many('op.student', string='Student(s)')
   38  
   39:     @api.constrains('student_ids', 'vehicle_id')
   40      def check_capacity(self):
   41          if len(self.student_ids) > self.vehicle_id.capacity:
   42              raise ValidationError('Students over than vehicle capacity.')
   43  
   44:     @api.constrains('from_stop_id', 'to_stop_id')
   45      def check_places(self):
   46          if self.from_stop_id == self.to_stop_id:
   47              raise ValidationError('To place cannot be equal to From place.')
   48  
   49:     @api.constrains('start_time', 'end_time')
   50      def _check_date_time(self):
   51          if self.start_time < 0 or self.end_time < 0:

/home/shivamm/Desktop/odoo-9.0/addons/openeducat_transportation/models/vehicle.py:
   33      partner_id = fields.Many2one('res.partner', 'Driver')
   34  
   35:     @api.constrains('capacity')
   36      def check_capacity(self):
   37          if self.capacity <= 0:

/home/shivamm/Desktop/odoo-9.0/addons/sale_timesheet/models/sale_timesheet.py:
   88  
   89      @api.multi
   90:     @api.constrains('order_line')
   91      def _check_multi_timesheet(self):
   92          for order in self:

/home/shivamm/Desktop/odoo-9.0/addons/website_forum/models/forum.py:
  133  
  134      @api.one
  135:     @api.constrains('allow_question', 'allow_discussion', 'allow_link', 'default_post_type')
  136      def _check_default_post_type(self):
  137          if (self.default_post_type == 'question' and not self.allow_question) \
  ...
  141  
  142      @api.one
  143:     @api.constrains('allow_link', 'allow_question', 'allow_discussion', 'default_post_type')
  144      def _check_default_post_type(self):
  145          if self.default_post_type == 'link' and not self.allow_link or self.default_post_type == 'question' and not self.allow_question or self.default_post_type == 'discussion' and not self.allow_discussion:
  ...
  376  
  377      @api.one
  378:     @api.constrains('post_type', 'forum_id')
  379      def _check_post_type(self):
  380          if (self.post_type == 'question' and not self.forum_id.allow_question) \

67 matches across 46 files
