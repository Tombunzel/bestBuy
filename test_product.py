import pytest
import products


def test_instantiate_product():
    assert isinstance(products.Product("product1", 1000, 100), products.Product)


def test_instantiate_product_invalid_details():
    with pytest.raises(ValueError):
        products.Product("", 1500, 100)


def test_product_deactivates():
    product = products.Product("product2", 1500, 100)
    product.buy(100)
    assert not product.is_active()


def test_buy_modifies_quantity():
    product = products.Product("product2", 1500, 100)
    product.buy(50)
    assert product.quantity == 50


def test_buy_too_much():
    product = products.Product("product2", 1500, 100)
    with pytest.raises(ValueError):
        product.buy(101)


pytest.main()

