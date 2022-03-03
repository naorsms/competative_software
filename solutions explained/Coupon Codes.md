# פתרון לCoupon Codes
## מה רוצים בתרגיל
מביאים לך מספר מחרוזות והם רוצים שתמצא את מספר הזוגות שהמחרוזות מייצרות שבהם יש רק תו אחד שונה.
לדוגמא:
 ```
WELC-OMET-OTHE
IEEE-XTRE-ME14
AAAA-0000-A0A0
AAAA-0000-A0A1
AAAA-0000-A0AB
AAAA-0000-ABAB
```
התשובה תהיה 4 כי יש הבדל של תו 1 בין הזוגות:(3,4),(3,5),(4,5),(5,6).
### קלט
שורה ראשונה מספר שמייצג את מספר המחרוזות(N) שייבחנו בתרגיל(לדוגמא בתרגיל למעלה N=6)
מספר השורות הבאות יהיה N,שורה לכל מחרוזת
הקלט במחרוזות יהיה 0-9 וA-Z ומכפים שצריך להסיר בפתרון

### התשובה שצריך להדפיס
מספר זוגות המחרוזות שבהן יש הבדל של תו 1(לפי הדוגמא למעלה נדפיס 4)

## איך פותרים
יוצרים dictionary
רצים על לולאה באורך N על כל מחרוזת
מסירים את כל המכפים מהמחרוזת
רצים בעוד לולאה באורך של המחרוזת ובכל סיבוב משנים תו אחד לפי הסדר במחרוזת (לדוגמא,משנים את התו ל-*).
```
for n in range(string_num):
    coupon = input().replace('-', '')
    for i in range(len(coupon)):
        string = coupon[:i] + "*" + coupon[i + 1:]
        if string in dic:
            dic[string] += 1
        else:
            dic[string] = 1
```
בודקים אם המחרוזת קיימת, אם כן אז הkey יהיה המחרוזת והvalue יהיה 1 + כמות הפעמים שהמחרוזת כבר הופיע אם לא אז הvalue יהיה שווה ל-1. דוגמא ללולאה אחרי 3 וחצי מחרוזות של הדוגמא מלמעלה:
```
{'*ELCOMETOTHE': 1, 'W*LCOMETOTHE': 1, 'WE*COMETOTHE': 1, 'WEL*OMETOTHE': 1, 'WELC*METOTHE': 1, 'WELCO*ETOTHE': 1, 'WELCOM*TOTHE': 1, 'WELCOME*OTHE': 1, 'WELCOMET*THE': 1,
'WELCOMETO*HE': 1, 'WELCOMETOT*E': 1, 'WELCOMETOTH*': 1,'*EEEXTREME14': 1, 'I*EEXTREME14': 1, 'IE*EXTREME14': 1, 'IEE*XTREME14': 1, 'IEEE*TREME14': 1, 'IEEEX*REME14': 1,
'IEEEXT*EME14': 1, 'IEEEXTR*ME14': 1, 'IEEEXTRE*E14': 1, 'IEEEXTREM*14': 1, 'IEEEXTREME*4': 1, 'IEEEXTREME1*': 1, '*AAA0000A0A0': 1, 'A*AA0000A0A0': 1, 'AA*A0000A0A0': 1,
'AAA*0000A0A0': 1, 'AAAA*000A0A0': 1, 'AAAA0*00A0A0': 1, 'AAAA00*0A0A0': 1, 'AAAA000*A0A0': 1, 'AAAA0000*0A0': 1, 'AAAA0000A*A0': 1, 'AAAA0000A0*0': 1, 'AAAA0000A0A*': 2,
'*AAA0000A0A1': 1, 'A*AA0000A0A1': 1, 'AA*A0000A0A1': 1, 'AAA*0000A0A1': 1, 'AAAA*000A0A1': 1, 'AAAA0*00A0A1': 1, 'AAAA00*0A0A1': 1, 'AAAA000*A0A1': 1, 'AAAA0000*0A1': 1,
'AAAA0000A*A1': 1, 'AAAA0000A0*1': 1}
```
אחרי שרצים על כל המחרוזות בודקים אם התאים בdictionary כל key  שהvalue שלו גדול מ1 סוכמים את כל המספרים מ1 עד לערך של הvalue לא כולל
```
Sum = 0
for index in dic:
    appearances = dic[index]
    if appearances > 1:
        for i in range(1, appearances):
            Sum += i
print(Sum)
```
לדוגמא:
אם הvalue הוא 3 אז סוכמים 1 + 2 
בגלל שאתה רוצה לראות כמה זוגות אתה יכול להרכיב מהvalue אז כאשר הוא 3 יש לך 2 זוגות אבל גם מ2 זוגות אתה יכול להרכיב עוד זוג 1
```
                    AAAA-0000-A0A0
AAAA-0000-A0A0      AAAA-0000-A0A1        AAAA-0000-A0A1
AAAA-0000-A0A1   =                   +    AAAA-0000-A0AB 
AAAA-0000-A0AB      AAAA-0000-A0A0
                    AAAA-0000-A0AB
```
