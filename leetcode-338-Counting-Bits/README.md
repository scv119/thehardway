1, converting a number to binary needs to get the biggest 2 ^ n < this number. So I will use a variable to track the highest 2 ^ n. 
2, use DP methods, use a list to track the previous result and the previous result will be used in the future calculation. Ex: a number i, its binary will be 1 +  res(i - highest 2 ^ n)

