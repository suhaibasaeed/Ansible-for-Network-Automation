#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
# Is the Netmiko module found
netmiko_found = False
try: # Exit gracefully if module not found
    from netmiko import ConnectHandler

    netmiko_found = True
except ImportError:
    pass

def main():
    # Define your module arguments
    module_args = dict(
        host=dict(type="str", required=True),
        device_type=dict(type="str", required=True),
        username=dict(type="str", required=False),
        # So password isn't leaked
        password=dict(type="str", required=False, no_log=True),
        config_list=dict(type="list", required=True),
    )

    # Create an instance of AnsibleModule class
    module = AnsibleModule(argument_spec=module_args)
    result = dict(changed=False, msg="") # Default result

    if not netmiko_found: # Ensure Netmiko installed; exit using JSON (if not).
        module.fail_json(msg="The Netmiko library is not installed!")

    # Extract the arguments using params attribute
    host = module.params["host"]
    device_type = module.params["device_type"]
    username = module.params["username"]
    password = module.params["password"]
    config_list = module.params["config_list"]
    # Create ConnectHandler object and pass in args
    net_connect = ConnectHandler(
        host=host, device_type=device_type, username=username, password=password
    )
    output = net_connect.send_config_set(config_list)
    
    # Check if command actually sent to the device
    if 'cisco1' in output:
        result["changed"] = True
    
    result["output"] = output # Add output to result dict
    module.exit_json(**result)

if __name__ == "__main__":
    main()
