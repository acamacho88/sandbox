import time
from datetime import date
import math
#from datetime import timedelta

print "\n"
print "*" * 40
print " "
print "       WELCOME TO LOANSIM"
print "  Created by Alex Camacho, 2013"
print " "
print "*" * 40

class loan:
    #loans need NAME, PRINCIPAL AMOUNT, INTEREST RATE, INITIAL INTEREST AMOUNT, MONTHLY PAYMENT AMOUNT,
    #YEAR OF LAST PAYMENT, MONTH OF LAST PAYMENT, DAY OF LAST PAYMENT, SCHEDULED PAY DATE
    def __init__(self, n, princ, intrate, initint, monthly, lastyr, lastmth, lastd):#, pdate):
        self.name = n
        self.principal = princ
        self.rate = intrate
        self.interest = initint
        self.payment = monthly
        self.year = lastyr
        self.month = lastmth
        self.day = lastd
        #self.paydate = pdate
        self.simprincipal = princ
        self.prevmonth = lastmth
        self.prevyear = lastyr
        self.prevint = initint
        self.currpay = monthly
        self.totalpaid = 0
        self.monthspaid = 0
        
    def __str__(self):
        return (self.name + ' ' +  str(self.principal) + ' ' + str(self.rate) + ' ' + \
        str(self.interest) + ' ' + str(self.payment) + ' ' + str(self.year) + ' ' + \
        str(self.month) + ' ' + str(self.day))

    def getPrinc(self):
        return self.principal

    def getMonth(self):
        return self.month

    def getYear(self):
        return self.year

    def getPayment(self):
        return self.payment

    def getSimPrinc(self):
        return self.simprincipal

    def getInt(self):
        return self.interest

    def getMonthsPaid(self):
        return self.monthspaid

    def getTotalPaid(self):
        return self.totalpaid

    def getPrevMonth(self):
        return self.prevmonth

    def setSimPrinc(self,amt):
        self.simprincipal = amt

    def setPrevMonth(self,month):
        self.prevmonth = month

    def setPrevYear(self,yr):
        self.prevyear = yr

    def setPrevInt(self,int):
        self.prevint = int

    def setCurrPay(self,pay):
        self.currpay = pay

    def setTotalPaid(self,tot):
        self.totalpaid = tot

    def setMonthsPaid(self,months):
        self.monthspaid = months

    def resetVals(self):
        self.simprincipal = self.principal
        self.prevmonth = self.month
        self.prevyear = self.year
        self.prevint = self.interest
        self.currpay = self.payment
        self.totalpaid = 0
        self.monthspaid = 0

# Takes in a question, ensures user input is of specified type
def checktype(q,type):
    i = 1
    while i == 1:
        i = 0
        val = raw_input(q)
        try:
            val = float(val)
            if type == "int":
                if val % 1 != 0:
                    print "\n"
                    print "Not an integer"
                    print "\n"
                    i = 1
        except ValueError:
            print "\n"
            print "Not a valid number, make sure no commas are entered"
            print "\n"
            i = 1
    if type == "int":
        val = int(val)
    return val

# Handles an individual loan addition
def loanadd():
    print "\n"
    name = raw_input("What would you like to name the loan? ")
    princ = checktype("What is the current principal amount of the loan? ","float")
    intrate = checktype("What is the interest rate on the loan? ","float")
    interest = checktype("How much interest is left over to pay \n(if your previous payment could not clear the accrued interest)? ","float")
    payment = checktype("What is the standard monthly payment on the loan? ","float")
    lastyear = checktype("In what year was the last payment made? ","int")
    lastmonth = checktype("Enter the number of the month the last payment was made ","int")
    lastday = checktype("Enter the number of the day the last payment was made ","int")
    loanlist.append(loan(name,princ,intrate,interest,payment,lastyear,lastmonth,lastday))	
    return

