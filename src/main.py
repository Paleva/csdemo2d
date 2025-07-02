import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    argument = sys.argv[1]
    print(f"Argument received: {argument}")


if __name__ == "__main__":
    main()