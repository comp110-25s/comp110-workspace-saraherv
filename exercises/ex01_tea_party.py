"""Tea party for 333 of my friends and myself!"""

__author__: str = "730485927"


def main_planner(guests: int) -> None:
    """Call and produce other functions"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))
        )
    )


def tea_bags(people: int) -> int:
    """Amount of tea bags needed per person"""
    return 2 * people


def treats(people: int) -> int:
    """Amount of treats needed per person"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Total cost of tea and treats"""
    return tea_count * 0.50 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
