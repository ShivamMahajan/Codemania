
nolabel='1' Doesnt display the field name (object name which will be shown by default

___________________________________________________________________________________

__________________________________________ORM Methods and User Defined Methods___________________________

self =The first argument of every class method, including __init__, is always a reference to the current instance of the class. By convention, this argument is always named self. In the __init__ method, self refers to the newly created object; in other class methods, it refers to the instance whose method was called
Context: is a dictionary which contains some information like: user language, company, timezone, etc by default. You can pass any kind of data/information in context as per your need either from xml or from py (mehtods) and then based on that extra information you can write your process code.

Domain: is a condition(s) which is used to filter your data or for searching

def create(self, cr, uid, vals, context=None):
    	# vals is a dictionary containing all the variable of the current object 
        print vals['name'] # name is the field name
        print vals['active'] # active is the  field name
        # Print Id of record
        k=super(skillset, self).create(cr, uid, vals, context=None) # skillset is the name of class 
        print k # the super method is called to override the vreate method
        # Must return
        return k 

def write(self, cr, uid, ids,vals,context=None):
        # vals is a dictionary  only containing  the updated variable of the current object
        # The current id of the record
        print vals
        vals['name']='PYTHON' # update the value of the variable
        # Returns the id of the uodate recored which is equal to ids
        return super(skillset, self).write(cr, uid, ids,vals, context=None)# skillset is the name of class 
 
def user_defined_method(self, cr, uid, ids, context=None):
    # ids The current id of the record

def onchange_user_id(self, cr, uid, ids, user_id, context=None):
     # This method is called on changing the user_id field value
     # user_id is the changed field      
    return {'value': {'parent_id': f,'department':d}}

    where the parent_id and department are the felds defined in the object
    and f and d are the variables

        
  <field name="user_id" placeholder="Task summary..." class="oe_inline" on_change="onchange_user_id(user_id)" />


context['active_id'] =Gives the id of the current record



Calling Function
self.get_company_id_apply_leave_policy(cr,uid,ids,context=None) 

Search & Browse

model = self.pool.get(MODEL) # model name
ids = model.search(cr, uid, DOMAIN, context=context) # ids of record satisfying the domain criteria
for rec in model.browse(cr, uid, ids, context=context): # record set
    print rec.name # recordest field
    model.write(cr, uid, ids, VALUES, context=context) # update the field of model

    may also be written as::

env = Env(cr, uid, context)         # cr, uid, context wrapped in env
recs = env[MODEL]                   # retrieve an instance of MODEL
recs = recs.search(DOMAIN)          # search returns a recordset
for rec in recs:                    # iterate over the records
    print rec.name
recs.write(VALUES)                  # update all records in recs





# hr.employee model Object 
employee_obj=self.pool.get('hr.employee')
#list of ids who match the criteria
employee_obj_id=employee_obj.search(cr,uid,[('name_related','=',"Shivam Mahajan")])
#i=self.search(cr,uid,[]) # all records because there is no domain
#Record Set matching the criteria
e=employee_obj.browse(cr,uid,employee_obj_id,context=None)
# ID of the record
print e.id
# The field name of the recordset
print e.name_related
# The name of the manager
print e.parent_id.name_related
#The name of the Super Manager
print e.parent_id.parent_id.name_related



def _get_nbr_employees(self, cr, uid, ids, name, args, context=None): # functional field
_________________________________________________________________________________________________________

_________________________________________Wizard__________________________________________________________


 Wizard

Calling A Wizard 

        <button string="Details" name="%(skillset.action_skillset_intro)d" type="action" />
skillset :Module name
action_skillset_intro :action+action_name

Wizrd Window

        <record id="skillset_intro" model="ir.actions.act_window">
            <field name="name">Add Description</field>
            <field name="type">ir.actions.act_window</field>
            <field name="res_model">skillset.intro</field>
            <field name="view_type">form</field>
            <field name="view_mode">form</field>
            <field name="target">new</field>
        </record>

     
_________________________________________________________________________________________________________

_________________________________________View Inheritance________________________________________________


View Inheritance

_inherit='project.task'

<record id="edit_res_company" model="ir.ui.view">
            <field name="name">custom.module.form</field>
            <field name="model">res.company</field> # Inherited Module
            <field name="inherit_id" ref="base.view_company_form"/>

            base=name of the module
            <field name="arch" type="xml">
             
                <field name="name" position="after">
                <field name="domain_name"/> -->

                            OR
                <xpath expr="//field[@name='name']" position="after" >
                    <field name="domain_name" />
                </xpath>
        
        </record>


_________________________________________________________________________________________________________

_________________________________________many2many field________________________________________________

rel_ids = fields.Many2many(comodel_name='res.users',
                            relation='table_name',
                            column1='col_name',
                            column2='other_col_name')

Specific options:

        comodel_name: name of the opposite model
        relation: relational table name (table to be created containing the relation)
        columns1: relational table left column name :The id of current object
        columns2: relational table right column name :The id of opposite object

<field name="company" widget="many2many_tags"/>


<field name="company_id" widget="selection"/> 

For a many2many field, a list of tuples is expected. Here is the list of tuple that are accepted, with the corresponding semantics

(0, 0,  { values }) link to a new record that needs to be created with the given values dictionary

(1, ID, { values }) update the linked record with id = ID (write values on it)

(2, ID) remove and delete the linked record with id = ID (calls unlink on ID, that will delete the object completely, and the link to it as well)

(3, ID) cut the link to the linked record with id = ID (delete the relationship between the two objects but does not delete the target object itself)

(4, ID) link to existing record with id = ID (adds a relationship)

(5) unlink all (like using (3,ID) for all linked records)

(6, 0, [IDs]) replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)

