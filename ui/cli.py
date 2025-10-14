from calculator import calculate
from calculator.utils.angle_modes import angle_mode

def run_cli():
    """Run the calculator in command-line mode"""
    print("Scientific Calculator")
    print("Commands:")
    print("  'deg' or 'rad' - Switch angle mode")
    print("  'mode' - Show current angle mode")
    print("  'quit' or 'exit' - Close calculator")
    print("=" * 40)
    print(f"Current mode: {angle_mode.get_mode()}")
    
    while True:
        try:
            expression = input("\n>>> ")
            
            # Handle exit commands
            if expression.lower() in ['quit', 'exit']:
                print("Goodbye!")
                break
            
            # Handle empty input
            if expression.strip() == "":
                continue
            
            # Handle mode change commands
            if expression.lower() == 'deg':
                angle_mode.set_mode('DEG')
                print(f"Mode set to: DEGREES")
                continue
            
            if expression.lower() == 'rad':
                angle_mode.set_mode('RAD')
                print(f"Mode set to: RADIANS")
                continue
            
            if expression.lower() == 'mode':
                print(f"Current mode: {angle_mode.get_mode()}")
                continue
            
            # Calculate expression
            result = calculate(expression)
            print(f"= {result}")
        
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_cli()