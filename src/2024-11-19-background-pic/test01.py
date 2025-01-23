from PIL import ImageDraw, Image

# Create a new abstract background
abstract_bg = Image.new("RGB", (width, height), (255, 255, 255))  # Start with a white background
draw = ImageDraw.Draw(abstract_bg)

# Define colors from the logo
teal = (3, 131, 117)
orange = (255, 140, 0)
black = (0, 0, 0)

# Add hexagonal patterns similar to the logo
center_x, center_y = width // 2, height // 2
hex_radius = 300

# Function to draw a hexagon
def draw_hexagon(draw, x, y, radius, color, thickness=5):
    angle = 60
    points = [
        (x + radius * np.cos(np.radians(angle * i)), y + radius * np.sin(np.radians(angle * i)))
        for i in range(6)
    ]
    points.append(points[0])  # Close the hexagon
    draw.line(points, fill=color, width=thickness)

# Draw multiple hexagons with varying sizes and colors
for i in range(1, 6):
    draw_hexagon(draw, center_x, center_y, hex_radius - i * 50, teal if i % 2 == 0 else black, thickness=10)

# Add circles at the vertex points of the largest hexagon
for i in range(6):
    angle = 60 * i
    x = center_x + hex_radius * np.cos(np.radians(angle))
    y = center_y + hex_radius * np.sin(np.radians(angle))
    draw.ellipse([x - 20, y - 20, x + 20, y + 20], fill=orange)

# Add lines connecting the center to the vertices
for i in range(6):
    angle = 60 * i
    x = center_x + hex_radius * np.cos(np.radians(angle))
    y = center_y + hex_radius * np.sin(np.radians(angle))
    draw.line([(center_x, center_y), (x, y)], fill=black, width=5)

# Save the abstract background
abstract_path = "/mnt/data/abstract_background_teal.png"
abstract_bg.save(abstract_path)

abstract_path


# Create additional examples of abstract hexagonal backgrounds

def generate_hexagon_background(radius_step=50, circle_radius=15, colors=None):
    """Generate an abstract background with hexagonal patterns."""
    bg = Image.new("RGB", (width, height), (255, 255, 255))  # White background
    draw = ImageDraw.Draw(bg)
    center_x, center_y = width // 2, height // 2
    hex_radius = 300  # Starting radius for hexagon patterns
    
    if colors is None:
        colors = [teal, orange, black]
    
    # Draw concentric hexagons
    for i in range(6):
        radius = hex_radius - i * radius_step
        color = colors[i % len(colors)]
        draw_hexagon(draw, center_x, center_y, radius, color, thickness=8)

    # Add accent circles at vertices of the largest hexagon
    for i in range(6):
        angle = 60 * i
        x = center_x + hex_radius * np.cos(np.radians(angle))
        y = center_y + hex_radius * np.sin(np.radians(angle))
        draw.ellipse([x - circle_radius, y - circle_radius, x + circle_radius, y + circle_radius], fill=colors[i % len(colors)])

    return bg

# Create three different variations
background_variations = []
for i, step in enumerate([40, 60, 80]):
    variation = generate_hexagon_background(radius_step=step, circle_radius=10 + i * 5, colors=[teal, black, orange])
    path = f"/mnt/data/hexagon_background_variation_{i + 1}.png"
    variation.save(path)
    background_variations.append(path)

background_variations





def create_hexagonal_grid(image_size, hex_radius, colors, blur_radius=10):
    """
    Create a hexagonal grid and blur it for an abstract background.
    
    Args:
    - image_size: Tuple, size of the image (width, height).
    - hex_radius: Radius of individual hexagons.
    - colors: List of colors to alternate hexagons.
    - blur_radius: Radius for Gaussian blur.
    
    Returns:
    - Blurred hexagonal grid image.
    """
    width, height = image_size
    bg = Image.new("RGB", image_size, (255, 255, 255))  # Start with white background
    draw = ImageDraw.Draw(bg)
    
    # Calculate hexagon dimensions
    hex_height = int(np.sqrt(3) * hex_radius)
    hex_width = 2 * hex_radius
    vert_dist = hex_height
    horiz_dist = int(3/2 * hex_radius)
    
    # Draw hexagons in a grid pattern
    for row in range(0, height + hex_height, vert_dist):
        for col in range(0, width + hex_width, horiz_dist):
            offset_x = col + (hex_radius if (row // vert_dist) % 2 else 0)
            offset_y = row
            hex_color = colors[(row // vert_dist + col // horiz_dist) % len(colors)]
            draw_hexagon(draw, offset_x, offset_y, hex_radius, hex_color, thickness=0)
    
    # Apply Gaussian blur for a soft effect
    blurred_bg = bg.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    return blurred_bg

# Define the size and colors for the grid
hex_grid_size = (1920, 1080)
hex_radius = 50
grid_colors = [teal, orange, black]

# Create the hexagonal grid background with blur
hex_grid_bg = create_hexagonal_grid(hex_grid_size, hex_radius, grid_colors, blur_radius=15)

# Save the blurred hexagonal grid background
hex_grid_path = "/mnt/data/blurred_hexagonal_grid_background.png"
hex_grid_bg.save(hex_grid_path)

hex_grid_path

