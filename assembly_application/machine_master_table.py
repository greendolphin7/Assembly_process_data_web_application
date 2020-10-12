from SQL import MySQL_query

def machine_master():
    machine_master_data = []

    ### 10
    master_dict = {}

    machine_code = 'OP10'  # 설비 코드명
    machine_class = 'MCO1'  # 단순 조립
    machine_process_time = 'exp10'
    machine_assembly = 'body_wavyfin'
    machine_data_code = 'E01'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    ### 20
    master_dict = {}

    machine_code = 'OP20'  # 설비 코드명
    machine_class = 'MCO1'  # 단순 조립
    machine_process_time = 'exp10'
    machine_assembly = 'op10_pipe1'
    machine_data_code = 'E01'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    ### 30
    master_dict = {}

    machine_code = 'OP30'  # 설비 코드명
    machine_class = 'MCO1'  # 단순 조립
    machine_process_time = 'exp10'
    machine_assembly = 'op20_pipe2'
    machine_data_code = 'E01'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    ### 40
    master_dict = {}

    machine_code = 'OP40'  # 설비 코드명
    machine_class = 'MCO2'  # 용접 조립
    machine_process_time = 'exp10'
    machine_assembly = 'op30_flange1'
    machine_data_code = 'T01'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    ### 50
    master_dict = {}

    machine_code = 'OP50'  # 설비 코드명
    machine_class = 'MCO2'  # 용접 조립
    machine_process_time = 'exp10'
    machine_assembly = 'op40_flange2'
    machine_data_code = 'T01'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    ### 60
    master_dict = {}

    machine_code = 'OP60'  # 설비 코드명
    machine_class = 'MCO3'  # 최종 검사
    machine_process_time = 'exp10'
    machine_assembly = 'final_test'
    machine_data_code = 'TEST'

    master_dict['machine_code'] = machine_code  # PK
    master_dict['machine_class'] = machine_class
    master_dict['machine_process_time'] = machine_process_time
    master_dict['machine_assembly'] = machine_assembly
    master_dict['machine_data_code'] = machine_data_code

    machine_master_data.append(master_dict)

    MySQL_query.insert_machine_master(machine_master_data)

    return machine_master_data
