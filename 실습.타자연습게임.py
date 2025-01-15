import random,  string, time

def random_word(length=5):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def ty_game():
    print("=== 영어 타자 연습 게임 ===")
    print("게임 시작! '종료료'을 입력하면 종료됩니다.")
    print("==========================")
    
    total_words = 0
    start_time = time.time()
    
    while True:
        word_length = random.randint(2, 10) 
        word = random_word(word_length)
        print(f"단어: {word}")
        
        while True:
            user_input = input("입력: ").strip()
            
            if user_input.lower() == "종료":
                end_time = time.time()
                elapsed_time = end_time - start_time
                #미세하게 측정하고 싶다면
                #end_time = time.perf_counter()
                #elapsd_time = end_time - start_time.per
                average_time = elapsed_time / total_words if total_words > 0 else 0
                print("게임 종료!")
                print(f"총 {total_words}개의 단어를 입력하셨습니다.")
                print(f"총 걸린 시간: {elapsed_time:.2f}초")
                print(f"평균 단어당 입력 시간: {average_time:.2f}초")
                return
            
            if user_input == word:
                print("통과!")
                total_words += 1
                break
            else:
                print("오타! 다시 시도하세요.")

ty_game()