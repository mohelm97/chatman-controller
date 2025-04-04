import argparse
from chatman_controller import ChatmanController, EyeMovement, HandMovement, AntennaMovement

def get_enum_input(enum_class):
    print(f"\nChoose {enum_class.__name__}:")
    for item in enum_class:
        print(f"{item.value}: {item.name}")
    while True:
        try:
            return enum_class(int(input("Enter value: ")))
        except (ValueError, KeyError):
            print("Invalid input, try again.")

def get_face_led_input():
    print("Enter 3 hex values for face LED (e.g. FF, 00, AA):")
    result = []
    for i in range(3):
        while True:
            try:
                val = input(f"Byte {i+1}: ").strip()
                result.append(int(val, 16))
                break
            except ValueError:
                print("Invalid hex. Try again.")
    return result

def interactive_mode(controller):
    print("\nEntering Interactive Mode...")
    while True:
        eye = get_enum_input(EyeMovement)
        hand = get_enum_input(HandMovement)
        antenna = get_enum_input(AntennaMovement)
        leds = get_face_led_input()
        controller.move(eye, hand, antenna, leds)

def main():
    parser = argparse.ArgumentParser(description="Chatman USB Toy CLI Controller")
    parser.add_argument("--eyes", type=str, choices=[e.name for e in EyeMovement], help="Eye movement")
    parser.add_argument("--hands", type=str, choices=[e.name for e in HandMovement], help="Hand movement")
    parser.add_argument("--antenna", type=str, choices=[e.name for e in AntennaMovement], help="Antenna movement")
    parser.add_argument("--leds", nargs=3, type=lambda x: int(x, 16), help="LED values in hex (e.g. FF 00 AA)")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    parser.add_argument("--no-reset", action="store_true", help="Don't reset Chatman on start")

    args = parser.parse_args()

    try:
        controller = ChatmanController(reset=not args.no_reset)
    except Exception as e:
        print(f"Failed to initialize ChatmanController: {e}")
        return

    if args.interactive or (not args.eyes and not args.hands and not args.antenna and not args.leds):
        interactive_mode(controller)
    else:
        try:
            eye = EyeMovement[args.eyes] if args.eyes else EyeMovement.NO_MOVEMENT
            hand = HandMovement[args.hands] if args.hands else HandMovement.NO_MOVEMENT
            antenna = AntennaMovement[args.antenna] if args.antenna else AntennaMovement.NO_MOVEMENT
            leds = args.leds if args.leds else [0x00, 0x00, 0x00]
            controller.move(eye, hand, antenna, leds)
        except KeyError as e:
            print(f"Invalid movement value: {e}")
        except Exception as e:
            print(f"Failed to send command to Chatman: {e}")

if __name__ == "__main__":
    main()
