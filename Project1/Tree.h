#ifndef TREE_H_
#define TREE_H_

#include <iostream>
#include <vector>
#include "Board.h"

using namespace std;

class Tree{

	public:
		Board* root;
		Board* curr;
		Board* child;
		Board* temp;
		Board* prev;

		Board* up;
		Board* down;
		Board* left;
		Board* right;

		int depth;

		Tree();
		Tree(Board* b);

		void moveup();
		void movedown();
		void moveleft();
		void moveright();

};

//default constructor

Tree::Tree(){
	root = new Board();
	curr = root;
	child = 0;
	depth = 0;
}

Tree::Tree(Board* b){
	root = b;
	curr = root;
	child = 0;
	depth = 0;
}

//moving up using trees

void Tree::moveup(){
	child = new Board(curr);
	child -> findBlank();
	child -> goUP();
	curr -> up = child;
	child -> prev = curr;
	child -> display();
}

//moving down using trees

void Tree::movedown(){
	child = new Board(curr);
	child -> findBlank();
	child -> goDOWN();
	curr -> down = child;
	child -> prev = curr;
	child -> display();
}

//moving left using trees

void Tree::moveleft(){
	child = new Board(curr);
	child -> findBlank();
	child -> goLEFT();
	curr -> left = child;
	child -> prev = curr;
	child -> display();
}

//moving right using trees

void Tree::moveright(){
	child = new Board(curr);
	child -> findBlank();
	child -> goRIGHT();
	curr -> right = child;
	child -> prev = curr;
	child -> display();
}

#endif