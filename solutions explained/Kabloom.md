# פתרון לKabloom
## מה רוצים בתרגיל
יש שני מערכים המכילים קלפים וצריך למצוא אלגוריתם שמוצא את התת מחרוזת הזהה ב2 המערכים הגדולה ביותר(כולל ג'וקרים שיכולים להיות כל מספר אם צריך).
## איך פותרים
בנינו פונקיצה ששולחים אליה זוג קלפים(קלף מכל מערך) שווים\אחד מהם ג'וקר והם מחזירים את הערך בהתאם לערכים שנקבעו מראש לקלפים ללא מספר ול-10 שמתייחסים אליו כאל האות T בתרגיל.\
נשתמש באלגורים LCS כדי לפתור את זה:
נבנה מטריצה ריבועית n+1 על n+1 כאשר השורה הראשונה והעמודה הראשונה מלאות באפסים.\
השורה מייצגת את המערך הראשון והעמודה מייצגת את המערך השני.\
נתחיל למלא מהאיבר במקום (1,1) עד לאיבר במקום ה(n,n).\
צורת המילוי: אם האיבר שאנחנו נמצאים בו עכשיו(עמודה) גדול מהערך של האיבר שהשורה מייצגת

אם הערך שאנחנו נמצאים בו עכשיו -האיבר שנמצא מעליו במטריצה גדול מהאיבר שנמצא משמאלו נשים אותו בערך ואם לא נשים את הערך השני.\
כעת נבדוק אם האות שאנחנו נמצאים בו עכשיו(עמודה) שווה מהאות של האיבר שהשורה מייצגת אם הם שונים לא נשנה כלום ונעבור לאיבר הבא.\ 
אם הם שווים נשים את הערך המקסימאלי בתא הנוכחי שלנו מתוך: 1)האיבר שנמצא מעל שמאלה לערך הנוכחי+ הערך שעכשיו השגנו מהפונקציה של האיברים שווים 2)הערך הנוכחי שנמצא בתא.\
נעבור לשלב הבא עד שהמטריצה מלאה עד הסוף ונחזיר את האיבר האחרון כפול 2
```
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
```
