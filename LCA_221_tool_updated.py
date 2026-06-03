import time

cities = {
    "Los Angeles": {
        "country": "USA",
        "lat": 0.5941,
        "lon": -2.0637,
        "greenness": 0.5147504719,
        "materials": ["EVA", "Polyester", "PU", "Cotton", "Nylon", "Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Sao Paulo": {
        "country": "Brazil",
        "lat": -0.4109,
        "lon": -0.8137,
        "greenness": 1.238202247,
        "materials": ["Polyester", "Rubber", "Cotton", "Nylon", "Adhesive", "Aluminum","Cardboard"]
    },
    "Chennai": {
        "country": "India",
        "lat": 0.2283,
        "lon": 1.4009,
        "greenness": 1.617977528,
        "materials": ["EVA", "Polyester", "PU", "Rubber", "Cotton", "Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Guangzhou": {
        "country": "China",
        "lat": 0.4037,
        "lon": 1.9769,
        "greenness": 1.807191011,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton", "Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Ho Chi Minh City": {
        "country": "Vietnam",
        "lat": 0.1889,
        "lon": 1.861,
        "greenness": 1.481348315,
        "materials": ["Polyester", "Rubber", "Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Jakarta": {
        "country": "Indonesia",
        "lat": -0.10778,
        "lon": 1.86518,
        "greenness": 1.955054802,
        "materials": ["Polyester", "Rubber", "Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Manila": {
        "country": "Philippines",
        "lat": 0.2548,
        "lon": 2.1116,
        "greenness": 1.665168539,
        "materials": ["Polyester", "Rubber", "Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Bangkok": {
        "country": "Thailand",
        "lat": 0.24,
        "lon": 1.7541,
        "greenness": 0.8606741573,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton","Nylon","Adhesive","Cardboard","TPU"]
    },
    "Gothenburg": {
        "country": "Sweden",
        "lat": 1.0072,
        "lon": 0.209,
        "greenness": 0.0404494382,
        "materials": ["EVA", "Polyester", "PU","Aluminum","Cardboard"]
    },
    "Copenhagen": {
        "country": "Denmark",
        "lat": 0.9718,
        "lon": 0.2193,
        "greenness": 0.3101123596,
        "materials": ["EVA", "Polyester", "PU","Cardboard"]
    },
    "Houston": {
        "country": "USA",
        "lat": 0.519,
        "lon": -1.664,
        "greenness": 0.8740853933,
        "materials": ["EVA", "Polyester", "PU","Cotton","Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Manaus": {
        "country": "Brazil",
        "lat": -0.0543,
        "lon": -1.0476,
        "greenness": 1.238202247,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Mumbai": {
        "country": "India",
        "lat": 0.3329,
        "lon": 1.2718,
        "greenness": 1.425797753,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton", "Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Shenzhen": {
        "country": "China",
        "lat": 0.393,
        "lon": 1.991,
        "greenness": 1.807191011,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton", "Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Da Nang": {
        "country": "Vietnam",
        "lat": 0.2804,
        "lon": 1.8888,
        "greenness": 1.481348315,
        "materials": ["Polyester", "Rubber","Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Bandung": {
        "country": "Indonesia",
        "lat": -0.12068,
        "lon": 1.87823,
        "greenness": 1.612808989,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Cebu City": {
        "country": "Philippines",
        "lat": 0.1799,
        "lon": 2.1625,
        "greenness": 1.665168539,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Laem Chabang": {
        "country": "Thailand",
        "lat": 0.2283,
        "lon": 1.7609,
        "greenness": 0.8606741573,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton","Nylon","Adhesive","Cardboard","TPU"]
    },
    "Malmo": {
        "country": "Sweden",
        "lat": 0.9705,
        "lon": 0.2269,
        "greenness": 0.0404494382,
        "materials": ["EVA", "Polyester", "PU","Aluminum","Cardboard"]
    },
    "Aarhus": {
        "country": "Denmark",
        "lat": 0.9802,
        "lon": 0.1782,
        "greenness": 0.3101123596,
        "materials": ["EVA", "Polyester", "PU","Cardboard"]
    },
    "Charlotte": {
        "country": "USA",
        "lat": 0.6148,
        "lon": -1.4109,
        "greenness": 0.5861020225,
        "materials": ["EVA","Polyester","PU","Cotton","Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Porto Alegre": {
        "country": "Brazil",
        "lat": -0.524,
        "lon": -0.894,
        "greenness": 1.238202247,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Surat": {
        "country": "India",
        "lat": 0.3695,
        "lon": 1.2711,
        "greenness": 1.91011236,
        "materials": ["Polyester", "Rubber","Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Wenzhou": {
        "country": "China",
        "lat": 0.489,
        "lon": 2.106,
        "greenness": 1.880224719,
        "materials": ["EVA", "Polyester", "PU", "Rubber","Cotton","Nylon","Adhesive","Aluminum","Cardboard","TPU"]
    },
    "Hai Phong": {
        "country": "Vietnam",
        "lat": 0.3642,
        "lon": 1.8619,
        "greenness": 1.481348315,
        "materials": ["Polyester", "Rubber","Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Surabaya": {
        "country": "Indonesia",
        "lat": -0.1266,
        "lon": 1.9679,
        "greenness": 1.955054802,
        "materials": ["Polyester", "Rubber","Cotton","Nylon","Adhesive","Cardboard"]
    },
    "Davao City": {
        "country": "Philippines",
        "lat": 0.1234,
        "lon": 2.1923,
        "greenness": 1.665168539,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Chiang Mai": {
        "country": "Thailand",
        "lat": 0.328,
        "lon": 1.727,
        "greenness": 0.8606741573,
        "materials": ["Polyester", "Rubber","Cotton","Adhesive","Cardboard"]
    },
    "Stockholm": {
        "country": "Sweden",
        "lat": 1.0355,
        "lon": 0.3153,
        "greenness": 0.0404494382,
        "materials": ["EVA", "Polyester", "PU","Aluminum","Cardboard"]
    },
    "Odense": {
        "country": "Denmark",
        "lat": 0.967,
        "lon": 0.181,
        "greenness": 0.3101123596,
        "materials": ["Polyester","Cardboard"]
    }
}

materials_four = {
    "EVA": {
        "embodied_carbon": 2.1,
        "quantity": 0.3
    },
    "Polyester": {
        "embodied_carbon": 3.12,
        "quantity": 0.15
    },
    "PU": {
        "embodied_carbon": 3.75,
        "quantity": 0.08
    },
    "Rubber": {
        "embodied_carbon": 3.18,
        "quantity": 0.25
    }
}

materials_five = {
    "EVA": {
        "embodied_carbon": 2.1,
        "quantity": 0.3
    },
    "Polyester": {
        "embodied_carbon": 3.12,
        "quantity": 0.15
    },
    "PU": {
        "embodied_carbon": 3.75,
        "quantity": 0.08
    },
    "Rubber": {
        "embodied_carbon": 3.18,
        "quantity": 0.25
    },
    "Cotton": {
        "embodied_carbon": 1.15,
        "quantity": 0.1
    }
}

materials_ten = {
    "EVA": {
        "embodied_carbon": 2.1,
        "quantity": 0.3
    },
    "Polyester": {
        "embodied_carbon": 3.12,
        "quantity": 0.15
    },
    "PU": {
        "embodied_carbon": 3.75,
        "quantity": 0.08
    },
    "Rubber": {
        "embodied_carbon": 3.18,
        "quantity": 0.25
    },
    "Cotton": {
        "embodied_carbon": 1.15,
        "quantity": 0.1
    },
    "Nylon": {
        "embodied_carbon": 5.5,
        "quantity": 0.03
    },
    "Adhesive": {
        "embodied_carbon": 6.3,
        "quantity": 0.02
    },
    "Aluminum": {
        "embodied_carbon": 14.77,
        "quantity": 0.005
    },
    "Cardboard": {
        "embodied_carbon": 1.53,
        "quantity": 0.2
    },
    "TPU": {
        "embodied_carbon": 3.5,
        "quantity": 0.15
    }
}

materials_six = {
    "EVA": {
        "embodied_carbon": 2.1,
        "quantity": 0.3
    },
    "Polyester": {
        "embodied_carbon": 3.12,
        "quantity": 0.15
    },
    "PU": {
        "embodied_carbon": 3.75,
        "quantity": 0.08
    },
    "Rubber": {
        "embodied_carbon": 3.18,
        "quantity": 0.25
    },
    "Cotton": {
        "embodied_carbon": 1.15,
        "quantity": 0.1
    },
    "Nylon": {
        "embodied_carbon": 5.5,
        "quantity": 0.03
    }
}

import math

def haversine(lat1, lon1, lat2, lon2):
    rad = 6371 # km
    a = math.sin((lat2-lat1)/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin((lon2-lon1)/2)**2
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return rad*c

def supply_chain_baseline(materials, cities, assembly_lat, assembly_lon, qty):
    print(f'\nCalculating transportation-minimizing supply chain baseline for assembly of {qty} units at a latitude of {assembly_lat} radians and a longitude of {assembly_lon} radians...')
    net_emissions = 0
    for material in materials:
        min_distance = float("inf")
        min_city = None
        for city in cities:
            if material in cities[city]["materials"]:
                distance_to_assembly_site = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"])
                if distance_to_assembly_site < min_distance:
                    min_distance = distance_to_assembly_site
                    min_city = city
        net_emissions += materials[material]["embodied_carbon"]*materials[material]["quantity"]*qty*cities[min_city]["greenness"]
        net_emissions += min_distance*0.000015*materials[material]["quantity"]*qty # assuming 0.000015 kg CO2 eq / km of shipping per kg package # assuming 0.01 kg CO2 eq / km of shipping for any size package
        print(f'{material} sourced from {min_city}, {cities[min_city]["country"]}, which is {min_distance} km away from assembly site.')
    print(f'\nThe total carbon emissions from this set of suppliers is {net_emissions} kg CO2 eq, accounting for material embodied carbon and transportation emissions.\n')


import heapq

def supply_chain_ucs(materials, cities, assembly_lat, assembly_lon, shoe_count):
    print(f'\nCalculating optimized supply chain via UCS for shoe assembly of {shoe_count} units at a latitude of {assembly_lat} radians and a longitude of {assembly_lon} radians...')
    start_state = ({}, list(materials.keys())) # first element is a dict with assignments of materials to chosen sources, second element is materials left to be assigned
    chain_combos = []
    chain_combo_count = 0
    heapq.heappush(chain_combos, (0, chain_combo_count, start_state))
    min_emissions = float("inf")
    min_assign = None
    while len(chain_combos) > 0:
        lowest_emissions_case = heapq.heappop(chain_combos)
        curr_emissions = lowest_emissions_case[0]
        curr_state = lowest_emissions_case[2]
        curr_assigned = curr_state[0]
        curr_pending = curr_state[1]
        if curr_emissions >= min_emissions: 
            continue
        if len(curr_pending) == 0:
            if curr_emissions < min_emissions:
                min_emissions = curr_emissions
                min_assign = curr_assigned
            continue
        next_material = curr_pending[0]
        next_pending = curr_pending[1:]
        for city in cities:
            if next_material in cities[city]["materials"]:
                added_embodied_emissions = materials[next_material]["embodied_carbon"]*materials[next_material]["quantity"]*shoe_count*cities[city]["greenness"]
                added_transportation_emissions = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"])*0.000015*materials[next_material]["quantity"]*shoe_count # assuming 0.000015 kg CO2 eq / km of shipping per kg package
                if city not in curr_assigned.values():
                    new_city_cost = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"]) * 0.000015 * 100
                    added_transportation_emissions += new_city_cost
                next_emissions = curr_emissions + added_embodied_emissions + added_transportation_emissions
                next_assigned = curr_assigned.copy() # city assignment for next_material TBD below
                next_assigned[next_material] = city
                next_state = (next_assigned, next_pending)
                chain_combo_count += 1
                heapq.heappush(chain_combos, (next_emissions, chain_combo_count, next_state))
    for material in min_assign:
        min_city = min_assign[material]
        min_distance = haversine(assembly_lat, assembly_lon, cities[min_city]["lat"], cities[min_city]["lon"])
        print(f'{material} sourced from {min_city}, {cities[min_city]["country"]}, which is {min_distance} km away from assembly site.')
    print(f'\nThe total carbon emissions from this set of suppliers is {min_emissions} kg CO2 eq, accounting for material embodied carbon and transportation emissions.\n')

def heuristic(pending_materials, materials, cities, assembly_lat, assembly_lon, qty):
    h = 0
    for material in pending_materials:
        min_distance = float("inf")
        for city in cities:
            if material in cities[city]["materials"]:
                distance = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"])
                if distance < min_distance:
                    min_distance = distance
        h += min_distance * 0.000015 * materials[material]["quantity"] * qty
    return h

def supply_chain_astar(materials, cities, assembly_lat, assembly_lon, shoe_count):
    print(f'\nCalculating optimized supply chain via A Star for shoe assembly of {shoe_count} units at a latitude of {assembly_lat} radians and a longitude of {assembly_lon} radians...')
    start_state = ({}, list(materials.keys())) # first element is a dict with assignments of materials to chosen sources, second element is materials left to be assigned
    chain_combos = []
    chain_combo_count = 0
    h = heuristic(list(materials.keys()), materials, cities, assembly_lat, assembly_lon, shoe_count)
    heapq.heappush(chain_combos, (h, chain_combo_count, (start_state, 0)))
    min_emissions = float("inf")
    min_assign = None
    while len(chain_combos) > 0:
        lowest_emissions_case = heapq.heappop(chain_combos)
        curr_state, curr_emissions = lowest_emissions_case[2]  # curr_g is the real cost
        curr_assigned = curr_state[0]
        curr_pending = curr_state[1]
        if len(curr_pending) == 0:
            if curr_emissions < min_emissions:
                min_emissions = curr_emissions
                min_assign = curr_assigned
            continue
        next_material = curr_pending[0]
        next_pending = curr_pending[1:]
        for city in cities:
            if next_material in cities[city]["materials"]:
                added_embodied_emissions = materials[next_material]["embodied_carbon"]*materials[next_material]["quantity"]*shoe_count*cities[city]["greenness"]
                added_transportation_emissions = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"])*0.000015*materials[next_material]["quantity"]*shoe_count # assuming 0.000015 kg CO2 eq / km of shipping per kg package
                if city not in curr_assigned.values():
                    new_city_cost = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"]) * 0.000015 * 100
                    added_transportation_emissions += new_city_cost
                next_emissions = curr_emissions + added_embodied_emissions + added_transportation_emissions
                next_assigned = curr_assigned.copy() # city assignment for next_material TBD below
                next_assigned[next_material] = city
                next_state = (next_assigned, next_pending)
                chain_combo_count += 1
                h = heuristic(next_pending, materials, cities, assembly_lat, assembly_lon, shoe_count)
                heapq.heappush(chain_combos, (next_emissions + h, chain_combo_count, (next_state, next_emissions)))

    for material in min_assign:
        min_city = min_assign[material]
        min_distance = haversine(assembly_lat, assembly_lon, cities[min_city]["lat"], cities[min_city]["lon"])
        print(f'{material} sourced from {min_city}, {cities[min_city]["country"]}, which is {min_distance} km away from assembly site.')
    print(f'\nThe total carbon emissions from this set of suppliers is {min_emissions} kg CO2 eq, accounting for material embodied carbon and transportation emissions.\n')

def oracle_helper(material_idx, material_list, current_assignment, current_emissions, materials, cities, assembly_lat, assembly_lon, shoe_count):
    if material_idx == len(material_list):
        return current_emissions, current_assignment
    material = material_list[material_idx]
    min_emissions = float("inf")
    min_assign = None
    
    for city in cities:
        if material in cities[city]["materials"]:
            emissions = materials[material]["embodied_carbon"] * materials[material]["quantity"] * shoe_count * cities[city]["greenness"]
            emissions += haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"]) * 0.000015 * materials[material]["quantity"] * shoe_count
            if city not in current_assignment.values():
                emissions += haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"]) * 0.000015 * 100
            new_assignment = current_assignment.copy()
            new_assignment[material] = city
            updated_emissions, updated_assignment = oracle_helper(material_idx + 1, material_list, new_assignment, current_emissions + emissions, materials, cities, assembly_lat, assembly_lon, shoe_count)

            if updated_emissions < min_emissions:
                min_emissions = updated_emissions
                min_assign = updated_assignment
    return min_emissions, min_assign

def supply_chain_oracle(materials, cities, assembly_lat, assembly_lon, shoe_count):
    material_list = list(materials.keys())
    min_emissions, min_assign = oracle_helper(0, material_list, {}, 0, materials, cities, assembly_lat, assembly_lon, shoe_count)
    for material, city in min_assign.items():
        distance = haversine(assembly_lat, assembly_lon, cities[city]["lat"], cities[city]["lon"])
        print(f'{material} sourced from {city}, {cities[city]["country"]}, which is {distance} km away.')
    print(f'\nOracle Total emissions: {min_emissions} kg CO2 eq\n')

# testing baseline on production of 1,000 shoes in Stanford, CA (lat = 0.6531 rad, lon = -2.1321 rad)
start = time.perf_counter()
supply_chain_baseline(materials_four, cities, 0.6531, -2.1321, 1000)
end = time.perf_counter()
print(f'Baseline took {end - start:.5f} seconds')

# testing baseline on production of 5,000 shoes in Madrid, Spain
start = time.perf_counter()
supply_chain_baseline(materials_four, cities, 0.7054, -0.0646, 5000)
end = time.perf_counter()
print(f'Baseline took {end - start:.5f} seconds')

# testing baseline on production of 20,000 shoes in Melbourne, Australia
start = time.perf_counter()
supply_chain_baseline(materials_four, cities, -0.6599, 2.5302, 20000)
end = time.perf_counter()
print(f'Baseline took {end - start:.5f} seconds')
        
# testing our implementation on production of 1,000 shoes in Stanford, CA (lat = 0.6531 rad, lon = -2.1321 rad)

supply_chain_ucs(materials_four, cities, 0.6531, -2.1321, 1000)
end = time.perf_counter()
print(f'UCS took {end - start:.5f} seconds')

# testing our implementation on production of 5,000 shoes in Madrid, Spain
start = time.perf_counter()
supply_chain_ucs(materials_four, cities, 0.7054, -0.0646, 5000)
end = time.perf_counter()
print(f'UCS took {end - start:.5f} seconds')

# testing our implementation on production of 20,000 shoes in Melbourne, Australia
start = time.perf_counter()
supply_chain_ucs(materials_four, cities, -0.6599, 2.5302, 20000)
end = time.perf_counter()
print(f'UCS took {end - start:.5f} seconds')

# testing our implementation on production of 1,000 shoes in Stanford, CA (lat = 0.6531 rad, lon = -2.1321 rad)
start = time.perf_counter()
supply_chain_astar(materials_four, cities, 0.6531, -2.1321, 1000)
end = time.perf_counter()
print(f'A Star took {end - start:.5f} seconds')

# testing our implementation on production of 5,000 shoes in Madrid, Spain
start = time.perf_counter()
supply_chain_astar(materials_four, cities, 0.7054, -0.0646, 5000)
end = time.perf_counter()
print(f'A Star took {end - start:.5f} seconds')

# testing our implementation on production of 20,000 shoes in Melbourne, Australia
start = time.perf_counter()
supply_chain_astar(materials_four, cities, -0.6599, 2.5302, 20000)
end = time.perf_counter()
print(f'A Star took {end - start:.5f} seconds')

# testing our implementation on production of 1,000 shoes in Stanford, CA (lat = 0.6531 rad, lon = -2.1321 rad)
start = time.perf_counter()
supply_chain_oracle(materials_four, cities, 0.6531, -2.1321, 1000)
end = time.perf_counter()
print(f'Oracle took {end - start:.5f} seconds')

# testing our implementation on production of 5,000 shoes in Madrid, Spain
start = time.perf_counter()
supply_chain_oracle(materials_four, cities, 0.7054, -0.0646, 5000)
end = time.perf_counter()
print(f'Oracle took {end - start:.5f} seconds')

# testing our implementation on production of 20,000 shoes in Melbourne, Australia
start = time.perf_counter()
supply_chain_oracle(materials_four, cities, -0.6599, 2.5302, 20000)
end = time.perf_counter()
print(f'Oracle took {end - start:.5f} seconds')