________________________________________________________________________________________________________

_____________________one2many field for the tree view in form view like a page in notebook_______________


class res_company(osv.osv):
    _inherit = 'res.company'

    _columns = {
        ':fields.one2many('employee_access.detail','company_id',string="Employee"),
    }

class employee_access_detail(osv.osv):
    _name="employee_access.detail"

    _columns={
        'company_id':fields.many2one('res.company',string="Company"),
        'email_login':fields.char("Email",required=True),
        'user_name':fields.char("Name",required=True),
    }

    <record model="ir.ui.view" id="edit_res_company_email_form">
      <field name="name">User Email Form View</field>
      <field name="model">res.company</field>
      <field name="inherit_id" ref="base.view_company_form"/>
      <field name="arch" type="xml">
        <page string="Report Configuration" position="after">
          <page string="Users">
            <field name="employee_access">
              <tree editable="bottom">
                <field name="user_name"/>
                <field name="email_login"/>
              </tree>
            </field>
          </page>



________________________________________________________________________________________________________

_________________________________________Groups__________________________________________________________


groups="base.group_system" :Admin User Group
base.group_system
base.group_hr_user
base.group_user

_________________________________________________________________________________________________________
_________________________Disable the Create and Edit button in the created form__________________________
 
 <form string="Leave Request" create="false" edit="false" delete="false">




----------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Functional Field
----------------------------------------------------------------------------------------------------------------------------------------------------------

def _default_get(self, cr, uid, context=None):
    print " This function called before new record create "
    res = 'bhavesh'
    return res     

def _set_value(self, cr, uid, ids, name, args, context=None):
    print " This function called at time of saving record and form view load "
    res = {}
    for i in self.browse(cr, uid, ids, context=context):
        res[i.id] = 'odedra'
    return res

_columns = {
    'value': fields.function(_set_value, type='char', string='Value'),
}

_defaults = {
    'value': _default_get,
}

# Note :The value of functional field doesn't get saved in database .



---------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------

