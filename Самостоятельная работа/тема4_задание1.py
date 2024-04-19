def calculate_rectangle_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def main():
    length = float(input("Введите длину прямоугольника: "))
    width = float(input("Введите ширину прямоугольника: "))

    area, perimeter = calculate_rectangle_properties(length, width)

    print("Площадь прямоугольника:", area)
    print("Периметр прямоугольника:", perimeter)

if __name__ == "__main__":
    main()
