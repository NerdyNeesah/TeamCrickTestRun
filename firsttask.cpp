#include <iostream>
#include <string>
#include <bits/stdc++.h>
using namespace std;
int hammingdist(char *str1, char *str2)
 {
    int i = 0, count = 0;
    while (str1[i] != '\0')
    {
        if (str1[i] != str2[i])
            count++;
        i++;
    }
    return count;
}
int main()
{
    char str1[] = "@Sanniya01";
    
    char str2[] = "@Sanniya01";

    
    cout<< "Sanniya Middha"<<","<<"sanniyamiddha12@gmail.com"<<","<<str1<<","<<"Genomics"<<","<<str2<<","<<hammingdist (str1, str2)<<endl;
    
    return 0;
}
