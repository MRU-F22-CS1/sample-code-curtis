def dms(coord: float) -> str:
    """
    Converts a coordinate in degrees to D:M:S, 
    then returns a formatted string.
    """
    degrees = int(coord) # coord // 1
    minutes = int(coord % 1 * 60) # (degrees - coord) * 60
    seconds = (coord - minutes / 60) % 1 * 3600
    return f"{degrees}° {minutes}' {seconds:.2f}\""

def main():
    lat = 51.013760
    long = 114.133691
    print(f"{dms(lat)} N, {dms(long)} W")

main()