# Makes sure a loan number selected makes sense
def loanselect(message):
    j = 1
    while j == 1:
        j = 0
        n = checktype(message,"int")
        if n <= 0 or n > len(loanlist):
            print "\n"
            print "Invalid loan number"
            print "\n"
            j = 1
    return n

# Handles loan modifications
def loanmodify():
    if len(loanlist) >= 1:
        printloans()
        print "\n"
        loannum = loanselect("Enter the number of the loan you would like to modify ")
        printloans()
        k = 1
        while k == 1:
            k = 0
            print "\n"
            col = raw_input("Enter the letter of the column you wish to modify ")
            if col == "a" or col == "A":
                loanlist[loannum-1].name = raw_input("Enter the loan name ")
            elif col == "b" or col == "B":
                loanlist[loannum-1].principal = checktype("Enter the principal ","float")
            elif col == "c" or col == "C":
                loanlist[loannum-1].rate = checktype("Enter the interest rate ","float")
            else:
                print "\nInvalid column letter"
                k = 1
        printloans()
    else:
        print "No loans entered!"
    return

# Handles deletion of a loan
def loanremove():
    if len(loanlist) >= 1:
        printloans()
        index = loanselect("\nEnter the number of the loan you would like removed ")
        loanlist.pop(index-1)
        if len(loanlist) >= 1:
            printloans()
    else:
        print "No loans entered!"
    return

# Saves current loans to a file
def saveloans():
    if len(loanlist) >= 1:
        f = open('savedloans.txt','a')
        f.write('**'+raw_input("Enter the name you'd like to call the current configuration\n")+'**\n')
        f.write(str(len(loanlist)) + '\n')
        for l in loanlist:
            f.write(str(l) + '\n')
        f.close()
    else:
        print "No loans entered!"
    return

# Reads in loans from file
def openloans():
    check = 0
    count = 0
    try:
        f = open('savedloans.txt','r')
        del loanlist[:]
        print "Currently saved configurations:\n"
        for line in f:
            if line[0:2] == '**':
                print line + '\n'
        print '\n'
        print 'Enter the name of the configuration you wish to load:\n'
        f.close()
        f = open('savedloans.txt','r')
        entry = raw_input()
        for line in f:
            if check == 2 and count != numloans:
                part = line.rsplit(' ')
                loanlist.append(loan(part[0],float(part[1]),float(part[2]),float(part[3]),float(part[4]),
                int(part[5]),int(part[6]),int(part[7][:-1])))
                count += 1
            if check == 1:
                numloans = int(line)
                check = 2
            if line[2:-3] == entry:
                check = 1
        f.close()
    except IOError:
        print "File with configurations not found!\n"
    return	

# Prints out all entered information on loans
def printloans():
    print "\n"
    print "  " + "(a)Name" + " "*16 + "(b)Principal" +" "*4 +"(c)Int Rate"
    print "-" * 54
    for c in range(len(loanlist)):
        print "|" + " "*22 + "|" + " "*14 + "|" + " "*14 + "|"
        print "|" + "  " + str(c+1) + ". " + loanlist[c].name + " "*(17-len(loanlist[c].name)) + "|" \
            + "  " + "$" + str(loanlist[c].principal) + " "*(11-len(str(loanlist[c].principal))) + "|" \
            + "  " + str(loanlist[c].rate) + "%" + " "*(11-len(str(loanlist[c].rate))) + "|"
        print "|" + " "*22 + "|" + " "*14 + "|" + " "*14 + "|"
        print "-" * 54
    return

# Calculates interest from amount of time since last payment
def intcalc(l):
    if l.prevmonth == 12:
        datediff = (date((l.prevyear+1),1,l.day) - date(l.prevyear,l.prevmonth,l.day)).days
        l.prevmonth = 1
        l.prevyear += 1
    else:
        datediff = (date(l.prevyear,(l.prevmonth+1),l.day) - date(l.prevyear,l.prevmonth,l.day)).days
        l.prevmonth += 1
    # Interest = Principal * (interest rate) / 365.25 * (days since last payment)
    interest = l.simprincipal * l.rate/100.0 / 365.25 * datediff
    interest += l.prevint
    return interest
	
