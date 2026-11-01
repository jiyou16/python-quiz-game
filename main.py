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


def get_default_quizzes():
    """기본 퀴즈 목록(리눅스 & Docker 기초)을 Quiz 객체 리스트로 반환"""
    return [
        Quiz(
            "현재 작업 중인 디렉터리의 절대 경로를 출력하는 명령어는?",
            ["ls", "cd", "pwd", "mkdir"],
            3,
        ),
        Quiz(
            "숨김 파일까지 포함해 자세한 목록을 보는 명령어는?",
            ["ls", "ls -l", "ls -la", "ls -d"],
            3,
        ),
        Quiz(
            "내용이 없는 빈 파일을 만드는 명령어는?",
            ["mkdir", "touch", "cat", "echo"],
            2,
        ),
        Quiz(
            "chmod 755를 적용한 결과 권한 문자열은?",
            ["rwxr-xr-x", "rw-r--r--", "rwx------", "rw-------"],
            1,
        ),
        Quiz(
            "rmdir 명령어로 삭제할 수 있는 것은?",
            ["모든 파일", "빈 디렉터리", "내용이 있는 디렉터리", "숨김 파일"],
            2,
        ),
        Quiz(
            "실행 중인 컨테이너에 새 셸을 열고, 나와도 컨테이너가 계속 실행되는 명령어는?",
            ["docker attach", "docker exec", "docker run", "docker logs"],
            2,
        ),
        Quiz(
            "docker run -p 8080:80 에서 8080은 무엇인가?",
            ["컨테이너 포트", "호스트 포트", "이미지 버전", "프로세스 ID"],
            2,
        ),
        Quiz(
            "컨테이너를 삭제해도 데이터가 남도록 Docker가 관리하는 저장 공간은?",
            ["이미지", "레이어", "볼륨", "태그"],
            3,
        ),
    ]


def ask_number(prompt, min_value, max_value):
    """min_value~max_value 범위의 정수를 입력받을 때까지 반복"""
    while True:
        raw = input(prompt).strip()

        if raw == "":
            print("입력이 비어 있습니다. 숫자를 입력해 주세요.")
            continue

        try:
            number = int(raw)
        except ValueError:
            print("숫자만 입력해 주세요.")
            continue

        if number < min_value or number > max_value:
            print(f"{min_value}~{max_value} 사이의 숫자를 입력해 주세요.")
            continue

        return number


class QuizGame:
    """퀴즈 게임 전체(메뉴, 진행, 데이터)를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = get_default_quizzes()  # 퀴즈 목록 (Quiz 객체 리스트)
        self.best_score = None                # 최고 점수 (아직 안 풀었으면 None)

    def show_menu(self):
        """메뉴 출력"""
        print("\n========== 리눅스 & Docker 퀴즈 ==========")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("==========================================")

    def play_quiz(self):
        """퀴즈를 순서대로 출제하고 맞힌 개수를 반환"""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해 주세요.")
            return None

        total = len(self.quizzes)
        print(f"\n=== 퀴즈를 시작합니다! (총 {total}문제) ===")

        score = 0
        for i, quiz in enumerate(self.quizzes, start=1):
            quiz.display(i)
            user_answer = ask_number("정답 번호를 입력하세요 (1-4): ", 1, 4)

            if quiz.is_correct(user_answer):
                print("⭕ 정답입니다!")
                score += 1
            else:
                correct_text = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({correct_text})입니다.")

        print(f"\n=== 결과: {total}문제 중 {score}문제 정답! ({score * 100 // total}점) ===")
        return score

    def add_quiz(self):
        print("\n[퀴즈 추가] 준비 중입니다.")

    def show_quiz_list(self):
        print("\n[퀴즈 목록] 준비 중입니다.")

    def show_best_score(self):
        print("\n[점수 확인] 준비 중입니다.")

    def run(self):
        """메뉴 반복 실행"""
        while True:
            self.show_menu()
            choice = ask_number("메뉴를 선택하세요 (1-5): ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_best_score()
            else:
                print("게임을 종료합니다. 안녕히 가세요!")
                break


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 프로그램을 안전하게 종료합니다.")