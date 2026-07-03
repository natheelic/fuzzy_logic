import sys

# This code defines membership functions for fuzzy logic and calculates
# the membership degrees for "cool," "warm," and "hot" 
# based on an input value x. The membership functions include triangular,
#  left shoulder, and right shoulder types. The main function takes 
# an input value from the command line, computes the membership degrees, 
# and prints them out.
# Triangular, Trapezoidal, Gaussian และ Sigmoidal

def main():
    cool_rule = 100
    warm_rule = 500
    hot_rule = 1000

    if len(sys.argv) > 3:
        u_cool = float(sys.argv[1])
        u_warm = float(sys.argv[2])
        u_hot = float(sys.argv[3])
        fan_speed = ((u_cool * cool_rule) + (u_warm * warm_rule)
                      + (u_hot * hot_rule)) / (u_cool + u_warm
                                               + u_hot)
        print(f"ความเร็วของพัดลม: {fan_speed} RPM")
    else:
        print("ผิดพลาด")

if __name__ == "__main__":
    main()