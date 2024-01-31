def monotonic_stack(arr):
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[i] > arr[stack[-1]]:
            top = stack.pop()
            result[top] = arr[i]

        stack.append(i)

    return result

# Example usage:
arr = [3, 7, 1, 5, 2, 6]
result = monotonic_stack(arr)
print("Original array:", arr)
print("Next greater elements to the right:", result)
