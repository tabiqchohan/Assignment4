def main():
    
    
    side1 = float(input("\033[1;3mEnter the length of side 1:\033[0m"))
    side2 = float(input("\033[1;3mEnter the length of side2:\033[0m"))
    side3 = float(input("\033[1;3mEnter the length of side3:\033[0m"))
    
    
    perimeter = side1 + side2 + side3
    
    
    print(f"The perimeter of the triangle is {perimeter}")
    
    
    
if __name__ == "__main__":
    main()