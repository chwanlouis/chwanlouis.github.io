import os
import random
# import numpy as np
import pandas as pd
from typing import List


def print_question(q: dict, q_no: int):
    print("QUESTION %s (database id: %s)" % (q_no, q["q_num"]))
    print(q["q_statement"])
    print("")
    print("(A) %s" % q["A"])
    print("(B) %s" % q["B"])
    print("(C) %s" % q["C"])
    print("(D) %s" % q["D"])
    if "E" in q.keys() and type(q['E']) == str:
        print("(E) %s" % q["E"])
    print("")
    return


def start_exam(df: pd.DataFrame, n_question: int, revise_question: List[int]):
    qs = df.sample(n=n_question).to_dict("records")
    rqs = df[df["q_num"].isin(revise_question)].to_dict("records")
    qs = qs + rqs
    random.shuffle(qs)
    correct_count = 0
    count = 1
    for q in qs:
        os.system('cls')
        print_question(q, count)
        ans = input("Please enter your answer: ")
        if ans.strip().upper() == q["ans"].strip().upper():
            print("Make it correct is your responsibility")
            correct_count += 1
        else:
            print("Wrong you idiot, the correct answer is [ %s ]" % q["ans"].strip().upper())
            print("Explanation: %s" % q["explain"])
        print("")
        _ = input("Press any key to continue ...")
        count += 1
    print("Result %s / %s" % (correct_count, n_question))
    return


if __name__ == "__main__":
    question_file_name = "aws.csv"
    q_df = pd.read_csv(question_file_name)
    revise_question = [92, 213, 712]
    start_exam(q_df, n_question=20, revise_question=revise_question)
