#ifndef BOARD_H_
#define BOARD_H_

#include <iostream>
#include <vector>

using namespace std;

class Board{
	public:
		int array[3][3];
		int temp[3][3];
		int goal[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8, 0}};
		vector<int**> nap;
		int blrow;
		int blcol;
		int depth;

		Board* up = NULL;
		Board* down = NULL;
		Board* left = NULL;
		Board* right = NULL;
		Board* prev = NULL;
		

		Board();
		Board(Board* b);

		void display();
		void createBoard();
		void findBlank();
		void goUP();
		void goDOWN();
		void goLEFT();
		void goRIGHT();

};

//default constructor -> creates the board

Board::Board(){
	createBoard();
}

Board::Board(Board* b){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			this->array[i][j] = b->array[i][j];
		}
	}
}

//constructing the statets with user input

void Board::createBoard(){ 
	int userInput;

	cout<<"Enter 9 numbers, 0 being the blank space:\n";

	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			cin >> userInput;
			array[i][j] = userInput;
		}
	}
	cout << endl;
}

//displaying the states

void Board::display(){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			cout << array[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
}

//checking to see where the blank is located

void Board::findBlank(){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			if(array[i][j] == 0){
				blrow = i;
				blcol = j;
			}
		}
	}
}

//swap with one above if exists

void Board::goUP(){
	//cout << blrow << endl;
	if(blrow - 1 > -1){
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				temp[i][j] = array[i][j];
			}
		}
		swap(array[blrow][blcol], array[blrow - 1][blcol]);
	}
}

//swap with one below if exists

void Board::goDOWN(){
	if(blrow + 1 < 3){
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				temp[i][j] = array[i][j];
			}
		}
		swap(array[blrow][blcol], array[blrow + 1][blcol]);
	}
}

//swap with one left if exists

void Board::goLEFT(){
	if(blcol - 1 > -1){
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				temp[i][j] = array[i][j];
			}
		}
		swap(array[blrow][blcol], array[blrow][blcol - 1]);
	}
}

//swap with one right if exists

void Board::goRIGHT(){
	if(blcol + 1 < 3){
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				temp[i][j] = array[i][j];
			}
		}
		swap(array[blrow][blcol], array [blrow][blcol + 1]);
	}
}

#endif