import fantasywords.markov as fw

def main(args):
    RAWINPUT = [i for i in fw.getInput()]
    INPUT = [i for i in fw.getInput()]
    print(len(INPUT))
    for i in range(int(args[1])):
        name = fw.gen(INPUT, 2)
        INPUT.append(name)
        print(name)
        INPUT = INPUT[-len(RAWINPUT):]
    print(repr(sorted([i for i in INPUT if i not in RAWINPUT])).replace(", ", "\n"))
    print(repr(sorted([i for i in INPUT if i in RAWINPUT])).replace(", ", "\n"))
    print(len(INPUT))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
