#!/usr/bin/env python3

'''
version: 1.0
author: Phong

Script that accepts argparse to modify an existing inventory file by filtering it, and outputting it to a seperate inventory file
The expected format of an inventory file that can be parse through must be like the sample below

Usage:
python3 inv_filter.py --inv-file /path/to/inventoryfile --group-name=<custom name> <host1> <host2> 
Sample execution of this script
python3 inv_filter.py --inv-file MON_PILOT_A_inventory --group-name=EXCLUDE abc130 abc298

This will then create a file specified as --group-name=EXCLUDE with the following content:
abc130
abc298

Then modify  MON_PILOT_A_inventory to remove abc130 abc298
'''

import argparse

def filter_inventory(inventory_file, group_name, hosts):
    # Read the inventory file
    with open(inventory_file, 'r') as file:
        inventory = file.readlines()

    # Strip newline characters from each line
    inventory = [line.strip() for line in inventory]

    # Create a new inventory for the specified group
    group_inventory = []

    # Iterate through the specified hosts
    for host in hosts:
        for line in inventory:
            if host in line:
                # Remove the matching line from the original inventory
                inventory.remove(line)
                # Add the full matching line to the group inventory
                group_inventory.append(line)
                break

    # Write the updated original inventory back to the file
    with open(inventory_file, 'w') as file:
        file.write('\n'.join(inventory))

    # Write the group inventory to a new file
    #group_inventory_file = f"{group_name}_inventory"
    group_inventory_file = f"{group_name}"
    with open(group_inventory_file, 'w') as file:
        file.write('\n'.join(group_inventory))

    print(f"Inventory filtered successfully.")
    print(f"Original inventory updated: {inventory_file}")
    print(f"Group inventory created: {group_inventory_file}")

# Create an argument parser
parser = argparse.ArgumentParser(description='Filter inventory based on group and hosts')
parser.add_argument('--inv-file', type=str, required=True, help='Path to the inventory file')
parser.add_argument('--group-name', type=str, required=True, help='Name of the group')
parser.add_argument('hosts', type=str, nargs='+', help='Hosts to filter')

# Parse the command-line arguments
args = parser.parse_args()

# Call the filter_inventory function with the provided arguments
filter_inventory(args.inv_file, args.group_name, args.hosts)
