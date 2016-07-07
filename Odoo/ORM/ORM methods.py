1.browse :"Fetch records as objects " (SELECT)	
browse(cr, uid, ids, context=None, list_class=None, fields_process=None)
2.check_access_rule :"Verifies that the operation given by operation is allowed for the user according to ir.rules.
3.copy:"Duplicate record with given id updating it with default values ----id of the record to copy
4.copy_data  :"Copy given record's data with all its fields values"00
5.create :"Create new record with specified value" (INSERT )
create(cr, uid, vals, context=None)
6.default_get :"Returns default values for the fields in fields_list."
7.export_data :"Export fields for selected objects"
8.fields_get :"Get the description of list of fields"
9.fields_view_get :"Get the detailed composition of the requested view like fields, model, view architecture"
10.get_xml_id :"Find out the XML ID of any database record, if there is one."
11.import_data :"Import given data in given module"
12.name_get :"tuples with the text representation of requested objects for to-many relationships"
13.name_search :"Search for records and their display names according to a search domain."
14.perm_read:"Returns some metadata about the given records.--list of ownership dictionaries for each requested record"
15.write :"Update records with given ids with the given field values--True" (UPDATE)
(cr, uid, ids, vals, context=None)

16.view_init :"Override this method to do specific things when a view on the object is opened."
17.unlink :"Delete records with given ids--True"(DELETE )
 unlink(cr, uid, ids, context=None)
18.search :"Search for records based on a search domain.-id or list of ids of records matching the criteria--integer or list of integers"
19.read_group :"Get the list of records in list view grouped by the given groupby fields--list of dictionaries(one dictionary for each record) containing:

cr -- database cursor
user (integer)-- current user id
ids -- object id or list of object ids 
vals (dictionary) -- field values for new record, e.g {'field_name': field_value, ...}
context (dictionary) -- optional context arguments,like lang, time zone e.g. {'lang': 'en_us', 'tz': 'UTC', ...}


CRUD =create ( CREATE)   browse(Read/Select)  write( UPDATE) unlink ( DELETE )
create(cr, uid, vals, context=None)
	def create(self, cr, uid, vals, context=None):

self.browse(cr, uid, ids, context=None, list_class=None, fields_process=None)
write(cr, uid, ids, vals, context=None)
unlink(cr, uid, ids, context=None)
search(cr,uid,[('active','=',True),('image','!=',False)])
