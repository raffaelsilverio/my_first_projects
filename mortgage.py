while True:
    print('-' * 25)
    print('    Mortage Calculator    ')
    print('-' * 25)
    months = int(input('Enter mortgage term (in months): '))
    rate = float(input('Enter interest rate: '))
    loan = float(input('Enter loan value: '))

    monthly_rate = rate / 100 / 12
    payment = (monthly_rate / ( 1 - (1 + monthly_rate) ** (-months))) * loan
    print(f'Monthly payment for a ${loan:.2f}, {(months / 12)} year mortgage at {rate:.2f}% interest rate is: {payment:.2f}' )
    print('-' * 25)
    restart = input('Do you want to start over?[Y/N] ').upper()
    if 'N' in restart:
        print('-' * 30)
        print('GoodBye...')
        break
