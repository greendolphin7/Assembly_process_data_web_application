from SQL import MySQL_query
from machine_master_table import machine_master

op10 = machine_master.op10(1)
op20 = machine_master.op20(1)
op30 = machine_master.op30(1)
op40 = machine_master.op40(1)
op50 = machine_master.op50(1)
op60 = machine_master.op60(1)

MySQL_query.insert_machine_master(op10)
MySQL_query.insert_machine_master(op20)
MySQL_query.insert_machine_master(op30)
MySQL_query.insert_machine_master(op40)
MySQL_query.insert_machine_master(op50)
MySQL_query.insert_machine_master(op60)
