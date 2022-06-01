import pytest
from brownie import accounts, network, A, B, C, Implementation


def test_store_number():
    if network.show_active() != "development":
        pytest.skip()
    NUMBER = 890
    print("Deploying contract A...")
    contractA = A.deploy({"from": accounts[0]})
    print("Storing new number..")
    tx_store = contractA.storeNewNumber(NUMBER, {"from": accounts[0]})
    tx_store.wait(1)
    STORED_NUMBER = contractA.retrieve()
    assert STORED_NUMBER == NUMBER


def test_store_number_with_call():
    if network.show_active() != "development":
        pytest.skip()
    NUMBER = 134
    print("Deploying contract A...")
    contractA = A.deploy({"from": accounts[0]})
    print("Deploying contract B")
    contractB = B.deploy({"from": accounts[0]})
    print("Storing using contract B.")
    tx_store_with_b = contractB.callContractAStore(
        contractA.address, NUMBER, {"from": accounts[0]}
    )
    print("Stored!")
    STORED_NUMBER = contractA.retrieve()
    MSG_SENDER = tx_store_with_b.events["Stored"]["sender"]
    assert STORED_NUMBER == NUMBER
    # the msg.sender was preserved?
    assert MSG_SENDER == contractB.address
    # nah the contract that called it was the msg.sender
