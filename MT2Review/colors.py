def colors(flags):
    newD = {}
    for k,v in flags.items():
        for i in v:
            if i not in newD:
                newD[i] = [k]
            else:
                newD[i].append(k)
    return newD

if __name__ == '__main__':
    flags = {
        "dominica":['gold','white','black','red','green'],
        "st. Lucia":['gold','white','black', 'blue'],
        "estonia":['white','black','blue']
    }
    print(colors(flags))
