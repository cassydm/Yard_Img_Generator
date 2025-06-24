from drawing import draw_layout

def get_user_input():
    sections = []

    print("Add a fence section:")
    while True:
        name = input("Section name (left/right/back/front or 'done'): ").strip().lower()
        if name == "done":
            break

        length = float(input(f"Enter length of {name} section in feet: "))
        gate = input("Add gate? (y/n): ").strip().lower() == "y"
        gate_pos = None

        if gate:
            gate_pos = float(input("Gate distance from start of section (in feet): "))

        sections.append({
            "name": name,
            "length": length,
            "gate": gate,
            "gate_pos": gate_pos
        })

    return sections

if __name__ == "__main__":
    sections = get_user_input()
    image = draw_layout(sections)
    image.save("fence_layout.png")
    image.show()
