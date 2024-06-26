def main():
    stages = [
        "ардипитеков",
        "Австралопитеки",
        "Парантропы",
        "Человек умелый",
        "Человек прямоходящий",
        "Гейдельбергский человек",
        "Человек флоресский",
        "Неандертальцы",
        "Человек разумный"
    ]
    
    answers = []
    
    print("Привет! Давай проверим твои знания по стадиям развития человека.")
    
    for stage in stages:
        answer = input(f"Введите следующую стадию развития (Текущая стадия: {stage}): ")
        answers.append(answer)
    
    print("Результаты теста:")
    print(" => ".join(answers))

if __name__ == "__main__":
    main()
