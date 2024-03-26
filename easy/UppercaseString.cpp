// https://www.codingninjas.com/studio/guided-paths/data-structures-algorithms-new/content/662497/offering/10674879?leftPanelTabValue=PROBLEM&customSource=studio_nav

#include <iostream> 
string convertString(string str) 
{
	// WRITE YOUR CODE HERE
	for(int i=0; i<str.length(); i++){
		if(i == 0){
			str[i] = toupper(str[i]);
		}
		if(str[i] == ' '){
			str[i+1] = toupper(str[i+1]);
		}
	}
	return str;
}