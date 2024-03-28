DOCUMENTATION = r'''
  name: rot13
  version_added: "1.0.2"
  short_description: encode/decode to ROT13
  description:
    - Encode or decode a string to ROT13
  positional: _input, query
  options:
    _input:
      description: String to encode or decode.
      type: str
      required: true
'''

EXAMPLES = r'''

    encoded: '{{ "Ansible" | rot13 }}'
    # => "Nafvoyr"

    decoded: '{{ "Nafvoyr" | rot13 }}'
    # => "Ansible"
'''

RETURN = r'''
  _value:
    description:
      - A string with encoded or decoded ROT13 content
    type: string
'''
import codecs

# ROT13 of string `s' 
def rot13(s):
    return codecs.encode(s, 'rot_13')

class FilterModule(object):

    def filters(self):
        return {
            'rot13'     : rot13,
        }
