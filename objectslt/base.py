import sys
import json
from objectpath import Tree

def usage(error_lvl):
    print("Usage:")
    print("    sys.argv[0] <content_file> <template_file> <out_file>")
    print("")
    sys.exit(error_lvl)

def walk(node, objpath):
    if isinstance(node, dict) or isinstance(node, list):
        for id, v in enumerate(node):
            if isinstance(node, dict):
                k = v
                v = node[k]
            else:
                k = id
                
            if isinstance(v, str):
                if v.startswith('OBJECTSLT:'):
                    _, ty, query = v.split(':', 2)
                    print(ty)
                    import pdb ; pdb.set_trace()
                    ty_class = __builtins__[ty]
                    newval = objpath.execute(query)
                    if isinstance(newval, ty_class):
                        node[k] = newval
                    else:
                        node[k] = ty_class(newval)
                else:
                    pass
                    # print(k)
                    # print(v)
            elif isinstance(v, dict) or isinstance(v, list):
                # print("Iter over [%s]" % k)
                walk(v, objpath)
            else:
                # print(k)
                # print(v)
                pass

def command():
    if len(sys.argv) != 4:
        usage(1)

    fin_name = sys.argv[1]
    tmpl_name = sys.argv[2]
    out_name = sys.argv[3]

    fin = open(fin_name, "r")
    fin_json = json.load(fin)
    fin_objpath = Tree(fin_json)

    tmpl = open(tmpl_name, "r")
    tmpl_json = json.load(tmpl)
    
    out = open(out_name + '.orig', "w")
    json.dump(tmpl_json, out, sort_keys=True, indent=4)

    walk(tmpl_json, fin_objpath)

    out = open(out_name, "w")
    json.dump(tmpl_json, out, sort_keys=True, indent=4)
