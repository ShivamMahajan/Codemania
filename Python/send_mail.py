def send_mail(self, cr, uid, ids, context=None):
   email_template_obj = self.pool.get('email.template')
   template_ids = email_template_obj.search(cr, uid, [('model_id.model', '=','your.object.name')], context=context) 
   if template_ids:
         values = email_template_obj.generate_email(cr, uid, template_ids[0], ids, context=context)
         values['subject'] = subject 
         values['email_to'] = email_to
         values['body_html'] = body_html
         values['body'] = body_html
         values['res_id'] = False
         mail_mail_obj = self.pool.get('mail.mail')
         msg_id = mail_mail_obj.create(cr, uid, values, context=context)
         if msg_id:
               mail_mail_obj.send(cr, uid, [msg_id], context=context) 
   return True