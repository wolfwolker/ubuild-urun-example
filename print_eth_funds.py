from prettytable import PrettyTable
from web3 import Web3
import os

# Connect to an Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/your-project-id'))

# Ethereum address to check
address = os.environ.get('ETH_WALLET')

# Get the balance of the address in wei
balance_wei = w3.eth.get_balance(address)

# Convert the balance to ether
balance_eth = w3.fromWei(balance_wei, 'ether')

# Print the balance

# Create a table to display the balance
table = PrettyTable()
table.field_names = ["Address", "Balance (ETH)"]
table.add_row([address, balance_eth])

# Print the table
print(table)
