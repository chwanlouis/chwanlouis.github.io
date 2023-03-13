import pandas as pd


def file_reader(file_name) -> list:
    output_list = list()
    is_q = False
    is_a = False
    is_b = False
    is_c = False
    is_d = False
    is_e = False
    is_ans = False
    is_explain = False
    line_count = 0
    with open(file_name, 'r') as file:
        question = dict()
        q_statement = ""
        e_statement = ""
        for line in file:
            try:
                line_count += 1
                line = line.replace("\r", "").replace("\n", "")
                if "QUESTION" in line:
                    if len(e_statement) > 0:
                        question["explain"] = e_statement
                        e_statement = ""
                    if len(question) > 0:
                        output_list.append(question)
                        question = dict()
                    _, q_num = line.split(" ")
                    question["q_num"] = q_num
                    is_q = True
                elif is_q and "A." not in line:
                    q_statement += line
                elif is_q and "A." in line.upper():
                    # collect the question
                    question["q_statement"] = q_statement
                    q_statement = ""
                    is_q = False
                    # get option A
                    question["A"] = line.replace("A.", "")
                    is_a = True
                elif is_a and "B." in line.upper():
                    is_a = False
                    question["B"] = line.replace("B.", "")
                    is_b = True
                elif is_b and "C." in line.upper():
                    is_b = False
                    question["C"] = line.replace("C.", "")
                    is_c = True
                elif is_c and "D." in line.upper():
                    is_c = False
                    question["D"] = line.replace("D.", "")
                    is_d = True
                elif is_d and "E." in line.upper():
                    is_d = False
                    question["E"] = line.replace("E.", "")
                    is_e = True
                elif (is_d or is_e) and "Answer:" in line:
                    is_d = False
                    is_e = False
                    question["ans"] = line.replace("Answer:", "")
                    is_ans = True
                elif is_ans and "Explanation:" in line:
                    is_ans = False
                    e_statement += line.replace("Explanation:", "")
                    is_explain = True
                elif is_explain and "QUESTION" not in line:
                    e_statement += line
                else:
                    raise ValueError
            except ValueError as e:
                print(e)
                print("File Reading Error at line %s" % line_count)
                return
    if len(e_statement) > 0:
        question["explain"] = e_statement
    if len(question) > 0:
        output_list.append(question)
    return output_list


if __name__ == "__main__":
    file_name = "aws.txt"
    output_file_name = "aws.csv"
    question_list = file_reader(file_name)
    question_df = pd.DataFrame(question_list)
    question_df.to_csv(output_file_name, index=False)