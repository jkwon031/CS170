#ifndef SEARCH_H_
#define SEARCH_H_

#include <iostream>
#include <vector>

using namespace std;

class Search{
	public:
		vector<Tree*> leaves;
		void generalSearchAlg();
};
	Search::Search(Tree* l){
		leaves = l;
	}

	//general serach algorithm -> not working

	void Search::generalSearchAlg(Board* b){
		int tempscore = 0;

		Tree* t = new Tree(b);

		leaves.push_back(t);
		while(!leaves.empty()){
			int score = 60000;
			Tree* smleaves;
			for(int i = 0; i < leaves.size(); i++){
				tempscore = 0 + leaves.at(i)->depth;
				if(tempscore < score){
					score = tempscore;
					smleaves = leaves.at(i);
				}
			}
			smleaves.moveup();
			smleaves.movedown();
			smleaves.moveleft();
			smleaves.moveright();
		}
	}

#endif