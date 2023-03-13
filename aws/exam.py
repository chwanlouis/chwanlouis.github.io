import numpy as np
import pandas as pd


def print_question(q: dict):
    print("QUESTION (%s)" % q["q_num"])
    print(q["q_statement"])
    print("(A) %s" % q["A"])
    print("(B) %s" % q["B"])
    print("(C) %s" % q["C"])
    print("(D) %s" % q["D"])
    if "E" in q.keys() and not np.isnan(q["E"]):
        print("(E) %s" % q["E"])
    return


def start_exam(df: pd.DataFrame, n_question: int):
    qs = df.sample(n=n_question).to_dict("records")
    correct_count = 0
    for q in qs:
        print_question(q)
        ans = input("Please enter your answer: ")
        if ans.strip().upper() == q["ans"].strip().upper():
            print("Correct !")
            correct_count += 1
        else:
            print("Wrong, the correct answer is [ %s ]" % q["ans"].strip().upper())
            print("Explanation: %s" % q["explain"])
    print("Result %s / %s" % (correct_count, n_question))
    return


if __name__ == "__main__":
    question_file_name = "aws.csv"
    q_df = pd.read_csv(question_file_name)
    # print(len(q_df))
    # q_df_filtered = q_df.dropna(subset=["q_statement"])
    # print(q_df[q_df["q_statement"].isna() | q_df["A"].isna() | q_df["B"].isna() | q_df["C"].isna() | q_df["D"].isna()
    #       | q_df["ans"].isna()]["q_num"].values)
    start_exam(q_df, n_question=20)
