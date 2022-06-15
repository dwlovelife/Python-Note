def main():
    set1 = {1, 2, 3, 4, 2, 2, 6}
    print(set1)
    print(len(set1))
    set2 = set(range(1, 3))
    print(set2)
    set1.add(11)
    set2.update({1,6,7,12})
    print(set2)
    set2.discard(1)
    print(set2)
    if 4 in set2:
        set2.remove(4)
    print(set2)
    print(set2.pop())
    set3 = {1, 2, True}
    print(set3.pop())


if __name__ == "__main__":
    main()
