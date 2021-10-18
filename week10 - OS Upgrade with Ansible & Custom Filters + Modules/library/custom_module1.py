#!/usr/bin/python

# Import Ansible module class

from ansible.module_utils.basic import AnsibleModule

def main():
    # Module arguments - Has one called my string which is required
    module_args = {
        "my_string": {"required": True, "type": "str"}
    }

    # Create instance of class
    module = AnsibleModule(argument_spec=module_args)

    # Define standard results
    result = {"changed": False, "output": ""}

    # Extract module argument using params attribute
    string_upper = module.params["my_string"]
    
    # Add key to result dict
    result["output"] = string_upper.upper()

    module.exit_json(**result)

if __name__ == "__main__":
    main()

