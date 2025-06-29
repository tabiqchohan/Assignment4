def maain():
    
    farenheit = float(input("\033[1;3mEnter the temperature in farenheit:\033[0m"))
    
    
    celsius = (farenheit - 32) * 5.0/9.0
    
    
    print(f"temperature : {farenheit}f = {celsius}C")
    
    
    
if __name__ =="__main__":
    maain()