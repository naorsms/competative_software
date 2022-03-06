# פתרון לMinimum Permutation
## מה רוצים בתרגיל
מקבלים 2 מערכים ורוצים לחבר מערך אחד למערך השני כך שאם נדפיס את המערך איבר איבר ייצא לנו את המספר הקטן ביותר שניתן ליצור מחיבור של מערך אחד עם השני
## איך פותרים
ע"מ לקבל את הערך הקטן ביותר נרצה להכניס את האיברים הנמוכים שיהיו בתחילת המערך ואת האיברים הגדולים יותר בסוף המערך.\
לכן אין סיכוי שמערך שאנחנו מכניסים ממנו איברים,נכניס איבר עם ערך גדול למקום יותר נמוך מאיבר עם ערך נמוך שנכניס.\
נמיין את המערך ונכניס מהאיבר הקטן ביותר עד האיבר הגדול ביותר.\
צורת ההכנסה:נבדוק אם האיבר הראשון במערך קטן מהאיבר שאנחנו רוצים להכניס,במידה וכן נמשיך לאיבר הבא במידה ולא נמקם אותו במקום זה.\
וכך נעבור איבר איבר ונמשיך במערך אליו אנחנו מכניסים במקום בו הפסקנו עם האיבר הקודם.\
אם עוד נשאר איברים במערך ועברנו כבר בכל המערך שאנו רוצים להכנים אליו נשים את כל איברים אלו בסוף המערך.
```
S.sort()
i = 0
j = 0
while i < N+j and j < M :
   if A[i] > S[j]:
      A.insert(i, S[j])
      j+=1
   else:
      i+=1
print(" ".join(map(str, A))," ".join(map(str,S[j:M])))
```