from time import sleep

import allure

from pageObject.flow_page.flow_page import FlowPage
from pageObject.flow_page.search_page import SearchPage


@allure.feature('结算中心')
class TestFlow:

    @allure.story('结算中心没有商品下单场景')
    def test_purchase_failure(self, login_driver):
        flow_page = FlowPage(login_driver)
        flow_page.flow_failed()
        assert flow_page.current_url == 'http://localhost/ecshop/flow.php?step=checkout'
        sleep(1)

    @allure.story('通过结算中心成功下单')
    def test_purchase_success(self, login_driver):
        # 先将商品加入购物车
        search_page = SearchPage(login_driver)
        search_page.add_cart()
        # 去结算中心提交订单
        flow_page = FlowPage(login_driver)
        flow_page.flow_success()
        assert flow_page.current_url == 'http://localhost/ecshop/flow.php?step=done'
        sleep(1)
