import pytest
from flask_mpesa.tests.data import AUTH, B2C, EXPRESS_SIM, EXPRESS_QUERY, C2B_REG, C2B_SIM, BAL, TRANSACTION_STATUS, B2B

base_url = "https://sandbox.safaricom.co.ke"


@pytest.fixture()
def auth():
    return AUTH


@pytest.fixture()
def b2c():
    return B2C


@pytest.fixture()
def express_sim():
    return EXPRESS_SIM


@pytest.fixture()
def express_query():
    return EXPRESS_QUERY


@pytest.fixture()
def c2b_reg():
    return C2B_REG


@pytest.fixture()
def c2b_sim():
    return C2B_SIM


@pytest.fixture()
def bal():
    return BAL


@pytest.fixture()
def t_status():
    return TRANSACTION_STATUS


@pytest.fixture()
def b2b():
    return B2B


@pytest.fixture(name="mock_fixture_test_auth")
def fixture_mock_test_auth(requests_mock):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)


@pytest.fixture(name="mock_fixture_test_b2c")
def fixture_mock_test_b2c(requests_mock, b2c):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/b2c/v1/paymentrequest"
    requests_mock.post(url, json=b2c)


@pytest.fixture(name="mock_fixture_test_express_sim")
def fixture_mock_test_express_sim(requests_mock, express_sim):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/stkpush/v1/processrequest"
    requests_mock.post(url, json=express_sim)


@pytest.fixture(name="mock_fixture_test_express_query")
def fixture_mock_test_express_query(requests_mock, express_query):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/stkpushquery/v1/query"
    requests_mock.post(url, json=express_query)


@pytest.fixture(name="mock_fixture_test_c2b_reg")
def fixture_mock_test_c2b_reg(requests_mock, c2b_reg):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/c2b/v1/registerurl"
    requests_mock.post(url, json=c2b_reg)


@pytest.fixture(name="mock_fixture_test_c2b_sim")
def fixture_mock_test_c2b_sim(requests_mock, c2b_sim):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/c2b/v1/simulate"
    requests_mock.post(url, json=c2b_sim)


@pytest.fixture(name="mock_fixture_test_bal")
def fixture_mock_test_bal(requests_mock, bal):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/accountbalance/v1/query"
    requests_mock.post(url, json=bal)


@pytest.fixture(name="mock_fixture_test_t_status")
def fixture_mock_test_t_status(requests_mock, t_status):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/transactionstatus/v1/query"
    requests_mock.post(url, json=t_status)


@pytest.fixture(name="mock_fixture_test_b2b")
def fixture_mock_test_b2b(requests_mock, b2b):
    url = base_url + "/oauth/v1/generate?grant_type=client_credentials"
    requests_mock.get(url, json=AUTH)
    url = base_url + "/mpesa/b2b/v1/paymentrequest"
    requests_mock.post(url, json=b2b)
