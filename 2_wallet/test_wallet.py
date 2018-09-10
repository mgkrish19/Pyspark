import pytest
from wallet import Wallet, InsufficientAmount

"""
fixture can help to setup some helper code that runs before any tests are executed
test functions that require fixtures should accept them as arguments.
For example, it can check whether a directory exists, it can delete previous database records
Or, more commonly, init test objects

each test is provided with a newly-initialized Wallet instance, not the one used in another test
good practice to add docstrings for fixtures
Run:   pytest --fixtures

3 potential scopes for fixture: 
1) session: run only once for several .py files => @pytest.fixture(scope = 'session')
2) module: run once for every .py file => @pytest.fixture(scope = 'test')
3) test: run once for every test => the default @pytest.fixture()

Fixture can also use fixture as well
"""

@pytest.fixture
def empty_wallet():
    ''' Returns a Wallet instance with 0 balance '''
    print ("Create empty wallet...")
    return Wallet()

@pytest.fixture
def wallet():
    ''' Returns a Wallet instance with a balance of 20 '''
    print ("Create wallet with $20 balance")
    return Wallet(20)

def test_default_initial_amount(empty_wallet):
    assert empty_wallet.balance == 0

def test_setting_initial_amount(wallet):
    assert wallet.balance == 20

def test_wallet_add_cash(wallet):
    wallet.add_cash(80)
    assert wallet.balance == 100

def test_wallet_spend_cash(wallet):
    wallet.spend_cash(10)
    assert wallet.balance == 10

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)


"""
parametrize can help to test various combinations of functions/methods
"""
@pytest.mark.parametrize('earned,spent,expected', 
    [
        (30, 10, 20), # each line is a test with a tuple of parameters to be sent to the following test_transactions function
        (20, 2, 18),
        (10, 5, 5),
    ]
)

def test_transactions(earned, spent, expected):
    my_wallet = Wallet()
    my_wallet.add_cash(earned)
    my_wallet.spend_cash(spent)
    assert my_wallet.balance == expected
