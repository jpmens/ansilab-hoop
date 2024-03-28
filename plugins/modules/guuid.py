DOCUMENTATION = r'''
---
module: guuid
short_description: Generate a UUID and store in it in a file
version_added: "1.0.0"
description:
   This generates a version 4 UUID and stores it in the specified path,
   optionally converting letters to upper case. The module fails if an
   existing file does not contain a valid version 4 UUID.
options:
    path:
        description: The path to the file which will contain the UUID.
        required: true
        type: path
    upper:
        description:
            - Control whether letters in UUID are to be uppercased
        required: false
        default: false
        type: bool
'''

from ansible.module_utils.basic import AnsibleModule
import uuid, re, os

def main():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(type='path', required=True),
            upper = dict(type='bool', default=False),
        ),
        supports_check_mode = True
    )

    changed = False
    path = module.params["path"]
    upper = module.params["upper"]
    try:
        if os.path.exists(path):
            u = open(path).read().rstrip()
            try:
                uuid.UUID(u, version=4)
            except ValueError:
                module.fail_json(dict(msg="File has invalid v4 UUID"))
        else:
            u = str(uuid.uuid4())
            changed = True

        if upper and re.search(r'[a-z]', u):
            u = u.upper()
            changed = True
        if not upper and re.search(r'[A-Z]', u):
            u = u.lower()
            changed = True

        if module.check_mode:
            module.exit_json(changed=changed)

        if changed:
            with open(path, "w") as f:
                f.write(f"{u}\n")
    except Exception as e:
        msg = "Cannot access {0}: {1}".format(path, e)
        module.fail_json(dict(msg=msg))

    result = dict(changed=changed, uuid=u, upper=upper)
    module.exit_json(**result)

if __name__ == '__main__':
    main()
