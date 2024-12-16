def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort packages into different stacks based on their dimensions and mass.
    
    Args:
        width (float): Width of the package in centimeters
        height (float): Height of the package in centimeters
        length (float): Length of the package in centimeters
        mass (float): Mass of the package in kilograms
        
    Returns:
        str: Stack designation ('STANDARD', 'SPECIAL', or 'REJECTED')
    
    Rules:
        - Bulky: volume ≥ 1,000,000 cm³ or any dimension ≥ 150 cm
        - Heavy: mass ≥ 20 kg
        - Standard: neither bulky nor heavy
        - Special: either bulky or heavy (but not both)
        - Rejected: both bulky and heavy
    """
    # Input validation
    if any(dim <= 0 for dim in [width, height, length, mass]):
        raise ValueError("All dimensions and mass must be positive numbers")

    # Check if package is bulky
    volume = width * height * length
    is_bulky = volume >= 1_000_000 or max(width, height, length) >= 150

    # Check if package is heavy
    is_heavy = mass >= 20

    # Determine the appropriate stack
    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"

def get_valid_float_input(prompt: str) -> float:
    """Helper function to get valid float input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Welcome to the Package Sorting System!")
    print("\nPlease enter package dimensions (in centimeters) and mass (in kilograms):")
    
    while True:
        try:
            width = get_valid_float_input("Width (cm): ")
            height = get_valid_float_input("Height (cm): ")
            length = get_valid_float_input("Length (cm): ")
            mass = get_valid_float_input("Mass (kg): ")

            result = sort(width, height, length, mass)
            
            # Calculate and display additional information
            volume = width * height * length
            print("\nPackage Analysis:")
            print(f"Volume: {volume:,.2f} cm³")
            print(f"Largest dimension: {max(width, height, length):.2f} cm")
            print(f"Mass: {mass:.2f} kg")
            print(f"\nSort Result: {result}")
            
            # Ask if user wants to sort another package
            again = input("\nWould you like to sort another package? (yes/no): ").lower()
            if again != 'yes' and again != 'y':
                print("Thank you for using the Package Sorting System!")
                break
            print("\n" + "="*50 + "\n")
            
        except ValueError as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
