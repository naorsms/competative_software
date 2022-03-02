#include<stdio.h>
#include <stdlib.h>
//#define _CRT_SECURE_NO_WARNINGS
int values(char x, char y) {
	if (x == 'R') {
		switch (y) {
		case 'R':
			return 50;
		case 'A':
			return 20;
		case 'Q':
			return 15;
		case 'K':
			return 15;
		case 'J':
			return 15;
		case 'T':
			return 10;
		default:
			return y - '0';
		}
	}
	else if (y == 'R') {
		switch (x) {
		case 'R':
			return 50;
		case 'A':
			return 20;
		case 'Q':
			return 15;
		case 'K':
			return 15;
		case 'J':
			return 15;
		case 'T':
			return 10;
		default:
			return x - '0';
		}
	}
	else {
		switch (x) {
		case 'A':
			return 20;
		case 'Q':
			return 15;
		case 'K':
			return 15;
		case 'J':
			return 15;
		case 'T':
			return 10;
		default:
			return x - '0';
		}
	}
}
char lcs1[1001][5], lcs2[1001][5];
int n, arr[1001][1001];
int main() {

	while (scanf("%d", &n) != 0) {
		if (n == 0)
			break;
		//printf("%d\n",n);
		for (int i = 1; i <= n; i++)
			scanf("%s", lcs1[i]);
		for (int i = 1; i <= n; i++)
			scanf("%s", lcs2[i]);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (arr[i][j - 1] > arr[i - 1][j])
					arr[i][j] = arr[i][j - 1];
				else
					arr[i][j] = arr[i - 1][j];
				if (lcs1[i][0] == lcs2[j][0] || lcs1[i][0] == 'R' || lcs2[j][0] == 'R') {
					if (arr[i][j] < arr[i - 1][j - 1] + values(lcs1[i][0], lcs2[j][0]))
						arr[i][j] = arr[i - 1][j - 1] + values(lcs1[i][0], lcs2[j][0]);
				}
			}
		}
		printf("%d\n", arr[n][n] * 2);
		//printf('\n')
		//n = scanf("%d", &n);
	}
}

