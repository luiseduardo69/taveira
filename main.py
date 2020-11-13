def printDecimal(n):
    print(n,'\t\t', end='')

def printBinario(n):
    print(bin(n), '\t', end='')

def printOctal(n):
    print(oct(n), '\t', end='')

def printHexadecimal(n):
    print(hex(n), '\t', '\n')

def imprimirTabela():
    n =0
    while n <256:
        printDecimal(n)
        printBinario(n)
        printOctal(n)
        printHexadecimal(n)
        n += 1


print("decimal binario octa hexa")
imprimirTabela()