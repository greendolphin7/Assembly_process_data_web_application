from SQL import MySQL_query
from product_master_table import product_master

EGRC_master = product_master.EGRC(1)
op10_WIP = product_master.op10_WIP(1)
op20_WIP = product_master.op20_WIP(1)
op30_WIP = product_master.op30_WIP(1)
op40_WIP = product_master.op40_WIP(1)
op50_WIP = product_master.op50_WIP(1)

body = product_master.body(1)
wavyfin = product_master.wavyfin(1)
pipe1 = product_master.pipe1(1)
pipe2 = product_master.pipe2(1)
flange1 = product_master.flange1(1)
flange2 = product_master.flange2(1)

MySQL_query.insert_product_master(EGRC_master)
MySQL_query.insert_product_master(op10_WIP)
MySQL_query.insert_product_master(op20_WIP)
MySQL_query.insert_product_master(op30_WIP)
MySQL_query.insert_product_master(op40_WIP)
MySQL_query.insert_product_master(op50_WIP)

MySQL_query.insert_product_master(body)
MySQL_query.insert_product_master(wavyfin)
MySQL_query.insert_product_master(pipe1)
MySQL_query.insert_product_master(pipe2)
MySQL_query.insert_product_master(flange1)
MySQL_query.insert_product_master(flange2)

