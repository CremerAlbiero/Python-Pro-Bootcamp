# Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "England": ["London", "Chester" ,"Cambridge",],
    "Germany": ["Berlin", "Hamburg", "Stuttgart",]
}

# Nesting Dictionary in a Dictionary
travel_visits = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits:": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart",], "total_visits": 5}
}


# Nesting Dictionary in a List
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
]