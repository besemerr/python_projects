#initialization
lawn_length = 20# ft.
lawn_width = 10# ft.
sod_cost = 2#/sq ft.
sod_unit_length = 3# ft.
sod_unit_width = 2# ft.

#calculate
lawn_area = lawn_length * lawn_width
sod_unit_area = sod_unit_length * sod_unit_width
sod_units_needed = lawn_area / sod_unit_area
sod_unit_cost = sod_cost * sod_unit_area
total_sod_cost = sod_units_needed * sod_unit_cost

#print
print("${:,.2f}".format(total_sod_cost))
