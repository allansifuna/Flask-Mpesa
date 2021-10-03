import pytest
from .base import mp


@pytest.mark.usefixtures("mock_fixture_test_auth")
def test_auth(auth):
    auth = mp.C2B.authenticate()
    assert auth is not None


@pytest.mark.usefixtures("mock_fixture_test_b2c")
def test_b2c(b2c):
    data = {"initiator_name": "testapi364",
            "security_credential": "TziD/ydlT52Fm6SOH1ebrzUFwy3cP6OGplsrWja+X/1roQy2AzMsj5QGuqu9O+IFR1E6l16Jm87tg4bhnxoIhAufCEWusQI1wJZ6YLzpN0cHZAY/8SN1JfHdgEkrmksAY14pejHyfntyLT9Sg51kBjaj6J7/2+gHl2e64klnJAhlfPJWxC18zwEzsg58zFmypcovPPB6MHkPLyHQNFbu4oXC0e2gkZrIAWXTNN7PpYt4m/w39s5txU7/6P7hTzXgYAgqk4kxfPBIBeEmKhH5tSGxMD+xnSpZIXLovFgopexq8S76pmdLMjr2CdR60GlwXnAPnKJ5U9CIxRRewuoksQ==",
            "amount": "1000",
            "command_id": "SalaryPayment",
            "party_a": "600977",
            "party_b": "254708374149",
            "remarks": "Just a Transaction",
            "queue_timeout_url": "https://testurl.com/b2b-timeout",
            "result_url": "https://testurl.com/b2b-result",
            "occassion": "Test123"
            }
    resp = mp.B2C.transact(**data)
    assert dict(resp).keys() == b2c.keys()


@pytest.mark.usefixtures("mock_fixture_test_express_sim")
def test_express_sim(express_sim):
    data = {
        "business_shortcode": 174379,
        "passcode": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
        "amount": "1",
        "phone_number": "254713812939",
        "callback_url": "https://testurl.com/b2b-result",
        "reference_code": "DSC",
        "description": "first test"
    }
    resp = mp.MpesaExpress.stk_push(**data)
    assert dict(resp).keys() == express_sim.keys()


@pytest.mark.usefixtures("mock_fixture_test_express_query")
def test_express_query(express_query):
    data = {
        "business_shortcode": 174379,
        "passcode": "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919",
        "checkout_request_id": "ws_CO_021020210904344355"
    }
    resp = mp.MpesaExpress.query(**data)
    assert dict(resp).keys() == express_query.keys()


@pytest.mark.usefixtures("mock_fixture_test_c2b_reg")
def test_c2b_reg(c2b_reg):
    data = {"shortcode": "600364",
            "response_type": "Completed",
            "confirmation_url": "https://testurl.com/confirmation",
            "validation_url": "https://testurl.com/validation"
            }
    resp = mp.C2B.register(**data)
    assert dict(resp).keys() == c2b_reg.keys()


@pytest.mark.usefixtures("mock_fixture_test_c2b_sim")
def test_c2b_sim(c2b_sim):
    data = {"shortcode": "600364",
            "command_id": "CustomerPayBillOnline",
            "amount": "123",
            "msisdn": "254708374149",
            "bill_ref_number": "account"
            }
    resp = mp.C2B.simulate(**data)
    assert dict(resp).keys() == c2b_sim.keys()


@pytest.mark.usefixtures("mock_fixture_test_bal")
def test_bal(bal):
    data = {"initiator": "testapi364",
            "security_credential": "TziD/ydlT52Fm6SOH1ebrzUFwy3cP6OGplsrWja+X/1roQy2AzMsj5QGuqu9O+IFR1E6l16Jm87tg4bhnxoIhAufCEWusQI1wJZ6YLzpN0cHZAY/8SN1JfHdgEkrmksAY14pejHyfntyLT9Sg51kBjaj6J7/2+gHl2e64klnJAhlfPJWxC18zwEzsg58zFmypcovPPB6MHkPLyHQNFbu4oXC0e2gkZrIAWXTNN7PpYt4m/w39s5txU7/6P7hTzXgYAgqk4kxfPBIBeEmKhH5tSGxMD+xnSpZIXLovFgopexq8S76pmdLMjr2CdR60GlwXnAPnKJ5U9CIxRRewuoksQ==",
            "command_id": "AccountBalance",
            "party_a": "600364",
            "identifier_type": "4",
            "remarks": "Just a Transaction",
            "queue_timeout_url": "https://testurl.com/b2b-timeout",
            "result_url": "https://testurl.com/b2b-result"
            }
    resp = mp.Balance.get_balance(**data)
    assert dict(resp).keys() == bal.keys()


@pytest.mark.usefixtures("mock_fixture_test_t_status")
def test_t_status(t_status):
    data = {"initiator": "testapi364",
            "transaction_id": "PJ251HK6YH",
            "party_a": "600364",
            "security_credential": "TziD/ydlT52Fm6SOH1ebrzUFwy3cP6OGplsrWja+X/1roQy2AzMsj5QGuqu9O+IFR1E6l16Jm87tg4bhnxoIhAufCEWusQI1wJZ6YLzpN0cHZAY/8SN1JfHdgEkrmksAY14pejHyfntyLT9Sg51kBjaj6J7/2+gHl2e64klnJAhlfPJWxC18zwEzsg58zFmypcovPPB6MHkPLyHQNFbu4oXC0e2gkZrIAWXTNN7PpYt4m/w39s5txU7/6P7hTzXgYAgqk4kxfPBIBeEmKhH5tSGxMD+xnSpZIXLovFgopexq8S76pmdLMjr2CdR60GlwXnAPnKJ5U9CIxRRewuoksQ==",
            "identifier_type": "4",
            "remarks": "Enterance Fee",
            "queue_timeout_url": "https://3e61-197-156-137-143.ngrok.io/b2b-timeout",
            "result_url": "https://3e61-197-156-137-143.ngrok.io/b2b-result",
            "occassion": "DSC-party_a"
            }
    resp = mp.TransactionStatus.check_transaction_status(**data)
    assert dict(resp).keys() == t_status.keys()


@pytest.mark.usefixtures("mock_fixture_test_b2b")
def test_b2b(b2b):
    data = {"initiator": "testapi364",
            "security_credential": "TziD/ydlT52Fm6SOH1ebrzUFwy3cP6OGplsrWja+X/1roQy2AzMsj5QGuqu9O+IFR1E6l16Jm87tg4bhnxoIhAufCEWusQI1wJZ6YLzpN0cHZAY/8SN1JfHdgEkrmksAY14pejHyfntyLT9Sg51kBjaj6J7/2+gHl2e64klnJAhlfPJWxC18zwEzsg58zFmypcovPPB6MHkPLyHQNFbu4oXC0e2gkZrIAWXTNN7PpYt4m/w39s5txU7/6P7hTzXgYAgqk4kxfPBIBeEmKhH5tSGxMD+xnSpZIXLovFgopexq8S76pmdLMjr2CdR60GlwXnAPnKJ5U9CIxRRewuoksQ==",
            "amount": "100",
            "command_id": "BusinessPayBill",
            "sender_identifier_type": "4",
            "receiver_identifier_type": "4",
            "party_a": "600364",
            "party_b": "600000",
            "remarks": "Enterance Fee",
            "queue_timeout_url": "https://4ca0-197-156-137-168.ngrok.io/b2b-timeout",
            "result_url": "https://4ca0-197-156-137-168.ngrok.io/b2b-result",
            "account_reference": "DSC-party_a"
            }
    resp = mp.B2B.transact(**data)
    assert dict(resp).keys() == b2b.keys()
