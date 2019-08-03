def write(fname, tasks):
    with open(fname, "w") as fp:
        for x in tasks:
            fp.write("%s\n" % x)

def deleteContent(pfile):
    pfile.truncate()
    return pfile

def read(fname):
    tasks = []
    with open(fname, "r") as fp:
        t1 = fp.readlines()
        for x in t1:
            tasks.append(x.rstrip('\n'))
    return tasks