indian = ["Butter Chicken", "Palak Paneer", "Chole Bhature", "Biryani", "Masala Dosa"]
italian = ["Margherita Pizza", "Pasta Carbonara", "Lasagna"]
chinese = ["Kung Pao Chicken", "Sweet and Sour Pork", "Dumplings", "Fried Rice", "Spring Rolls"]

dish = input("Enter a dish name: ")
if dish in indian:
    print(f"{dish} is indian cuisine.")
elif dish in italian:
    print(f"{dish} is italian cuisine.")
elif dish in chinese:
    print(f"{dish} is chinese cuisine.")
else:
    print(f"{dish} cuisine is unknown.")
