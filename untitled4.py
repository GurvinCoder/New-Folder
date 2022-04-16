savings=int(input('Сколько денег хотите положить: '))
interest=int(input('Под какой процент вы кладете: '))/100
time=int(input('На сколько лет вы хотите положить деньги в банк: '))
def bank(s, i=0.02, t=1):
    if i>0.05:
        print('Максимальный процент в банке 5% годовых')
        return False
    def calculate_savings(savings, interest, time):
        for t in range(time):
            savings+=savings*interest
        return savings
    savings=calculate_savings(s, i, t)
    return savings
total_savings=bank(savings, interest, time)
print(f'Ваши деньги:{total_savings}')