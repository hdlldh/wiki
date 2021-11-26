from utils import *


def test_ascii_or_emoji_only():
    successful_cases = 0
    failed_cases = []

    test_cases = [
        {"name": "default_check", "input": "This is an English!", "expected": True},
        {"name": "chinese_check", "input": "你好", "expected": False},
        {"name": "emoji_check", "input": "😃", "expected": True},
    ]

    for test_case in test_cases:
        result = ascii_or_emoji_only(test_case["input"])

        try:
            assert result == test_case["expected"]
            successful_cases += 1
        except:
            failed_cases.append(
                {
                    "name": test_case["name"],
                    "expected": test_case["expected"],
                    "got": result,
                }
            )
            print(
                f"Wrong output from ascii_or_emoji_only function. \n\t Name: {failed_cases[-1].get('name')}. \n\tExpected: {failed_cases[-1].get('expected')}.\n\tGot: {failed_cases[-1].get('got')}."
            )

    if len(failed_cases) == 0:
        print("\033[92m All tests passed")
    else:
        print("\033[92m", successful_cases, " Tests passed")
        print("\033[91m", len(failed_cases), " Tests failed")


def test_tokenize_sentence():
    successful_cases = 0
    failed_cases = []

    test_cases = [
        {"name": "default_check", "input": "This is an English!", "expected": ['this', 'is', 'an', 'english', '!']},
        {"name": "colon_check", "input": "Category:18th-century French painters",
         "expected": ['category', '18th', 'century', 'french', 'painters']},
    ]

    for test_case in test_cases:
        result = tokenize_sentence(test_case["input"])

        try:
            assert result == test_case["expected"]
            successful_cases += 1
        except:
            failed_cases.append(
                {
                    "name": test_case["name"],
                    "expected": test_case["expected"],
                    "got": result,
                }
            )
            print(
                f"Wrong output from tokenize_sentence function. \n\t Name: {failed_cases[-1].get('name')}. \n\tExpected: {failed_cases[-1].get('expected')}.\n\tGot: {failed_cases[-1].get('got')}."
            )

    if len(failed_cases) == 0:
        print("\033[92m All tests passed")
    else:
        print("\033[92m", successful_cases, " Tests passed")
        print("\033[91m", len(failed_cases), " Tests failed")


def test_remove_dynamic_symbol():
    successful_cases = 0
    failed_cases = []

    test_cases = [
        {"name": "default_check", "input": "This is a {{dynamic}}subject line",
         "expected": "This is a subject line"},
        {"name": "negative_check", "input": "This is not a dynamic subject line",
         "expected": "This is not a dynamic subject line"},
        {"name": "negative_start_check", "input": "{{dynamic}} subject line is here",
         "expected": "subject line is here"},
        {"name": "negative_end_check", "input": "The subject line is {{dynamic}}",
         "expected": "The subject line is"},
    ]

    for test_case in test_cases:
        result = remove_dynamic_symobl(test_case["input"])

        try:
            assert result == test_case["expected"]
            successful_cases += 1
        except:
            failed_cases.append(
                {
                    "name": test_case["name"],
                    "expected": test_case["expected"],
                    "got": result,
                }
            )
            print(
                f"Wrong output from remove_dynamic_symbol function. \n\t Name: {failed_cases[-1].get('name')}. \n\tExpected: {failed_cases[-1].get('expected')}.\n\tGot: {failed_cases[-1].get('got')}."
            )

    if len(failed_cases) == 0:
        print("\033[92m All tests passed")
    else:
        print("\033[92m", successful_cases, " Tests passed")
        print("\033[91m", len(failed_cases), " Tests failed")


def test_count_n_grams():
    successful_cases = 0
    failed_cases = []

    test_cases = [
        {"name": "default_check_1",
         "input": {
             "data": [
                 ["i", "like", "a", "cat"],
                 ["this", "dog", "is", "like", "a", "cat"],
             ],
             "n": 1,
             "start_token": "<s>",
             "end_token": "<e>"
         },
         "expected": {
             ("<s>",): 2,
             ("i",): 1,
             ("like",): 2,
             ("a",): 2,
             ("cat",): 2,
             ("this",): 1,
             ("dog",): 1,
             ("is",): 1,
             ("<e>",): 2,
         }
         },
        {"name": "default_check_2",
         "input": {
             "data": [
                 ["i", "like", "a", "cat"],
                 ["this", "dog", "is", "like", "a", "cat"],
             ],
             "n": 2,
             "start_token": "<s>",
             "end_token": "<e>"
         },
         "expected": {
             ("<s>", "<s>"): 2,
             ("<s>", "i"): 1,
             ("i", "like"): 1,
             ("like", "a"): 2,
             ("a", "cat"): 2,
             ("cat", "<e>"): 2,
             ("<s>", "this"): 1,
             ("this", "dog"): 1,
             ("dog", "is"): 1,
             ("is", "like"): 1,
             ("cat", "<e>"): 2,
             ("<e>", "<e>"): 2,
         }
         },
    ]

    for test_case in test_cases:
        result = count_n_grams(**test_case["input"])

        try:
            assert result == test_case["expected"]
            successful_cases += 1
        except:
            failed_cases.append(
                {
                    "name": test_case["name"],
                    "expected": test_case["expected"],
                    "got": result,
                }
            )
            print(
                f"Wrong output from count_n_grams function. \n\t Name: {failed_cases[-1].get('name')}. \n\tExpected: {failed_cases[-1].get('expected')}.\n\tGot: {failed_cases[-1].get('got')}."
            )

    if len(failed_cases) == 0:
        print("\033[92m All tests passed")
    else:
        print("\033[92m", successful_cases, " Tests passed")
        print("\033[91m", len(failed_cases), " Tests failed")


if __name__ == '__main__':
    test_ascii_or_emoji_only()
    test_tokenize_sentence()
    test_remove_dynamic_symbol()
    test_count_n_grams()
