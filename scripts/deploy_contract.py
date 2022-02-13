import time
from brownie import RandomNumberGen, accounts, config, network

from scripts.helpful_scripts import fund_with_link, get_account


def main():
    deploy_contract()


def deploy_contract():
    account = get_account()
    fee = 0.1 * 10 ** 18
    contract = RandomNumberGen.deploy(
        config["networks"][network.show_active()]["vrf_coordinator"],
        config["networks"][network.show_active()]["link"],
        config["networks"][network.show_active()]["key_hash"],
        fee,
        {"from": account},
    )
    fund_with_link(contract.address)
    tx1 = contract.getRandomness({"from": account})
    tx1.wait(1)
    time.sleep(200)
    print(f"The random number is {contract.randomNumber()}")
    print(f"The dice rolled is {contract.rollDice()}")
