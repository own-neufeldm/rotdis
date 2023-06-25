import myscreen.display


def main() -> None:
    display = myscreen.display.get_primary_display()
    rotation = display.get_rotation()
    if rotation == 0:
        display.set_rotation(90)
    elif rotation == 90:
        display.set_rotation(0)
    return None


if __name__ == "__main__":
    main()
