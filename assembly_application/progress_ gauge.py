from SQL import MySQL_query

class gauge_calculator():

    def progress_gauge(self):  # 게이지 값 리턴하는 함수
        data = MySQL_query.get_item_count_for_gauge()

        count_new_product = data[0]['item_count']

        get_gauge = (count_new_product / 8640) * 100

        return get_gauge

    def count_product_today(self):  # 오늘 생산한 양품 갯수 리턴하는 함수
        data = MySQL_query.get_item_count_for_gauge()

        count_new_product = data[0]['item_count']

        return count_new_product
