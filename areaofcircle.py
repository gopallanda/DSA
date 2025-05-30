import math

radius = float(input("enter radius of a circle:"))
area = math.pi * radius * radius
cr = 2 * (math.pi * radius)

# Calculate area and circumference
print(f"\nCircle Details:")
print(f"Radius: {radius:.2f} units")
print(f"Area: {area:.2f} square units") 
print(f"Circumference: {cr:.2f} units")

# Additional circle properties
diameter = 2 * radius
print(f"Diameter: {diameter:.2f} units")

# Calculate sector and arc properties
angle = float(input("\nEnter angle in degrees for sector calculations: "))
sector_area = (angle/360) * math.pi * radius * radius
arc_length = (angle/360) * 2 * math.pi * radius

print(f"\nSector and Arc Properties (for {angle}°):")
print(f"Sector Area: {sector_area:.2f} square units")
print(f"Arc Length: {arc_length:.2f} units")

# Calculate inscribed and circumscribed shapes
inscribed_square_area = 2 * radius * radius
circumscribed_square_area = 4 * radius * radius
inscribed_triangle_area = (3**0.5/4) * radius * radius

print(f"\nInscribed and Circumscribed Shapes:")
print(f"Inscribed Square Area: {inscribed_square_area:.2f} square units")
print(f"Circumscribed Square Area: {circumscribed_square_area:.2f} square units") 
print(f"Inscribed Regular Triangle Area: {inscribed_triangle_area:.2f} square units")

# Circle ratios and relationships
area_to_circumference = area/cr
print(f"\nRelationships:")
print(f"Area to Circumference Ratio: {area_to_circumference:.2f}")
print(f"Area to Radius² Ratio (π): {(area/(radius*radius)):.2f}")
