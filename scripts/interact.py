from brownie import A, B, C, Implementation, accounts


def interact_call():
    print("Deploying contract A...")
    contractA = A.deploy({"from": accounts[0]})
    print("Storing new number..")
    tx_store = contractA.storeNewNumber(5, {"from": accounts[0]})
    storedNumber = contractA.retrieve()
    print(f"Stored Number with contract A: {storedNumber}")

    print("Deploying contract B")
    contractB = B.deploy({"from": accounts[0]})
    print("Storing using contract B.")
    tx_store_with_b = contractB.callContractAStore(
        contractA.address, 890, {"from": accounts[0]}
    )
    print("Stored!")
    tx_store_with_b.wait(1)
    print(f"The new number stored is: {contractA.retrieve()}")


def interact_delegate_call():
    print("Deploying implementaion..")
    implementation = Implementation.deploy({"from": accounts[0]})
    print("Deploying contract C....")
    contract_c = C.deploy({"from": accounts[0]})
    print("delegating call to implementation...")
    tx_delegate_call = contract_c.storeNumber(
        implementation.address, 70, {"from": accounts[0]}
    )
    tx_delegate_call.wait(1)
    print(f"{contract_c.retrieveNumber()}")
    print(f"{tx_delegate_call.events['Stored']['sender']}")


def main():
    # interact_call()
    interact_delegate_call()
