import pytest
from brownie import accounts, network, A, B, C, Implementation


def test_delegate_call():
    if network.show_active() != "development":
        pytest.skip()
    NUMBER = 420
    print("Deploying implementaion..")
    implementation = Implementation.deploy({"from": accounts[0]})
    print("Deploying contract C....")
    contract_c = C.deploy({"from": accounts[0]})
    print("delegating call to implementation...")
    tx_delegate_call = contract_c.storeNumber(implementation.address, NUMBER)
    tx_delegate_call.wait(1)

    STORED_NUMBER = contract_c.retrieveNumber()
    MSG_SENDER = tx_delegate_call.events["Stored"]["sender"]
    assert STORED_NUMBER == NUMBER
    # the msg.sender was preserved?
    assert MSG_SENDER == accounts[0].address
    # you bet sure it was
