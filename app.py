import json


def main():

    while True:

        with open("Scientists.json", "r") as f:
            info = json.load(f)

        select = str(input("\nEnter a name: "))

        in_list = False

        for scientist in info["scientists"]:
            if scientist["name"] == select:
                print("Name: {}\t Birthday: {}".format(
                    scientist["name"],
                    scientist["birthday"]))
                in_list = True
                break
            else:
                continue

        if in_list is False:

            add = str(input(f"{select} isn't in this list (Type 'Add', to add {select})"))

            if add == 'Add':

                date = str(input("Please enter the Birthday as follows - dd/mm/yyyy"))

                with open("Scientists.json", "w") as f:
                    info["scientists"].append({"name": select, "birthday": date})
                    json.dump(info, f, indent=2)


if __name__ == '__main__':
    main()
