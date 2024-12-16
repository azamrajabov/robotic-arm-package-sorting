# Package Sorting System Documentation

## Overview
The Package Sorting System is designed for Thoughtful's robotic automation factory to efficiently sort packages into appropriate stacks based on their dimensions and mass. This document outlines the system's rules, implementation details, and usage instructions.

## Rules and Criteria

### Package Classifications
* **Bulky Package**
  - Volume (Width × Height × Length) ≥ 1,000,000 cm³, OR
  - Any single dimension ≥ 150 cm

* **Heavy Package**
  - Mass ≥ 20 kg

### Sorting Categories
1. **STANDARD**
   - Packages that are neither bulky nor heavy
   - Can be handled normally by automated systems

2. **SPECIAL**
   - Packages that are either bulky OR heavy (but not both)
   - Require special handling procedures

3. **REJECTED**
   - Packages that are BOTH bulky AND heavy
   - Cannot be processed through the system

## Implementation

### File Structure
The system consists of two Python files:
```
package_sorter.py      # Main program with sorting logic
test_package_sorter.py # Unit tests
```

### Installation
1. Create a new directory for the project
2. Download both Python files into the directory
3. Ensure Python 3.x is installed on your system

### Running the Program

#### Interactive Mode
To use the interactive package sorting system:
```bash
python package_sorter.py
```

#### Running Tests
To execute the unit tests:
```bash
python test_package_sorter.py
```

## Usage Guide

### Interactive Mode
1. Start the program
2. Enter package dimensions when prompted:
   - Width (in centimeters)
   - Height (in centimeters)
   - Length (in centimeters)
   - Mass (in kilograms)
3. Review the analysis results:
   - Package volume
   - Largest dimension
   - Mass
   - Sort result (STANDARD/SPECIAL/REJECTED)
4. Choose to sort another package or exit

### Input Requirements
- All measurements must be positive numbers
- Dimensions must be in centimeters
- Mass must be in kilograms
- Decimal values are accepted

### Example Session
```
Welcome to the Package Sorting System!

Please enter package dimensions (in centimeters) and mass (in kilograms):
Width (cm): 100
Height (cm): 100
Length (cm): 100
Mass (kg): 15

Package Analysis:
Volume: 1,000,000.00 cm³
Largest dimension: 100.00 cm
Mass: 15.00 kg

Sort Result: SPECIAL

Would you like to sort another package? (yes/no):
```

## Testing

### Test Coverage
The unit tests cover:
- Standard packages
- Bulky packages
- Heavy packages
- Rejected packages
- Edge cases
- Invalid inputs

### Running Custom Tests
To add custom test cases:
1. Open `test_package_sorter.py`
2. Add new test methods to the `TestPackageSorter` class
3. Run the tests to verify functionality

## Error Handling
The system includes robust error handling for:
- Invalid numeric inputs
- Negative values
- Zero values
- Non-numeric inputs

## Support
For additional support or to report issues:
1. Check the existing test cases for examples
2. Review the error messages for specific input problems
3. Verify that all inputs meet the specified requirements
