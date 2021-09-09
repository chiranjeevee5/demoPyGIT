def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person('chiranjeevee', age = - 30, workplace = ' - Washington DC' , location = ' - Chennai')