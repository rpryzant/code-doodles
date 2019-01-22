


def flatten(d):
   if d is None or type(d) != type({}):
      return None # bad!
   out = {}
   for key in d.keys():
      if type(d[key]) != type({}):
         out[key] = d[key]
      else:
         fl_sub_d = flatten(d[key])
         for fl_key in fl_sub_d:
            out["%s.%s" % (key, fl_key)] = fl_sub_d[fl_key] 
   return out





test = {
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


print flatten(test)
