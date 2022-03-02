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
		default:
			return x - '0';
		}
	}
}
int main() {
	char lcs1[1001], lcs2[1001];
	int n, arr[1001][1001];
	while (scanf("%d", &n) != 0) {
		for (int i = 1; i <= n; i++)
			scanf("%c", &lcs1[i]);
		for (int i = 1; i <= n; i++)
			scanf("%c", &lcs2[i]);
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n + 1; j++) {
				if (arr[i][j - 1] > arr[i - 1][j])
					arr[i][j] = arr[i][j - 1];
				else
					arr[i][j] = arr[i - 1][j];
				if (lcs1[i] == lcs2[j] || lcs1[i] == 'R' || lcs2[j] == 'R') {
					if (arr[i][j] < arr[i - 1][j - 1] + values(lcs1[i], lcs2[j]))
						arr[i][j] = arr[i - 1][j - 1] + values(lcs1[i], lcs2[j]);
				}
			}
		}
		printf("%d\n", arr[n][n] * 2);
		//printf('\n')
		scanf("%d", &n);
	}
}

