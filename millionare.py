from random import shuffle, choice

questions = {1: {'question': "Де ростуть соняхи?",
                 'answers': ['На землі', 'На сонці', 'На небі', 'У воді'],
                 'answer': 'На землі',
                 'scores': 500},
             2: {'question': "На якому материку є лише одна країна?",
                 'answers': ['Австралія', 'Європа', 'Азія', 'Африка'],
                 'answer': 'Австралія',
                 'scores': 1000},
             3: {'question': "Яких грошей не буває?",
                 'answers': ['Льє', 'Гривні', 'Долари', 'Рупії', ],
                 'answer': 'Льє',
                 'scores': 2000
                 },
             4: {'question': "Як називають портрет, написаний з самого себе?",
                 'answers': ["Автопортрет", "Самосвал", "Самопис", "Автограф"],
                 'answer': 'Автопортрет',
                 'scores': 5000
                 },
             5: {'question': "Як називають безпілотний літальний апарат?",
                 'answers': ["Дрон", "Махаон", "Десептикон", "Аніон"],
                 'answer': 'Дрон',
                 'scores': 10000
                 },
             6: {'question': "В якій грі не використовують м'яч?",
                 'answers': ["Керлінг", "Сквош", "Крикет", "Петанк"],
                 'answer': 'Керлінг',
                 'scores': 25000
                 },
             7: {'question': "Який з цих мостів знаходиться в Києві?",
                 'answers': ["Дарницький", "Кримський", "Ріковий", "Ужанський"],
                 'answer': 'Дарницький',
                 'scores': 100000
                 },
             8: {'question': "Хто з цих людей письменник?",
                 'answers': ["Едгар Аллан По", "Жан-Клод Каміль Франсуа Ван Варенберг", "Оскар-Клод Моне",
                             "Енріке Мартін Моралес"],
                 'answer': 'Едгар Аллан По',
                 'scores': 200000
                 },
             9: {'question': "Хто з цих мореплавців відкрив Мис Доброї Надії?",
                 'answers': ["Бартоломеу Діаш", "Жак-Ів Кусто", "Васко да Гама", "Христофор Колумб"],
                 'answer': 'Бартоломеу Діаш',
                 'scores': 500000
                 },
             10: {'question': "Який хімічний елемент отримав назву через синій колір у його спектрі?",
                  'answers': ["Індій", "Родій", "Скандій", "Нептуній"],
                  'answer': 'Індій',
                  'scores': 1000000
                  }}


def get_question(questions, level):
    return f"Питання №{level}: {questions[level]['question']}"


def get_list_answers(questions, level):
    answers = questions[level]["answers"].copy()
    shuffle(answers)
    for idx, answer in enumerate(answers, start=1):
        print(f"{idx}. {answer}")
    return answers


def get_answer():
    alt_answer = [1, 2, 3, 4]
    user_answer = int(input("Введіть варіант відповіді: "))
    while user_answer not in alt_answer:
        print('Такого варіанту відповіді немає!')
        user_answer = int(input("Введіть варіант відповіді: "))
    return user_answer


def true_answer(questions, level, answers, user_answer, guaranteed_scores):
    global continue_game
    q = questions[level]
    current_scores = q["scores"]
    if answers[user_answer - 1] == q['answer']:
        print(f'Ваша відповідь правильна! Ви маєте {current_scores} балів')
    else:
        lose(guaranteed_scores)
        continue_game = False
    if level == 5 or level == 10:
        guaranteed_scores = q["scores"]
    return guaranteed_scores, current_scores, continue_game


def lose(guaranteed_scores):
    print(f"Ви програли! Ваш виграш становить {guaranteed_scores} балів")
    return continue_game


def hints_choice():
    hint_question = input("Хочете використати підказку? ").strip().lower()
    return hint_question


def hint_50_realized(questions, level, answers):
    q = questions[level]
    answers_50 = answers.copy()
    answers=answers_50
    n=0
    while n<2:
        wrong_answer = choice(answers)
        if wrong_answer == q['answer']:
            continue
        elif wrong_answer == "  ":
            continue
        else:
            get_index=answers.index(wrong_answer)
            answers[get_index]="  "
            n+=1
    for idx, answer in enumerate(answers, start=1):
        print(f"{idx}. {answer}")

    return answers


def hint_exp_realized(questions, level, answers):
    q = questions[level]
    answers_exp = answers.copy()
    for i in range (4):
        answers_exp.append(q["answer"])
    shuffle(answers_exp)
    answer_exp = choice(answers_exp)
    print(f'Відповідь знавця: {answer_exp}')
    return answers


def hint_user_input(questions, level, hint_50, hint_exp, answers_50, answers):
    alt_hint=["50 на 50","допомога знавця"]
    while True:
        hint_input = input("Оберіть підказку: ").strip().lower()
        if hint_input not in [h.lower() for h in alt_hint]:
            print("Такої підказки не існує!")
            continue
        if hint_input == "50 на 50":
            hint_50 = False
            new_answers=hint_50_realized(questions, level, answers_50)
            return new_answers, hint_50, hint_exp
        elif hint_input == "допомога знавця":
            hint_exp = False
            hint_exp_realized(questions, level)
            return answers, hint_50, hint_exp


continue_game = True
num_level = 1
available_hint=True
hint_50 = True
hint_exp = True
current_scores = 0
guaranteed_scores = 0

while continue_game and num_level <= 10:
    ques = get_question(questions, num_level)
    print(ques)
    answ_lst = get_list_answers(questions, num_level)
    available_hint = (hint_50 or hint_exp)
    if available_hint:
        print(f"Вам доступні підказки: ")
        if hint_50:
            print(" - 50 на 50")
        if hint_exp:
            print(" - Допомога знавця")
        use_hint = input("Хочете використати підказку? (так/ні): ").strip().lower()
        if use_hint == 'так':
            answ_lst, hint_50, hint_exp = hint_user_input(questions, num_level, hint_50, hint_exp, answ_lst)
    answ = get_answer()
    guaranteed_scores, current_scores, continue_game = true_answer(questions, num_level, answ_lst, answ,
                                                                   guaranteed_scores)
    if num_level == 10:
        print(f'Вітаю! Ви переможець гри! Ваш супер приз {guaranteed_scores} балів')
    num_level += 1
    if not continue_game:
        break
