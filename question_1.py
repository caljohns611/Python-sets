#question 1 task 1

our_routes = {"MCI", "ATL", "LAX", "SLC" }
competitor_routes = {"ATL", "MDW", "SFO", "LAX"}

Both_airlines = our_routes.intersection(competitor_routes)
unique_destinations = our_routes.difference(competitor_routes)

all_routes = our_routes.union(competitor_routes)
shared_destinations = our_routes.intersection(competitor_routes)
routes_not_both = all_routes.difference(shared_destinations)


print("Destinations that are unique to our airline: ", unique_destinations)
print("Destinations that both airlines fly to: ", Both_airlines)
print("Destinations that both airlines dont share: ", routes_not_both)
