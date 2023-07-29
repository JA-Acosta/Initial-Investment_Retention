'''
>>> JAAR
>>> 07/28/2023
>>> Sell Price Calculator
>>> Version 1
'''

'''
>>> Generates a program that will ask the user to input a stocks ticker, purchase price, and initial number of shares purchased in order to calculate the sell price required to retain both a specific number of shares and the entire initial investment in full.
'''

def stock_information()-> dict :
    '''
    >>> Asks the user for the stock information including the ticker, purchase price, and how many stocks they would like to retain after selling their shares.

    >>> Return: (dict) stock {key : list[price, shares_purchased]}
    '''
    ticker = input('Enter the ticker symbol: ')
    stock = { ticker : [0, 0]}

    while not stock[ticker][0] or  stock[ticker][0] < 0 :
        try :
            stock[ticker][0] = float(input('Enter the purchase price: '))
            if stock[ticker][0] < 0 :
                print("The stock price can't be negative!")
                continue
        except ValueError :
            print('Your answer was invalid!')

    while not stock[ticker][1] or  stock[ticker][1] < 0 :
        try :
            stock[ticker][1] = int(input('How many shares did you purchase?: '))
            if stock[ticker][1] < 0 :
                print("Error! Please enter a positive integer!")
                continue
        except ValueError :
            print('Your answer was invalid!')

    return stock

def sale_price(stock, info) :
    retain = 0

    while retain or retain < 1 or not isinstance(int, retain) :
        try :
            retain = int(input(f'How many shares of {stock} do you want to retain?: '))
            if retain < 0 :
                raise ValueError
        except ValueError :
            print('Your input was invalid!')
        else :
            return info[0] + (retain * info[0] / (info[1] - retain))


def main() :
    for key, value in stock_information().items() :
        print(sale_price(key, value))

if __name__ == '__main__' :
    main()