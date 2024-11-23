question = input("what is the capital of france?")
if question.lower().strip() in {"paris"}:
    print("answer is correct!")
else:
    print("answer is wrong!")