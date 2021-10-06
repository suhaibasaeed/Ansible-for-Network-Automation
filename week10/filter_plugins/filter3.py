import re

def cisco_arp(arp_string):
    # Initalise list and dict
    show_arp_list = []
    show_arp_dict = {}
    # Strip whitespace from command output
    arp_string = arp_string.strip()
    # Loop through string
    for i in arp_string.splitlines():
        # Match on header and skip loop iteration if found
        if re.search(r"^Protocol.*Interface$", i, flags=re.M):
            continue
        
        # Unpack list and extract ip addr and mac addr
        _, ip_addr, _, mac, _, _ = i.split()
        # Add extract info as key value pairs
        show_arp_dict.update({ip_addr: mac})
        
    # Return dictionary
    return show_arp_dict
    

# Boilerplate Class and method
class FilterModule(object):
    def filters(self):

        return {"ciscoarp": cisco_arp}