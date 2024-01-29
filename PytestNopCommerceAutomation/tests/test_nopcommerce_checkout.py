import logging

from configuration.config import TestData
from pages.checkout_page import CheckoutPage
from pages.product_detail_page import ProductPage
from tests.base_test import BaseTest
from pages.shopping_cart import ShoppingCart

logger = logging.getLogger()


class TestCheckout(BaseTest):

    def test_add_to_cart_product_and_checkout(self):
        print("in test add to cart function")

        product_details = ProductPage(self.driver)
        product_details.product_details_page(TestData.select_processor, TestData.select_ram, TestData.select_quantity)

        cart = ShoppingCart(self.driver)
        cart.shopping_cart_checkout(TestData.gift_wrapping_value)

        # checkout = CheckoutPage(self.driver)
        # checkout.fill_shipping_address(
        #     TestData.select_country,
        #     TestData.select_state,
        #     TestData.select_city,
        #     TestData.select_address1,
        #     TestData.select_postal_code,
        #     TestData.select_phone_no
        # )

        logger.info("Test example function executed correctly")
