import sys


def triangular_membership(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    if x == b:
        return 1.0
    if x < b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)


def left_shoulder_membership(x, a, b):
    if x <= a:
        return 1.0
    if x >= b:
        return 0.0
    return (b - x) / (b - a)


def right_shoulder_membership(x, a, b):
    if x <= a:
        return 0.0
    if x >= b:
        return 1.0
    return (x - a) / (b - a)


def main():

    cool = [0, 0, 20]
    warm = [10, 20, 30]
    hot = [20, 40, 40]

    if len(sys.argv) > 1:
        try:
            x = float(sys.argv[1])
        except ValueError:
            print("Usage: python3 MemberFunc.py <x>")
            print("Example: python3 MemberFunc.py 28")
            return
    else:
        x = 30

    u_cool = left_shoulder_membership(x, cool[0], cool[2])
    u_warm = triangular_membership(x, warm[0], warm[1], warm[2])
    u_hot = right_shoulder_membership(x, hot[0], hot[1])

    print("Membership degree of cool:", u_cool)
    print("Membership degree of warm:", u_warm)
    print("Membership degree of hot:", u_hot)

if __name__ == "__main__":
    main()