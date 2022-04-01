import pytest
import time

def test_getSimpleCalc():
    x=int(input("\nEnter the Num1 : "))
    y=int(input("\nEnter the Num2 : "))
    sum=(x+y)
    powFun=x**y
    print("\nSum of Two numbers : ",sum)
    print("\nValue of "+str(x)+" to the power "+str(y)+" : ",powFun)

@pytest.mark.skip
def test_getTestUnit2():
    assert 5==4.999
    print("\nThis is 2nd TestCase..!!")


def test_getTestARTUnit3():
    assert 5==4.999
    print("\nThis is 4th with Assert TestCase..!!")


def test_getFuncADStest():
    for i in range(10):
        print("\nHey!!! Ping Me!! ",i)
        time.sleep(2)
        print("\nPong!!! ")


@pytest.mark.xfail
def test_getCLR_lpl():
    print("\nHey!! this SDET!!")
    print("\nI am applying xfail marker to it!!!!..")

@pytest.mark.xfail
def test_getSDET_qaAuto():
    print("\nHey!! SDET!!---> Marking xfail 2")
    print("\nPlease have transition to DataScientist/ML/Developer!!..")