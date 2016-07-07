Move around workflow states back and forth?
-----------------------------------------------
-----------------------------------------------

class Sale_order(osv.Model):

    _inherit = 'sale.order'

    _columns = {
        'state': fields.selection(
            [
            ('draft', 'Draft Quotation'),
             # New State Added
            ('my_new_state', 'My New State'),
            ('sent', 'Quotation Sent'),
            ('cancel', 'Cancelled'),
            ('waiting_date', 'Waiting Schedule'),
            ('progress', 'Sales Order'),
            ('manual', 'Sale to Invoice'),
            ('invoice_except', 'Invoice Exception'),
            ('done', 'Done'),
            ], 
            'Status', 
            readonly=True, 
            track_visibility='onchange',
            help="Gives the status of the quotation or sales order. \nThe exception status is automatically set when a cancel operation occurs in the processing of a document linked to the sales order. \nThe 'Waiting Schedule' status is set when the invoice is confirmed but waiting for the scheduler to run on the order date.", 
            select=True
            ),
    }



    <openerp>
    <data>

        # <!-- Inherit the sale order model's form view and customize -->
        <record id="sale_form_view" model="ir.ui.view">
            <field name="name">sale.order.form.inherit</field>
            <field name="model">sale.order</field>
            <field name="inherit_id" ref="sale.view_order_form"/>
            <field name="arch" type="xml">
                <!-- Statusbar widget should also contain the new status -->
                <field name="state" position="replace">
                    <field name="state" widget="statusbar" statusbar_visible="draft,my_new_state,sent,invoiced,done" statusbar_colors='{"invoice_except":"red","waiting_date":"blue"}'/>
                </field>
            </field>
        </record>



    </data>
</openerp>


sale_workflow.xml





<openerp>
    <data>

# That code tells OpenERP that once a user arrives to this activity 
# (which is a part of an existing sale.wkf_sale workflow) 
# via some transition, a python function called action_my_new_function() should be executed. 


        <!-- Create new activity for the new state -->
        <record id="act_my_new_state" model="workflow.activity">
            <field name="wkf_id" ref="sale.wkf_sale"/>
             # <field name="flow_start">True</field>/<field name="flow_stop">True</field>
            <field name="name">my_new_state</field>
            <field name="kind">function</field>
            <field name="action">action_my_new_function()</field>
        </record>

# Let's say we want to be able to progress from 
# Draft Quotation to My New State, from
#  My New State to Quotation Sent, 
# and also go back from Quotation Sent to My New State. For that we need the following transitions:


        <!-- Create transitions -->

        <!-- From Draft to new state -->
        <record id="trans_draft_my_new_state" model="workflow.transition">
            <field name="act_from" ref="sale.act_draft"/>
            <field name="act_to" ref="act_my_new_state"/>
            <field name="signal">signal_my_new_state_forward</field>
        </record>    

        <!-- From new state to Quotation Sent -->
        <record id="trans_new_state_sent" model="workflow.transition">
            <field name="act_from" ref="act_my_new_state"/>
            <field name="act_to" ref="sale.act_sent"/>
            <field name="signal">signal_quotation_sent</field>
        </record>

        <!-- From Quotation Sent back to new state -->
        <record id="trans_sent_new_state" model="workflow.transition">
            <field name="act_from" ref="sale.act_sent"/>
            <field name="act_to" ref="act_my_new_state"/>
            <field name="signal">signal_my_new_state_backward</field>
        </record>  

    </data>
</openerp>

# The signals tell what user inputs are used to trigger the transition, 
# In our example we'll use the press of a button as a trigger. 
# Let's add new buttons to the form view definition. Note the states attributes, 
# they limit in which states the button will be visible. 
# The name attribute of the button matches the signal defined in the workflow and 
# thus triggers the transition to a specific activity.



<?xml version="1.0" encoding="UTF-8"?>
<openerp>
    <data>
        <!-- Inherit the sale order model's form view and customize -->
        <record id="sale_form_view" model="ir.ui.view">
            <field name="name">sale.order.form.inherit</field>
            <field name="model">sale.order</field>
            <field name="inherit_id" ref="sale.view_order_form"/>
            <field name="arch" type="xml">

                <!-- Statusbar widget should also contain the new statuses -->
                <field name="state" position="replace">
                    <field name="state" widget="statusbar" statusbar_visible="draft,my_new_state,sent,invoiced,done" statusbar_colors='{"invoice_except":"red","waiting_date":"blue"}'/>
                </field>

                <field name="state" position="before">
                    <!-- From draft to new state -->
                    <button string="Send to new state" type="workflow" name="signal_my_new_state_forward" states="draft" class="oe_highlight"/>

                    <!-- From new state to Quotation Sent -->
                    <button string="Mark as sent" type="workflow" name="signal_quotation_sent" states="my_new_state" class="oe_highlight"/> 

                    <!-- From Quotation Sent back to new state -->
                    <button string="Back to new state" type="workflow"  name="signal_my_new_state_backward" states="sent" class="oe_highlight"/>
                </field>
            </field>
        </record>
    </data>
</openerp>

Python code that actually changes the sale order's state on button click. 
little code that is put inside our sale order subclass
Note that the function name is the same as in the action of our new activity, i.e. action_my_new_function()

def action_my_new_function(self, cr, uid, ids, context=None):
    res = self.write(cr, uid, ids, {'state': 'my_new_state'}, context=context)    
    return res
