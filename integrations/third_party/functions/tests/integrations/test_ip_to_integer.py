from sqlite3.dbapi2 import paramstyle

import pytest

# from ....functions.actions.IpToInteger import IpToInteger
from ...actions.IpToInteger import IpToInteger
from ..core.product import Product
from ..core.session import MockSession
from integration_testing.set_meta import set_metadata

import pytest

@set_metadata
def test_ip_to_integer_success():
    product = Product()
    session = MockSession()

    ip_address = "192.168.0.1"
    expected_result = 3232235521

    product.set_input_data({"ip": ip_address})
    IpToInteger().run(product=product, session=session)

    results = session.action_output.results
    assert len(results) == 1
    assert results[0]["integer"] == expected_result
