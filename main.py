from pyscript import document, display


def checkNum(e):

    num_bers = [1, 2, 3, 4, 5]

    num1 = int(document.getElementById("num1").value)
    name = "Rocky"

    confirm_num = num1 in num_bers

    message = (f"Sorry {name}, number is not found", f"Yey! {name}, your number is found!")

    document.getElementById("output1").innerHTML = message[confirm_num]