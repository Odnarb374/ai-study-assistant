from backend.src.input_handler import load_text

def main():
    raw_text = load_text("example.pdf")

    print(raw_text)

if __name__ == "__main__":
    main()