'image': fields.binary("Photo",
            help="This field holds the image used as photo for the employee, limited to 1024x1024px."),
        'image_medium': fields.function(_get_image, fnct_inv=_set_image,
            string="Medium-sized photo", type="binary", multi="_get_image",
            store = {
                'hr.employee': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Medium-sized photo of the employee. It is automatically "\
                 "resized as a 128x128px image, with aspect ratio preserved. "\
                 "Use this field in form views or some kanban views."),
        'image_small': fields.function(_get_image, fnct_inv=_set_image,
            string="Small-sized photo", type="binary", multi="_get_image",
            store = {
                'hr.employee': (lambda self, cr, uid, ids, c={}: ids, ['image'], 10),
            },
            help="Small-sized photo of the employee. It is automatically "\
                 "resized as a 64x64px image, with aspect ratio preserved. "\
                 "Use this field anywhere a small image is required."),


Odoo - how to properly copy views from other model



class my_model(models.Model):

_name = 'my.model'

field1 = fields.Char('name')




class my_model_template(models.Model):

_name = 'my.model.template'

_inherit = 'my.model'






You need to specify which view to open for which view mode. Because when you copy another model's view, it seems it does not find correct view automatically (even if only one is defined for each mode)

<record model="ir.actions.act_window.view" id="action_my_model_template_tree">
    <field name="sequence" eval="1"/>
    <field name="view_mode">tree</field>
    <field name="view_id" ref="view_my_model_template_tree"/>
    <field name="act_window_id" ref="action_my_model_template"/>
</record>     

<record model="ir.actions.act_window.view" id="action_my_model_template_form">
    <field name="sequence" eval="1"/>
    <field name="view_mode">form</field>
    <field name="view_id" ref="view_my_model_template_form"/>
    <field name="act_window_id" ref="action_my_model_template"/>
</record> 

Note Also if you will use such model anywhere in other models views and you try to open it's form directly from that other view, it will also open "unformatted" view. To bypass this too, you need to specify view to open:

For example like this:

<record id="view_my_other_model_form" model="ir.ui.view">
    <field name="name">my.other.model.form</field>
    <field name="model">my.other.model.</field>
    <field name="arch" type="xml">
        <form string="My Other Model">
            <field name="my_model_template_id" 
                context="{'form_view_ref': 'my_model_template.view_my_model_template_form'}"/>
        </form>
    </field>
</record>

CReating Filter and Group BY
     
     <record id="view_task_search_form" model="ir.ui.view">
            <field name="name">project.task.search.form</field>
            <field name="model">project.task</field>
            <field name="arch" type="xml">
               <search string="Tasks">
                    <field name="name" string="Tasks"/>
                    <field name="categ_ids"/>
                    <field name="partner_id"/>
                    <field name="project_id" />
                    <field name="reviewer_id"/>
                    <field name="user_id" />
                    <field name="stage_id"/>
                    <filter string="My Tasks" domain="[('user_id','=',uid)]"/>
                    <filter string="Unassigned" name="unassigned" domain="[('user_id', '=', False)]"/>
                    <separator/>
                    <filter string="New" name="draft" domain="[('stage_id.sequence', '&lt;=', 1)]"/>
                    <separator/>
                    <filter string="New Mail" name="message_unread" domain="[('message_unread','=',True)]"/>
                    <group expand="0" string="Group By">
                        <filter string="Project" name="project" context="{'group_by':'project_id'}"/>
                        <filter string="Task" context="{'group_by':'name'}"/>
                        <filter string="Assigned to" name="User" context="{'group_by':'user_id'}"/>
                        <filter string="Stage" name="Stage" context="{'group_by':'stage_id'}"/>
                        <filter string="Company" context="{'group_by':'company_id'}" groups="base.group_multi_company"/>
                        <separator/>
                        <filter string="Last Message" name="group_message_last_post" context="{'group_by':'message_last_post:week'}"/>
                        <filter string="Assignation Month" context="{'group_by':'date_start:month'}" help="Creation Date"/>
                    </group>
                </search>
            </field>
        </record>



'parent_id': fields.many2one('hr.employee', 'Manager'),
'child_ids': fields.one2many('hr.employee', 'parent_id', 'Subordinates'),


0
Attach many files in a binary field type

<field name="attachment_ids" widget="many2many_binary"/>
You can find it here: /mail/wizard/mail_compose_message_view.xml





1
Temur
On 5/4/15, 8:37 PM

For remember easily, you can assume that in database "ID's are saved at «many» side" i.e. if you've two objects(models) 'object_a' and 'object_b' and you've relational field in the 'object_a' :

    if field type is one2many, then ID's(of object_a) are saved in 'object_b' (object_b is at «many» side, it contains ids)
        i.e fields.ome2many('object_b',object_a_id)
a----------------->>>>>>>>>>b

    if field type is 'many2one', then ID's(of object_b) are saved in 'object_a' (object_a is at «many» side, it contains ids)
        fields.many2one('object_b,')
a<<<<<<<<<<<<--------------b

    if field type is many2many, then ID's(of both objects) are saved in the separated table (it's exception as ids are not either in A or in B, but they are in the table that may be named using "relation" parameter of many2many field)
        fields.many2many('obje')

        a <<<<<<----------------->>>>>>>>>>b

--------------------------------------------------------------------------------------
----------------------------------------------------------------------------------
    This method is called when group by is done

    def read_group(self, cr, uid, domain, fields, groupby, offset=0, limit=None, context=None, orderby=False, lazy=True):
        print domain --[]
        print fields ---[]
        print groupby ---[]
        print type (groupby) --list
        res=super(Project_Task_Work,self).read_group(cr, uid, domain, fields, groupby, offset, limit, context, orderby, lazy)
        print res ---return list of dictionary
        return res

  --------------------------------------------------------------------------------------
----------------------------------------------------------------------------------


    
    



    Access Rights are CRUD yes/no flags (similar to Unix FS permissions), and allow per-model access control. They state whether members of this group may perform a Create, Read, Update, and Delete operation on any document of a certain document model (e.g. a project task). The default policy is DENY, so by default any operation will be refused if the user does not explicitly have the right to perform it via one of her groups' access rights.
    Record Rules are filters applied on CRUD operations, and allow per-document access-control, once access right are already granted. Users will only be able to perform an operation on a given document if the document matches at least one of the record rules. The default policy is ALLOW, so if no rule exists for a given model, all documents of that model may be accessed by users who have the necessary access rights.

Both Access Rights and Record Rules may also be defined globally without assigning them to a specific group, in which case they apply to everyone. There is one pitfall for Record Rules: global rules may NOT be relaxed by other rules (on purpose!), so use with care.

In your case it looks like you should define one extra Record Rule on the Project User group that explicitly restricts access on Project Tasks to your own tasks (and presumably those that are not assigned yet). You need to create a new entry in the Security Rules menu with these parameters:

    object/model: project.task
    name: See own tasks only
    domain: ['|',('user_id','=',False),('user_id','=',user.id)]
        (means: your own tasks and unassigned ones)
    apply for read: [x]
    apply for write: [x]
    apply for create: [x]
    apply for delete: [x]
    groups: Project / User

The domain of a record rule is a standard OpenERP domain that is evaluated on the records on which you are trying to perform the operation, and can refer to a user variable that contains the current user's data (technically, a browse_record on the current user). Look for search() in the list of ORM methods for a full description of domain.

If you want to allow special users (e.g. Project Managers) to view all tasks in the system, you can relax this rule for them by adding another rule to the Project Manager group which allows access to all tasks. There is a special "domain filter" that means "ALLOW ALL" and is useful to relax another stricter rule: [(1,'=',1)].

Note: Have a look at the existing Record Rules to see what they're doing first, and be sure to read the explanations on the Record Rule form when you are adding yours. And remember that if you do something wrong with Access Rights and Record Rules, you can always fix the mess with the admin account, as these security restrictions do not apply to the admin (similarly to the root user on Unix).



<form string="NAMEOFFORM" create="false" edit="false" version="7.0" delete="false">
 This way "Edit" and "Create" are removed from view for all Users.












Fields_view_get in Odoo
Many times, we are not sure with the exact view of form, also number of fields to be presented 
or their properties. 
It varies as per User’s choice. 
This is place where we need to load views dynamically.
The method used to load dynamic view is fields_view_get(

So, in Odoo there is fields_view_get() method in which we can load views as per user’s preferrences.Odoo matches this requirement through fields_view_get method to great extent.

The syntax of method is as follows:

def fields_view_get(self, cr, uid, view_id=None, view_type=’form’, context=None, toolbar=False, submenu=False)

If we only want to alter propeties of fields,then  fields_view_get also provide scope for that.
You can change “onchange”  function or readonly ,required property of a particular field.

http://elico-corp.com.sg/2015/10/01/how-to-tech-dynamically-modify-your-view/

OpenERP Object Attributes
Objects Introduction

To define a new object, you must define a new Python class then instantiate it. This class must inherit from the osv class in the osv module.
Object definition

The first line of the object definition will always be of the form:

class name_of_the_object(osv.osv):
        _name = 'name.of.the.object'
        _columns = { ... }
        ...
name_of_the_object()

An object is defined by declaring some fields with predefined names in the class. Two of them are required (_name and _columns), the rest are optional. The predefined fields are:
Predefined fields

_auto

    Determines whether a corresponding PostgreSQL table must be generated automatically from the object. Setting _auto to False can be useful in case of OpenERP objects generated from PostgreSQL views. See the "Reporting From PostgreSQL Views" section for more details.
_columns (required)

    The object fields. See the fields section for further details.
_constraints

    The constraints on the object. See the constraints section for details.
_sql_constraints

    The SQL Constraint on the object. See the SQL constraints section for further details.
_defaults

    The default values for some of the object's fields. See the default value section for details.
_inherit

    The name of the osv object which the current object inherits from. See the object inheritance section (first form) for further details.
_inherits

    The list of osv objects the object inherits from. This list must be given in a python dictionary of the form: {'name_of_the_parent_object': 'name_of_the_field', ...}. See the object inheritance section (second form) for further details. Default value: {}.
_log_access

    Determines whether or not the write access to the resource must be logged. If true, four fields will be created in the SQL table: create_uid, create_date, write_uid, write_date. Those fields represent respectively the id of the user who created the record, the creation date of record, the id of the user who last modified the record, and the date of that last modification. This data may be obtained by using the perm_read method.
_name (required)

    Name of the object. Default value: None.
_order

    Name of the fields used to sort the results of the search and read methods.

    Default value: 'id'.

    Examples:

    _order = "name"
    _order = "date_order desc"

_rec_name

    Name of the field in which the name of every resource is stored. Default value: 'name'. Note: by default, the name_get method simply returns the content of this field.
_sequence

    Name of the SQL sequence that manages the ids for this object. Default value: None.
_sql

    SQL code executed upon creation of the object (only if _auto is True). It means this code gets executed after the table is created.
_table

    Name of the SQL table. Default value: the value of the _name field above with the dots ( . ) replaced by underscores ( _ ).


ondelete='cascade' (in many2one)
delete one2may records when parent record is deleted
delete the records in the one2many fields when the original record that had them is deleted.



 recordsets, a sorted set of records of the same model.
 Methods defined on a model are executed on a recordset, and their self is a recordset:Recordsets are immutable,



     The delegation inheritance inherits only fields and methods are not inherited. It can be useful, when we need to embed a model in our current model without affecting the existing views, but we want to have the fields of inherited objects.

    Any field not found in current model will be taken from the inherited models. You can have multiple inheritance, so that the new table created in DB contains your new fields and fields which delegates the inherited object fields (fields storing IDs from inherited tables.

        openerp-server --help



        






        
record.birthday <type 'str'>
till_datetime = datetime.strptime(record.birthday,"%Y-%m-%d")  # for date efield
1984-09-15 00:00:00 <type 'datetime.datetime'> 
interview_deadline = datetime.strptime(interview.deadline_2,"%Y-%m-%d %H:%M:%S") # for datetime field
The format to be passed in th strptime function based on date or datetime field
till_datetime = till_datetime.strftime("%Y-%m-%d 23:59:59")
984-09-15 23:59:59 <type 'str'>


    <menuitem
sequence="1" 
groups="base.group_no_one"
action="open_view_categ_form" 
id="menu_view_employee_category_form"
parent="hr.menu_hr_configuration"/>

uid
active_id
False
True
nolabel='1' Doesnt display the field name (object name which will be shown by default
default_order="id desc"  Sorting in view.xml
_order = "priority desc, sequence, date_start, name, id"  in python file.by default asc order 

<field name="limit">5</field>  in your action (XML file).

<field name="standard_id" operator="child_of" />
Using operator in search view
Using 'Child_of' operator In 'Parent-Child Relationship

Priority:
<field name="priority" eval="15"/>

attrs="{'readonly':[('stage_id','!=', 9)]}"

'priority': fields.selection([('0','Low'), ('1','Normal'), ('2','High')], 'Priority', select=True),
'0' '1' '2' are unicode characters not the integer
So intialize in the form
    vals['priority']='3'
   
Default sequence for menuitem is 10 .
They are sorted on the basis of their id created
______________________________________________________________________________________________________________________________________
   Differenece between  __init__() and init() 
    def __init__(self, cr, uid, name, context):
        super(account_analytic_balance, self).__init__(cr, uid, name, context=context)
        self.localcontext.update( {
            'time': time,
            'get_objects': self._get_objects,  # Method
            })

A constructor is a special kind of method that Python calls when it instantiates an object using the definitions found in your class
MyInstance = MyClass()

 Python relies on the constructor to perform tasks such as initializing (assigning values to) any instance variables that the object will need when it starts. Constructors can also verify that there are enough resources for the object and perform any other start-up task you can think of.

The name of a constructor is always the same, __init__(). The constructor can accept arguments when necessary to create the object. When you create a class without a constructor, Python automatically creates a default constructor for you that doesn’t do anything. Every class must have a constructor, even if it simply relies on the default constructor. 


def init(self, cr):


You can create a method init(self, cr) in your model and it will be called upon module installation or upgrade. 
You can check for update on install mode by checking the existence of data or structures that should have 
been created in initialization or you can just use common sql or replace mechanism to use the same sql for both states.

Most reports use this method to create required views


______________________________________________________________________________________________________________________________________

Method Overloading :
There is no function overloading in Python, meaning that you cant have multiple functions with the same name but different arguments.
Python supports overloading but in a Pythonic way. (using variable length arguments) *args

______________________________________________________________________________________________________________________________________


fields.property() 

'property_stock_procurement': fields.property(
        type='many2one',
        relation='stock.location',
        string="Procurement Location",
        view_load=True,
        domain=[('usage','like','procurement')],
        help="This stock location will be used, instead of the default one, as the source location for stock moves generated by procurements."),
        
        
       "The fields.property class inherits from fields.function and overrides the read and write method. 
       The type of this field is many2one, so in the form a property is represented like a many2one function. 
       But the value of a property is stored in the ir.property class/table as a complete record.
     The stored value is a field of type reference (not many2one) because each property may point to a different object. " 
     
     
     A property is a concept that is attached to an object and has special features:

    Different value for the same property depending on the company

    Rights management per field

    It's a link between resources (many2one)

So yes, it won't show in the database 'stock' table, but it will be in the ir_property table. 
This allows for different properties for the same object depending on the users current company.
There is some use cases where value of the field must change depending of the current company.

To activate such behavior you can now use the company_dependent option.

A notable evolution in new API is that “property fields” are now searchable.

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _columns = {
        'property_product_pricelist': fields.property(
            type='many2one', 
            relation='product.pricelist', 
            domain=[('type','=','sale')],
            string="Sale Pricelist", 
            help="This pricelist will be used, instead of the default one, for sales to the current partner"),
    }
Name :property_product_pricelist
Field :Sale Pricelist #Field Label 
 Resource  :  Resource 
 Value :product.pricelist,6  #Object Relation 
 Type : Many2one
 
 https://www.odoo.com/es_ES/forum/ayuda-1/question/beginner-question-about-functional-fields-and-property-fields-77398#answer_77401

______________________________________________________________________________________________________________________________________


