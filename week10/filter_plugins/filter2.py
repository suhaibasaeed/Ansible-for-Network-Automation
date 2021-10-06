import re

def arista_arp(arp_string):
    show_arp_list = []
    arp_string = arp_string.strip()
    
    for i in arp_string.splitlines():
        # Match on header and skip loop iteration if found
        if re.search(r"^Address.*Interface$", i, flags=re.M):
            continue
        # Append mac address to output which is 3rd element in list
        show_arp_list.append(i.split()[2])
    # Return list of lists
    return show_arp_list

# Boilerplate Class and method
class FilterModule(object):
    def filters(self):

        return {"aristaarp": arista_arp}