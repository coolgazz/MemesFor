#include <iostream>
#include <string>
#include <random>
#include <time.h>
int attempts = 0;

int guessNumbers() {
	return rand() % 100 + 1;
}

int main() {
	srand(time(NULL));
	setlocale(LC_ALL, "RUS");
	
	std::cout << "Добро пожаловать в игру 'Угадай число'!" << std::endl;
	std::cout << "Я загадал число от 1 до 100. Попробуй угадать его." << std::endl;

	int secretNumber = guessNumbers();

	while (true) {
		int userGuess;
		std::cout << "Твоя попытка: ";
		std::cin >> userGuess;
		attempts += 1;

		if (userGuess < secretNumber) {
			std::cout << "Слишком маленькое число. Попробуй еще раз." << std::endl;
		}
		else if (userGuess > secretNumber) {
			std::cout << "Слишком большое число. Попробуй еще раз" << std::endl;
		}
		else {
			std::cout << "Поздравляю! Ты угадал число за " << attempts << " попыток." << std::endl;
			break;
		}
	}
	
	return 0;
	
}
