#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <vector>
#include <queue>
#include "Board.h"
#include "Tree.h"

using namespace std;

int main(){
//	Tree t = Tree();

	Board b = new Board();
	Tree t = Tree(&b);


	//cout << "Welcome to my 8-Puzzle Solver!\n\n Type 1 to use a default puzzle.\n Type 2 to create your own puzzle." << endl;
	
	
	
	t.moveup();
}