# פתרון לRumour
## מה רוצים בשאלה
נתון עץ בינארי שממוספר מ1 עד אינסוף(הקודקוד הראשון הוא 1 ושני הבנים הם 2 3 הבן של 2 זה 4 5 של 3 זה 6 7 וכן הלאה).\
צריך לחשב את מרחק בין 2 מספרים על העץ(לדוגמא המרחק בין 1 ל5 הוא 2 כי יש ביניהם 2 צלעות)
## איך פותרים
קולטים את 2 המספרים שצריך לחשב את המרחק ביניהם.\
כדי להגיע לאבא של הקודקוד נצטרך לחלק ב2 ולעגל כלפי מטה.\
מכיוון ששני המספרים יוצאים מאותו שורש לשניהם חייב להיות "אבא"(קודקוד משותף שממנו הם התחילו).\
לכן נבדוק כל פעם מי המספר הגדול מביניהם ונחלק אותו ב2 עד שהוא יהיה שווה או קטן מהספר השני.\
כל חלוקה כזאת מוסיפים 1 למרחק.\
ברגע שהמספרים שווים התרגיל נגמר ואם המספר השני נהיה יותר גדול מתחילים לחלק אותו עד שבאיזשהו שלב הם יהיו שווים.
```
  while(a != b){
            if(a>b){
                sum++;
                a = a/2;
            }
            if(b>a){
                sum++;
                b = b/2;
            }
        }
```