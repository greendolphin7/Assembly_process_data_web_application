from SQL import MySQL_query

class OEE_cal():

    def Availability_Calculator(self):

        data = MySQL_query.get_time_for_availability(1)

        op10_makespan = 1  # 0으로 나누는거 방지
        op20_makespan = 1
        op30_makespan = 1
        op40_makespan = 1
        op50_makespan = 1
        op60_makespan = 1

        op10_count = 0
        op20_count = 0
        op30_count = 0
        op40_count = 0
        op50_count = 0
        op60_count = 0

        for row in range(len(data)):

            if data[row]['machine_code'] == 'OP10':
                op10_makespan = op10_makespan + data[row]['process_time']
                op10_count = op10_count + 1

            elif data[row]['machine_code'] == 'OP20':
                op20_makespan = op20_makespan + data[row]['process_time']
                op20_count = op20_count + 1

            elif data[row]['machine_code'] == 'OP30':
                op30_makespan = op30_makespan + data[row]['process_time']
                op30_count = op30_count + 1

            elif data[row]['machine_code'] == 'OP40':
                op40_makespan = op40_makespan + data[row]['process_time']
                op40_count = op40_count + 1

            elif data[row]['machine_code'] == 'OP50':
                op50_makespan = op50_makespan + data[row]['process_time']
                op50_count = op50_count + 1

            else:
                op60_makespan = op60_makespan + data[row]['process_time']
                op60_count = op60_count + 1

            op10_idle_time = op10_count * 10 - op10_makespan
            op20_idle_time = op20_count * 10 - op20_makespan
            op30_idle_time = op30_count * 10 - op30_makespan
            op40_idle_time = op40_count * 10 - op40_makespan
            op50_idle_time = op50_count * 10 - op50_makespan
            op60_idle_time = op60_count * 10 - op60_makespan

            op10_availability = (op10_makespan - op10_idle_time) / 86400 * 100
            op20_availability = (op20_makespan - op20_idle_time) / 86400 * 100
            op30_availability = (op30_makespan - op30_idle_time) / 86400 * 100
            op40_availability = (op40_makespan - op40_idle_time) / 86400 * 100
            op50_availability = (op50_makespan - op50_idle_time) / 86400 * 100
            op60_availability = (op60_makespan - op60_idle_time) / 86400 * 100

            total_availability = (op10_availability + op20_availability + op30_availability
                                  + op40_availability + op50_availability + op60_availability) / 6

            total_availability = round(total_availability, 1)

        return total_availability

    def Productivity_Calculator(self):

        data = MySQL_query.get_item_count_for_productivity(1)

        total_productivity = (data[0]['total_item_count'] / 8640) * 100

        total_productivity = round(total_productivity, 1)

        return total_productivity

    def Quality_Calculator(self):

        data = MySQL_query.get_item_count_for_quality(1)

        OK_count = data[0]['item_count']

        NOK_count = data[1]['item_count']

        if OK_count < NOK_count:
            temp = OK_count
            OK_count = NOK_count
            NOK_count = temp

        quality = OK_count / (OK_count + NOK_count) * 100

        quality = round(quality, 1)

        return quality
