from PIL import Image, ImageDraw, ImageFont

def draw_layout(sections):
    # Create a blank canvas
    width, height = 800, 600
    img = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(img)

    # Define house center
    house_width, house_height = 200, 150
    house_x = (width - house_width) // 2
    house_y = (height - house_height) // 2

    # Draw house
    draw.rectangle([house_x, house_y, house_x + house_width, house_y + house_height], outline="black", width=3)

    # Draw wings (front left/right)
    wing_w, wing_h = 50, 75
    # Left wing
    draw.rectangle([house_x - wing_w, house_y, house_x, house_y + wing_h], outline="black", width=2)
    # Right wing
    draw.rectangle([house_x + house_width, house_y, house_x + house_width + wing_w, house_y + wing_h], outline="black", width=2)

    # Draw each fence section
    for section in sections:
        name = section['name'].lower()
        length = section['length']
        gate = section['gate']
        gate_pos = section.get('gate_pos', None)

        if name == "left":
            start = (house_x - wing_w, house_y + wing_h)
            end = (house_x - wing_w, house_y + wing_h + length * 3)  # scale ft to pixels
            draw.line([start, end], fill="saddlebrown", width=4)
            draw.text((start[0] - 60, (start[1]+end[1])//2), f"{length} ft", fill="black")

            # Add gate as a gap
            if gate and gate_pos:
                gate_y = start[1] + gate_pos * 3
                draw.line([start, (start[0], gate_y - 5)], fill="white", width=6)
                draw.line([(start[0], gate_y + 5), end], fill="saddlebrown", width=4)

    return img

