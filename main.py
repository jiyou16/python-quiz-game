class Quiz:
    """퀴즈 한 문제를 나타내는 클래스"""

    def __init__(self, question, choices, answer):
        self.question = question  # 문제 (str)
        self.choices = choices    # 선택지 4개 (list[str])
        self.answer = answer      # 정답 번호 1~4 (int)

    def display(self, number=None):
        """문제와 선택지를 화면에 출력"""
        if number is None:
            print(f"\n{self.question}")
        else:
            print(f"\n[문제 {number}] {self.question}")

        for i, choice in enumerate(self.choices, start=1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_answer):
        """사용자 답(1~4)이 정답인지 True/False로 반환"""
        return user_answer == self.answer
def ask_number(prompt, min_value, max_value):
    """숫자를 입력받아 min_value~max_value 범위면 int로 반환. 아니면 다시 묻는다."""
    while True:
        raw = input(prompt).strip()          # 앞뒤 공백 제거
        if raw == "":
            print("입력이 비어 있습니다. 숫자를 입력해 주세요.")
            continue
        try:
            number = int(raw)
        except ValueError:
            print(f"'{raw}'은(는) 숫자가 아닙니다. 다시 입력해 주세요.")
            continue
        if number < min_value or number > max_value:
            print(f"{min_value}~{max_value} 사이의 번호를 입력해 주세요.")
            continue
        return number


def show_menu():
    print()
    print("========== 파이썬 퀴즈 게임 ==========")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=====================================")


def main():
    while True:
        show_menu()
        choice = ask_number("메뉴를 선택하세요: ", 1, 5)
        if choice == 1:
            print("[퀴즈 풀기] 준비 중입니다.")
        elif choice == 2:
            print("[퀴즈 추가] 준비 중입니다.")
        elif choice == 3:
            print("[퀴즈 목록] 준비 중입니다.")
        elif choice == 4:
            print("[점수 확인] 준비 중입니다.")
        else:
            print("게임을 종료합니다. 안녕히 가세요!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.") 