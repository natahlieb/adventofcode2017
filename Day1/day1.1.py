import sys

def main(value):


    inputList = list(value)
    print(inputList)
    sum = 0
    for k in range(0, len(inputList)// 2, 1):
        print('k is {}, index to compare is  {}'.format(k, k + len(inputList)//2))
        if(inputList[k] == inputList[k + len(inputList)//2]):
            sum += int(inputList[k])

    print( sum * 2)

if __name__ == "__main__":
    main(sys.argv[1])

    