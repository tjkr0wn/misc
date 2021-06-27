#!/usr/bin/python3
import sys
import linecache

dump_file_handle = None

def file_len(h):
    for i, l in enumerate(h):
            pass
    return i + 1

def writeout(s):
    if dump_file_handle is None:
        pass

def parse_line(l):
    if "pac" not in l:
        return

    pacs = list()
    class_names = list()
    addresses = list()
    func_names = list()

    class_name_b = None
    class_name = str()
    func_name = str()

    i = l.find("pac=")
    if i != -1:
            pac = hex(int(l[i+4:i+10], 0))
            pacs.append(pac)
            class_name_b = [i+11, None]

    i = l.find("::")
    if i != -1:
        class_name_b[1] = i
        for x in range(class_name_b[0], class_name_b[1]):
            class_name += l[x]
        class_names.append(class_name)

    i = l.find(")")
    if i != -1:
        for x in range(class_name_b[1]+2, i):
            func_name += l[x]
        func_name += ")"
        func_names.append(func_name)

    i = l.find("func=")
    if i != -1:
        addr = hex(int(l[i+5:i+24], 0))
        addresses.append(addr)

    print("pac: {}, class name: {}, function address: {}, function: {}".format(pac, class_name, addr, func_name))
    return (pacs, class_names, func_names, addresses)

def main(kinfo):
    handles = list()
    for i in kinfo:
        handles.append(open(i, "r"))

    for l in range(0, file_len(handles[0])):
        base_info = parse_line(linecache.getline(kinfo[0], l))

    for z in range(0, file_len(handles[1])):
        strip_info = parse_line(linecache.getline(kinfo[1], z))

    #TODO: Check for matching properties and writeout

if __name__ == '__main__':
    try:
        kinfo = (sys.argv[1], sys.argv[2])
    except:
        quit("Usage: python3 parse_iometa_kext_info.py iometa_symbolized_output.tx iometa_stripped_output.txt")
    main(kinfo)
