#way of storing and organizing data. 
# Simpler than using a lot of variables, you could use, for example, just one:

usa_states = [
    "Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", 
    "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", 
    "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", 
    "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", 
    "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", 
    "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", 
    "California", "Minnesota", "Oregon", "Kansas", "West Virginia", 
    "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", 
    "Montana", "Washington", "Idaho", "Wyoming", "Utah", 
    "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawi"
]

# the order is very important. 
# Like if you want to organize them in the order they joined in the union.
print(f"5 states: {usa_states[0:5]}")

#using index[] to change data
usa_states[49] = 'Hawaii'

#add new data:
usa_states.append("Yukon Territory")
print(usa_states)