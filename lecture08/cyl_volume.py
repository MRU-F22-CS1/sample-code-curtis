import math

def volume_cyl(rad: float, height: float) -> float:
    vol = math.pi * rad**2 * height
    return vol

def main() -> None:
    r = 7
    h = 20
    # v = volume_cyl(r, h)
    print(f"Volume: {volume_cyl(r, h):.1f}")

main()