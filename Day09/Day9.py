distLookups = dict()
routes = list()
routeDistances = list()

def routesFrom(startingCity, route):
    for k in distLookups[startingCity]:
        if k not in route:
            nextRoute = list(route)
            nextRoute.append(k)
            if len(nextRoute) == len(distLookups):
                routes.append(nextRoute)
                return
            routesFrom(k, nextRoute)

#with open("Day9TestInput.txt") as f:
with open("Day9Input.txt") as f:
    for line in f.readlines():
        cities, distance = line.split(" = ")
        first, second = cities.split(" to ")
        print first, second, distance

        if first not in distLookups:
            distLookups[first] = dict()
        distLookups[first][second] = int(distance)

        if second not in distLookups:
            distLookups[second] = dict()
        distLookups[second][first] = int(distance)

    for k in distLookups:
        currentRoute = list()
        currentRoute.append(k)
        routesFrom(k, currentRoute)

    for route in routes:
        #print route
        lastCity = None
        routeDist = 0

        for city in route:
            if lastCity:
                #print "looking up from " + lastCity + " to " + city
                routeDist += distLookups[lastCity][city]
            lastCity = city
        print route, routeDist
        routeDistances.append(routeDist)

    print min(routeDistances)
    print max(routeDistances)