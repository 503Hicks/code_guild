# Lab 9: Unit Converter

# This lab will involve writing a program that allows the user to convert a number between units.

# Version 1

# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

# > what is the distance in feet? 12
# > 12 ft is 3.6576 m
# Version 2

# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m
# Below is some sample input/output:

# > what is the distance? 100
# > what are the units? mi
# > 100 mi is 160934 m
# Version 3

# Add support for yards, and inches.

# 1 yard is 0.9144 m
# 1 inch is 0.0254 m
# Version 4

# Now we'll ask the user for the distance, the starting units, and the units to convert to.

# You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

# ft	mi	m	km
# ft	1		0.3048	
# mi		1	1609.34	
# m	1/0.3048	1/1609.34	1	1/1000
# km			1000	1
# But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

# Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

# Below is some sample input/output:

# > what is the distance? 100
# > what are the input units? ft
# > what are the output units? mi
# 100 ft is 0.0189394 mi



meters = {
'in': 0.0254,
'ft': 0.3048,
'yd': 0.9144,
'm': 1,
'mi': 1609.34,
'km': 1000,
}

distance = float(input('Enter a distance: '))
start_units = input('Enter type of units: ')
end_units = meters.get(input('Enter the unit you would like to convert to: '))



m = 1
ft = distance * 0.3048 
mi = distance * 1609.34
km = distance * 1000
yd = distance * 0.9144
inch = distance * 0.0254




if start_units == 'ft':
    print(f'{distance}{start_units} is {ft}m')
    feet_dist = ft/end_units
    # mi_dist = ft/1609.34
    # km_dist = ft/1000
    print(f' {distance}{start_units} converts to {feet_dist}')
    # print(mi_dist)
    # print(km_dist)
elif start_units == 'mi':
    print(f'{distance}{start_units} is {mi}m')
    mi_dist = mi/end_units
    print(mi_dist)
elif start_units == 'km':
    print(f'{distance}{start_units} is {km}m')
    km_dist = km/end_units
    print(km_dist)
elif start_units == 'yd':
    print(f'{distance}{start_units} is {yd}m')
    yd_dist = yd/end_units
    print(yd_dist)
elif start_units == 'inch':
    print(f'{distance}{start_units} is {inch}m')
    inch_dist = inch/end_units
    print(inch_dist)