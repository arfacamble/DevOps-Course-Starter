# Provisioning the app with ansible

1. Copy the contents of the ansible folder into the users host directory on a VM that will be the control node.
1. Update the inventory if necessary with the managed nodes which will provision the app
1. Run the plabook with the command `ansible-playbook playbook.yml -i inventory.yml`
    - add the `-v` verbose flag if there are any problems