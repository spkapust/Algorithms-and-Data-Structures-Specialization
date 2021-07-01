#include <iostream>
#include <vector>
#include <algorithm>

int NaiveMaxPairwiseProduct(const std::vector<int>& numbers) {
    int max_product = 0;
    int n = numbers.size();

    for (int first = 0; first < n; ++first) {
        for (int second = first + 1; second < n; ++second) {
            max_product = std::max(max_product,
                numbers[first] * numbers[second]);
        }
    }

    return max_product;
}

int MaxPairwiseProduct(const std::vector<int>& numbers) {
    int a = 0;
    int b = 0;
    int n = numbers.size();

    for (int i = 0; i < n; ++i) {
        if (a < numbers[i]){a = numbers[i];}
        else if (b < numbers[i]){b = numbers[i];}
    }
    return a*b;
}

int main() {
    int n;
    std::cin >> n;
    std::vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> numbers[i];
    }

    std::cout << MaxPairwiseProduct(numbers); << "\n";
    return 0;
}