def simmenu():

    simloop = 1

    while simloop == 1:

        print "\n"
        print "Select a number from the following menu:"
        print "\n"
        print "1. Run simulation"
        print "2. Options"
        print "3. Back"
        print "\n"

        choice = raw_input()

        # Makes sure a number was entered

        check1 = False

        for e in range(3):
            if choice == str(e+1):
                check1 = True

        if check1 == False:
            print "\nINVALID ENTRY"
        else:

            choice = int(choice)

            if choice == 1:
                paysim()
            elif choice == 2:
                printsimoptions()
            elif choice == 3:
                simloop = 0

    return


def printsimoptions():
    # Set option menu text
    monthlyprinttxt = ['1. Monthly print statements:'+' '*24 +'+disabled\n'+' '*53+'enabled\n',
                       '1. Monthly print statements:'+' '*25 +'disabled\n'+' '*52+'+enabled\n']

    payoffaddtxt = ['2. When a loan is paid off, add payment amount:     +disabled\n'+' '*53+'to smallest loan\n'+' '*53+'to largest loan',
                    '2. When a loan is paid off, add payment amount:      disabled\n'+' '*52+'+to smallest loan\n'+' '*53+'to largest loan',
                    '2. When a loan is paid off, add payment amount:      disabled\n'+' '*53+'to smallest loan\n'+' '*52+'+to largest loan']

    loop2 = 1

    while loop2 == 1:
        print "\n"
        print "Select an option to cycle through the choices"
        print "\n"
        print monthlyprinttxt[monthlyprint[0]]
        print payoffaddtxt[payoffadd[0]]
        print "3. Back"
        print "\n"

        choice2 = raw_input()

        check2 = False

        for f in range(3):
            if choice2 == str(f+1):
                check2 = True

        if check2 == False:
            print "\nINVALID ENTRY"
        else:

            choice2 = int(choice2)

            if choice2 == 1:
                monthlyprint.append(monthlyprint[0])
                monthlyprint.pop(0)
            elif choice2 == 2:
                payoffadd.append(payoffadd[0])
                payoffadd.pop(0)
            elif choice2 == 3:
                loop2 = 0

    return


