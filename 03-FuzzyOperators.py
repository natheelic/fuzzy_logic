import sys

def fuzzy_and(a, b):
    return min(a, b)

def fuzzy_or(a, b):
    return max(a, b)

def fuzzy_not(a):
    return 1 - a


def main():
    if len(sys.argv) > 2:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        print("Fuzzy AND:", fuzzy_and(a, b))
        print("Fuzzy OR:", fuzzy_or(a, b))
        print("Fuzzy NOT of a:", fuzzy_not(a))
        print("Fuzzy NOT of b:", fuzzy_not(b))
    else:
        print("Usage: python3 FuzzyOperators.py <a> <b>")
        print("Example: python3 FuzzyOperators.py 0.5 0.7")

if __name__ == "__main__":
    main()