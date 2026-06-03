# AI-LCA-CS221
CS 221 Extra Credit Project Keira Cornwell and Kunal Arora

This tool uses UCS and A* search to compute the greenest way to source different materials needed for shoe manufacturing across 30 manufacturing cities based on the assembly site. The data for the greenness, location, and materials manufactured in each location can be found in the cities dictionary in the file. Additionally, the materials and quantities of the main materials needed for shoe manufacturing can be found in the file, split into either the four main materials, five main materials, or ten main materials, based on speed of run needs. If the file is run, it automatically runs all four implementations for finding the best path on the list of four materials. 
To run the baseline, in the file call supply_chain_baseline(materials, cities, lat, long, qty)
To run the UCS, in the file call supply_chain_ucs(materials, cities, lat, long, qty)
To run the A*, in the file call supply_chain_astar(materials, cities, lat, long, qty)
To run the recursive oracle, in the file call supply_chain_oracle(materials, cities, lat, long, qty)
