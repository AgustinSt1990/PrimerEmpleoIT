def impares(pi, pf):
    return [i for i in range(pi, pf+1) if i%2 != 0]

if __name__ == '__main__':
    print (impares(1, 8))