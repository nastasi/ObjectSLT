import sys
import json

def usage(error_lvl):
    print("Usage:")
    print("    sys.argv[0] <content_file> <template_file> <out_file>")
    print("")
    sys.exit(error_lvl)


def walk(node):
    if isinstance(node, dict) or isinstance(node, list):
        for id, v in enumerate(node):
            if isinstance(node, dict):
                k = v
                v = node[k]
            else:
                k = id
                
            if isinstance(v, str):
                if v.startswith('OBJECTSLT:'):
                    print('============ MANGLE %s' % k)
                else:
                    print(k)
                    print(v)
            elif isinstance(v, dict) or isinstance(v, list):
                print("Iter over [%s]" % k)
                walk(v)
            else:
                print(k)
                print(v)
                
def command():
    if len(sys.argv) != 4:
        usage(1)

    fin_name = sys.argv[1]
    tmpl_name = sys.argv[2]
    out_name = sys.argv[3]

    tmpl = open(tmpl_name, "r")
    tmpl_json = json.load(tmpl)
    
    walk(tmpl_json)

    out = open(out_file, "w")
    json.dump(tmpl_json, out)
