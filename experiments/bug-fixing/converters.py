def converter(feet, inches):
    feet_to_inches = int(feet) * 12
    inches = feet_to_inches + int(inches)
    meters = inches * 0.0254
    return meters
