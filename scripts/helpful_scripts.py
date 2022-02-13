from brownie import Contract, accounts, network, config, LinkToken


def get_account():
    if network.show_active() == "development":
        account = accounts[0]
    else:
        account = accounts.add(config["wallets"]["from_key"])
    return account


def fund_with_link(contract_address):
    account = get_account()
    link = Contract.from_abi(
        LinkToken._name,
        config["networks"][network.show_active()]["link"],
        LinkToken.abi,
    )
    amount = 0.1 * 10 ** 18
    tx = link.transfer(contract_address, amount, {"from": account})
    tx.wait(1)
    print("Contract funded with link successfully")
    return tx
