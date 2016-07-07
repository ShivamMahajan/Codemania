sudo su - postgres Switching to postgres User
psql 
\l ( listing all the database)
\c  (connecting to the database)
\q quitting  or q

createuser --createdb --username postgres --no-createrole --no-superuser --pwprompt odoo

pg_restore -C -d postgres /home/shivamm/Downloads/TimesheetAnalysis.dump 




sudo apt-get install python-setup tools : for installing python libararies

sudo python setup.py install

openerp-server --addons-path= ,   --xmlrpc-port=8040  :::::for starting the odoo.py

sudo apt-get install node-clean-css
sudo apt-get install node-less
