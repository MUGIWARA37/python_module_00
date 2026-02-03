def ft_count_harvest_recursive() -> None:
    def recure(days) -> None:
        if not days:
            return
        recure(days - 1)
        print("Day ", days)
        return
    days = int(input("Days until harvest:"))
    recure(days)
    print("Harvest time!")
