# Print the sum of the current number and the previous number


def current_previous_sum():
    previous_num = 0
    for i in range(1, 11):
        answer = previous_num + i
        print("Current number is", i, "and previous Number is", previous_num, "and sum is", answer)
        previous_num = i
        # return answer


print(current_previous_sum())
