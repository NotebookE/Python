def pribavka(zarplata, avto):
    k=0
    if(avto > 10):
        k = round((avto - 10) * 0.02 * zarplata)
    return k

a=int(input('Введите зарплату сотрудника: '))
b=int(input('Введите количество автомобилей проданных за месяц: '))
c=pribavka(a,b)
print('В этом месяце прибавка к зарплате составит: ' + str(c))