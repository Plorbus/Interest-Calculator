# write your code here
import math
import argparse


parser = argparse.ArgumentParser("Tool for taking in input for A,P,I,N")
parser.add_argument("--payment", type=float, help="annuity payment = A")
parser.add_argument("--principal", type=float)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
parser.add_argument("--type", type=str)
#principal = float(input("Enter the loan principal: \n> "))
args = parser.parse_args()

check_4 = [args.payment, args.principal, args.periods, args.interest, args.type]

value_check = [args.payment, args.principal, args.periods, args.interest]


checker = 0
for check in check_4:
    if check is not None:
        checker += 1



if checker <= 3:
    print("Incorrect parameters checker")
    quit()


if args.interest == None:
    print("Incorrect parameters")
    quit()


for value in value_check:
    if value is not None:
        if value < 0:
            print("Incorrect parameters")
            quit()



#
# if args.payment < 0 or args.interest < 0 or args.principal < 0 or args.principal < 0:
#     print("Negative")
total_intrest = 0.0
total_payment = 0.0
if args.type == "diff" or args.type == "annuity":
    i = (args.interest / 100) / 12
    P = args.principal
    n = args.periods


    if args.type == "diff":
        if args.payment == None:
            for m in range(1, n + 1):
                #D_m = (P / n) + i * (P - P * (m - 1) / n)
                principal_per_month = P / n
                interest_portion = i * (P - (P * (m - 1) / n))
                total_intrest += interest_portion
                Dm = principal_per_month + interest_portion
                total_payment += math.ceil(Dm)
                print(f"Month {m}: payment is {math.ceil(Dm)}")
            print(f"\noverpayment {total_payment - P}")

        else:
            print("Incorrect parameters")
            quit()


    else:

        if args.payment == None:
            A = args.principal * (i * (1 + i) ** args.periods) / ((1 + i) ** args.periods - 1)
            overpay = math.ceil(A) * n
            print(f"Your annuity payment = {math.ceil(A)}")
            print(f"Overpayment = {overpay - P}")

        if args.principal == None:
            P1 = args.payment / ((i * (1 + i)**args.periods) / ((1 + i)**args.periods - 1))
            overpay = (args.payment * args.periods) - math.floor(P1)
            print(f"Your loan principal = {math.floor(P1)}! ")
            print(f"Overpayment = {round(overpay)}")

        if args.periods == None:
            N = math.ceil(math.log(args.payment / (args.payment - i * args.principal)) / math.log(1 + i))
            years = N // 12
            remain = N % 12
            overpay = args.payment * years
            overpay = args.payment * N - P
            if remain == 0:
                print(f"It will take {(years)} years to repay this loan!")
                print(f"Overpayment = {round(overpay)}")
            else:
                print(f"It will take {(years)} years and {remain} months to repay this loan!")
                print(f"Overpayment = {round(overpay)}")


else:
    print("Incorrect parameters")
    quit()


#print(f"Your loan principal = {A}")