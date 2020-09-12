
"""
    This script fills the CoffeeMachine & CooffeePods models with the data provided
"""
from Coffee.models import CoffeeMachine, CoffeePod

#####################################################
First we will fill coffeemachine table

f = open("coffeemachines.txt", "r")
for line in f:
    line = line.split('–')[1] # We are interested in the part after the '–' char. eg. small machine, deluxe model, water line compatible
    line = line.split(',')

    # We get the first field: product_type
    if 'small' in line[0]:
        product_type = 'COFFEE_MACHINE_SMALL'
    elif 'large' in line[0]:
        product_type = 'COFFEE_MACHINE_LARGE'
    else:
        product_type = 'ESPRESSO_MACHINE'

    # Then we get the second field: model
    if 'base' in line [1]:
        model = 'BASE'
    elif 'premium' in line [1]:
        model = 'PREMIUM'
    else:
        model = 'DELUXE'

    # Then we get the third field: water_line_compatible
    water_line_compatible = True if len(line) == 3 else False
    # Create the object
    CoffeeMachine.objects.create(product_type=product_type, model=model, water_line_compatible=water_line_compatible)
f.close()
#####################################################
# Then we will fill coffeepods table

f = open("coffeepods.txt", "r")
for line in f:
    line = line.split('–')[1] # We are interested in the part after the '–' char. eg. small machine, deluxe model, water line compatible
    line = line.split(',')

    # We get the first field: product_type
    if 'small' in line[0]:
        product_type = 'COFFEE_POD_SMALL'
    elif 'large' in line[0]:
        product_type = 'COFFEE_POD_LARGE'
    else:
        product_type = 'ESPRESSO_POD'

    # We get the second field: pack_size
    pack_size = line[1].partition(' ')[2][0]

    # We get the third field: coffee_flavor
    if 'vanilla' in line[2]:
        coffee_flavor = 'COFFEE_FLAVOR_VANILLA'
    elif 'caramel' in line[2]:
        coffee_flavor = 'COFFEE_FLAVOR_CARAMEL'
    elif 'psl' in line[2]:
        coffee_flavor = 'COFFEE_FLAVOR_PSL'
    elif 'mocha' in line[2]:
        coffee_flavor = 'COFFEE_FLAVOR_MOCHA'
    else:
        coffee_flavor = 'COFFEE_FLAVOR_HAZELNUT'
    # Create the object
    CoffeePod.objects.create(product_type=product_type, pack_size=pack_size, coffee_flavor=coffee_flavor)
f.close()