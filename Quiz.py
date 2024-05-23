import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                "question": "O que é a trama de um conto?",
                "options": [
                    "A. O enredo ou sequência de eventos do conto.",
                    "B. O lugar onde a história acontece.",
                    "C. Os sentimentos dos personagens.",
                    "D. A moral da história."
                ],
                "answer": "A"
            },
            {
                "question": "Quem é o narrador em um conto?",
                "options": [
                    "A. O personagem principal.",
                    "B. Quem conta a história.",
                    "C. O vilão da história.",
                    "D. O leitor."
                ],
                "answer": "B"
            },
            {
                "question": "O que é o foco narrativo?",
                "options": [
                    "A. O tema principal do conto.",
                    "B. O ponto de vista através do qual a história é contada.",
                    "C. O desfecho da história.",
                    "D. A época em que a história acontece."
                ],
                "answer": "B"
            },
            {
                "question": "Quem são os personagens em um conto?",
                "options": [
                    "A. Os animais de estimação dos autores.",
                    "B. As pessoas, animais ou seres fictícios que participam da história.",
                    "C. Os leitores do conto.",
                    "D. Os lugares onde a história se passa."
                ],
                "answer": "B"
            },
            {
                "question": "O que é o tempo em um conto?",
                "options": [
                    "A. O clima da história.",
                    "B. A época ou duração em que os eventos do conto acontecem.",
                    "C. A velocidade da narrativa.",
                    "D. A emoção transmitida pela história."
                ],
                "answer": "B"
            },
            {
                "question": "O que é o clímax em um conto?",
                "options": [
                    "A. O início da história.",
                    "B. A parte mais emocionante ou de maior tensão do conto.",
                    "C. A resolução final dos problemas.",
                    "D. A descrição dos personagens."
                ],
                "answer": "B"
            },
            {
                "question": "O que é o desfecho/epílogo em um conto?",
                "options": [
                    "A. O ponto alto da ação.",
                    "B. A conclusão ou finalização da história.",
                    "C. A apresentação dos personagens.",
                    "D. O conflito principal."
                ],
                "answer": "B"
            }
        ]
        self.score = 0

    def start(self):
        print("Bem-vindo ao Jogo de Contos! Vamos começar o quiz.")
        random.shuffle(self.questions)
        for q in self.questions:
            print("\n" + q["question"])
            for option in q["options"]:
                print(option)
            answer = input("Sua resposta (A, B, C ou D): ").strip().upper()
            if answer == q["answer"]:
                print("Correto!")
                self.score += 1
            else:
                print(f"Errado! A resposta correta é {q['answer']}.")

        print(f"\nVocê terminou o quiz! Sua pontuação é {self.score}/{len(self.questions)}.")

if __name__ == "__main__":
    game = QuizGame()
    game.start()
