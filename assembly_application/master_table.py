class master_table:

    def master(self):
        p_code = ['EGRC', 'body', 'wavyfin', 'pipe1', 'pipe2', 'flange1', 'flange2',
                  'op10_WIP', 'op20_WIP', 'op30_WIP', 'op40_WIP', 'op50_WIP']  # 제품, 반제품, 부품 이름
        p_num = ['P01', 'WIP1', 'WIP2', 'WIP3', 'WIP4', 'WIP5',
                 'PART1', 'PART2', 'PART3', 'PART4', 'PART5', 'PART6']  # 제품 분류 (종류), 반제품 종류, 부품 종류,
        p_class = ['N01', 'N02', 'NO3']  # 제품 구분 (제품, 반제품, 부품)

        m_code = ['OP10', 'OP20', 'OP30', 'OP40', 'OP50', 'OP60']  # 설비 코드
        m_class = ['MCO1', 'MCO2', 'MCO3']  # 단순조립, 용접조립, 최종검사 machine class
        m_assembly = ['body_wavyfin', 'op10_pipe1', 'op20_pipe2', 'op30_flagne1', 'op40_flange2',
                      'final_test']  # 조립되는 역할 코드
        m_data_code = ['E01', 'T01', 'TEST']  # 전류, 온도, 테스트 코드
        m_process_time = ['exp10']  # 설비 작업시간 분포 코드

        p_quality = ['OK', 'NOK']  # 양품, 불량품 코드

        # 길이 목표 치수 코드, 너비랑 겹치는 부분이 있어서 중간에 l,w,h 추가
        p_target_l = ['body_l_200', 'wavyfin_l_100', 'pipe1_l_30', 'pipe2_l_30', 'flange1_l_30', 'flange2_l_30',
                      'op10_l_200', 'op20_l_200', 'op30_l_200', 'op40_l_230', 'op50_l_260', 'op60_l_260']
        p_target_w = ['body_w_100', 'wavyfin_w_50', 'pipe1_w_50', 'pipe2_w_50', 'flange1_w_80', 'flange2_w_80',
                      'op10_w_100', 'op20_w_140', 'op30_w_180', 'op40_w_180', 'op50_w_180', 'op60_w_180']
        p_target_h = ['body_h_50', 'wavyfin_h_60', 'pipe1_h_30', 'pipe2_h_30', 'flange1_h_40', 'flange2_h_40',
                      'op10_h_60', 'op20_h_60', 'op30_h_60', 'op40_h_60', 'op50_h_60', 'op60_h_60']

        return p_code, p_num, p_class, m_code, m_class, m_assembly, m_data_code, p_quality, p_target_l, p_target_w, p_target_h