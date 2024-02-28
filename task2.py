def main():
    print("\nSelect your choise what you need to get\n")
    print(f"1. Speed\n"
          f"2. Distance\n"
          f"3. time")
    selected_mode = choise()
    if selected_mode == "1":
        distance = numChecker("Give the Distance: ")
        time = numChecker("Give the Time: ")
        print(get_speed(distance,time))
    elif selected_mode == "2":
        speed = numChecker("Give the Speed:")
        time = numChecker("Give the Time: ")
        print(get_distance(speed,time))
    elif selected_mode == "3":
        speed = numChecker("Give the Speed: ")
        distance = numChecker("Give the Distance: ")
        print(get_time(distance,speed))


def choise():
    choises = ["1", "2", "3"]
    while True:
        user = input("Select your choise 1,2,3 ")
        if user in choises:
            return user


def numChecker(question):
    while True:
        user = input(question)
        if user.isdigit():
            return int(user)


def get_speed(distance, time):
    return distance/time


def get_time(distance, speed):
    return distance / speed


def get_distance(speed, time):
    return speed * time


if __name__=="__main__":
    main()
