
def main():
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)


if __name__ == "__main__":
    main()