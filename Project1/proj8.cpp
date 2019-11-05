#include <iostream>
#include <cstdlib>
#include <queue>
#include <string.h>
#include <stdio.h>

using namespace std;

struct node{
	int arr[3][3];
	struct node *up;
	struct node *down;
	struct node *left;
	struct node *right;
};

struct node* newNode(int data){
	struct node* node = (struct node*)malloc(sizeof(struct node));
	node->arr;
	node->up = NULL;
	node->down = NULL;
	node->left = NULL;
	node->right = NULL;
	return(node);
}

void matcop(int result[3][3], int mat[3][3]){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			result[i][j] = mat[i][j];
		}
	}
}

void boundary(int r, int c, int m[3][3], queue<int[3][3]>& q){
	int rm[3][3];
	int rp[3][3];
	int cm[3][3];
	int cp[3][3];

	if(r - 1 > -1){
		swap(m[r][c], m[r-1][c]);
		matcop(rm, m);
		q.push(rm);
	}
	if(r + 1 < 3){
		swap(m[r][c], m[r+1][c]);
		matcop(rp, m);
		q.push(rp);
	}
	if(c - 1 > -1){
		swap(m[r][c], m[r][c-1]);
		matcop(cm, m);
		q.push(cm);
	}
	if(c + 1 < 3){
		swap(m[r][c], m[r][c+1]);
		matcop(cp, m);
		q.push(cp);
	}
}


int search(int matrix[3][3], int goalm[3][3]){
	queue<int[3][3]> ucqueue;

	int rmatrix[3][3];
	int lmatrix[3][3];

	int row = 0;
	int col = 0;

	struct node* head;

	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			if(matrix[i][j] == 0){
				head->arr = matrix;
				ucqueue.push(matrix);
				row = i;
				col = j;
			}
		}
	}

	do{
		if(head->arr == NULL){
			return -1;
		}
		if(head->arr == goalm){
			return 1;
		}
		ucqueue.pop();
		boundary(row, column, matrix, ucqueue);

		head->arr = ucqueue.front();
	}while(head->arr != goalm);
}

int printMatrix(int matrix[3][3]){
		for(int row = 0; row < 3; row++){
		for(int col = 0; col < 3; col++){
			cout << matrix[row][col] << " ";
		}
		cout << endl;
	}
}

int main(){
	int goal[3][3];
	int value = 1;
	
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 3; j++){
			if(i == 2 && j == 2){
				goal[i][j] = 0;
			}else{
				goal[i][j] = value;
				value++;
			}
		}
	}
	printMatrix(goal);
}