"""
i like this better =)

"""
def flatten(d):
    assert isinstance(d, dict)

    out = {}
    for k, v in d.iteritems():
        if isinstance(v, dict):
            for suffix, flat_val in flatten(v).items():
                out['%s.%s' % (k, suffix)] = flat_val
        else:
            out[k] = v
    return out



d = {
  'Key1': '1',
  'Key2': {
    'a' : '2',
    'b' : '3',
    'c' : {
      'd' : '3',
      'e' : '1'
      }
    }
}

print flatten(d)
