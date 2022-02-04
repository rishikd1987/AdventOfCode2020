


def read_data():
    with open("sample.txt") as f:
        contents = f.read().splitlines()
    return contents

def main():
    data = read_data()
    print(data)

if __name__ == "__main__":
    main()