def paysim():

    # Resets relevant values for all loans

    for e in range(len(loanlist)):
        loanlist[e].resetVals()

    outstanding = 1
    currmonths = 1

    while outstanding > 0:
        # Prints the current month if option is selected
        if monthlyprint[0] == 1:
            print '\n'
            print 'MONTH ' + str(currmonths)
        # Makes sure the check for any outstanding principal is reset every month calculated	
        outstanding = loanlist[0].simprincipal
        # Cycles through each loan
        for d in range(len(loanlist)):
            # Makes sure the loan being analyzed has a balance
            if loanlist[d].simprincipal > 0:
                intamount = intcalc(loanlist[d])
                # Checks if the payment can clear the accrued interest
                if loanlist[d].currpay >= intamount:
                    # If the interest can be cleared, makes sure if the loan is being 
                    # finished off that no more is paid than necessary
                    if (loanlist[d].currpay - intamount) >= loanlist[d].simprincipal:
                        loanlist[d].totalpaid += loanlist[d].simprincipal
                        loanlist[d].prevint = 0
                        loanlist[d].simprincipal = 0
                        loanlist[d].monthspaid = currmonths
                        # Takes care of payment adding options if loan is paid off
                        if payoffadd[0] != 0:
                            adjustloan = 0
                            # Gets a nonzero value for initial loan comparison
                            for f in range(len(loanlist)):
                                if loanlist[f].simprincipal > 0:
                                    adjustloan = loanlist[f].simprincipal
                            # Finds either min loan principal amount or max depending on user choice
                            for f in range(len(loanlist)):
                                if payoffadd[0] == 1:
                                    if loanlist[f].simprincipal > 0 and loanlist[f].simprincipal <= adjustloan:
                                        adjustloan = loanlist[f].simprincipal
                                        ii = f
                                elif payoffadd[0] == 2:
                                    if loanlist[f].simprincipal >= adjustloan:
                                        adjustloan = loanlist[f].simprincipal
                                        ii = f
                            loanlist[ii].currpay += loanlist[d].currpay
                    else:
                        loanlist[d].totalpaid += loanlist[d].currpay
                        #if d == 2 and currmonths == 1:
                        #	loanlist[d].simprincipal -= loanlist[d].currpay - intamount + 293.61
                        #	loanlist[d].totalpaid += loanlist[d].currpay + 1000
                        #	loanlist[d].currpay += 17.65 + 32.35
                        #else:
                        #	loanlist[d].simprincipal -= loanlist[d].currpay - intamount
                        #	loanlist[d].totalpaid += loanlist[d].currpay
                        loanlist[d].simprincipal -= loanlist[d].currpay - intamount
                        loanlist[d].prevint = 0
                else:
                    loanlist[d].prevint = intamount - loanlist[d].currpay
                    loanlist[d].totalpaid += loanlist[d].currpay

                # If option is selected, print monthly statements for each loan
                if monthlyprint[0] == 1:
                    print loanlist[d].name + ' loan'
                    print 'Total payment: $' + str(loanlist[d].currpay) +', Applied Interest: $' + \
                            str(intamount) + ', Applied Principal: $' + str(loanlist[d].currpay-intamount)
                    print 'Principal: $' + str(loanlist[d].simprincipal)

#str(intamount) + ', Applied Principal: $' + str((loanlist[d].currpay+math.fabs(loanlist[d].currpay))/2.0)

#				currmonths += 1   (old currmonths assignment)

                if loanlist[d].simprincipal > outstanding:
                    outstanding = loanlist[d].simprincipal

        currmonths += 1

    cumulat = 0
    maxtime = 0
    for d in range(len(loanlist)):
        print "\n"
        print "Total amount paid: $" + str(loanlist[d].totalpaid)
        print "Total months paid: " + str(loanlist[d].monthspaid)
        cumulat = cumulat + loanlist[d].totalpaid
        if loanlist[d].monthspaid > maxtime:
            maxtime = loanlist[d].monthspaid

    print "\n"
    print "Cumulative amount paid: $" + str(cumulat)
    print "Total months paid: " + str(maxtime)

    print "\n"
    return

loop = 1

loanlist = []

# Main program loop

while loop == 1:

    # Initializes sim option lists

    monthlyprint = [0,1]
    payoffadd = [0,1,2]

    print "\n"
    print "Select a number from the following menu:"
    print "\n"
    print "1. Enter new loans"
    print "2. Modify an existing loan"
    print "3. Remove loans"
    print "4. Save current loan setup"
    print "5. Open existing loan setup"
    print "6. Enter repayment simulation"
    print "7. Exit program"
    print "\n"

    selection = raw_input()

    # Makes sure a number was entered

    check = False

    for a in range(10):
        if selection == str(a+1):
            check = True

    if check == False:
        print "\nINVALID ENTRY"
    else:

        # Main menu selection divider

        selection = int(selection)
        if selection == 1:
            newloans = int(raw_input("\nHow many new loans would you like to enter? "))
            # Goes through loan adding function specified number of times
            for b in range(newloans):
                loanadd()
            print "\nCurrent loans entered:"
            printloans()
        elif selection == 2:
            loanmodify()
        elif selection == 3:
            loanremove()
        elif selection == 4:
            saveloans()
        elif selection == 5:
            openloans()
            printloans()
        elif selection == 6:
            simmenu()
        elif selection == 7:
            loop = 0

