# اردو سکرپٹ
اردو سکرپٹ اردو زبان میں کوڈنگ کو فروغ دینے کی ایک کا وش ہے۔ کیونکہ انگریزی زبان سیکھنے کے بعد ہی لوگ اعلی معیار کی کوڈنگ کرسکتے ہیں۔ اردو سکرپٹ اس
مرحلے کو ختم کرکے اردو زبان میں کوڈنگ کرنے کا موقع دیتی ہے۔

# یہ رپوزٹری کیا ہے؟
اس رپا زٹری<sup>5</sup> میں اردوپروگرامنگ زبان<sup>3</sup> کے کمپائیلر<sup>4</sup> کی ہے۔ ابھی تک آپکو اس میں دو ضروری چیزیں نظر آیئنگیں۔

*  urdu.lexer.py
*  پہلا پروگرام۔اردو


 کمپایئلر کا پھلا مرحلہ لیکزیکل انیلسیز<sup>1</sup> کہلاتا ہے۔ اس میں اردو کے الفاظ کہ ریگولر اکسپریشنز<sup>2</sup> کی زبان میں لکھا جاتا ہے تاکہ ہم ایک نئی کمپیو ٹر کی زبان کوکسی اصول کے تحت بیان کرسکیں۔


اگر آ پ اس کوڈ کو رن کریں تو آ پ کو درج ذیل سے قریب قریب تحریر نظرآئے گی۔


```
LexToken(مختص,'اول',1,0)

LexToken(برابر,'=',1,4)

LexToken(ھندسہ,10,1,6)

LexToken(مختص,'دوم',2,9)

LexToken(برابر,'=',2,13)

LexToken(ھندسہ,20,2,15)

LexToken(مختص,'نتیجہ',4,19)

LexToken(برابر,'=',4,25)

LexToken(مختص,'اول',4,27)

LexToken(جمع,'+',4,31)

LexToken(مختص,'دوم',4,33)

LexToken(اگر,'اگر',5,37)

LexToken(مختص,'نتیجہ',6,42)

LexToken(سےبڑا,'>',6,48)

LexToken(ھندسہ,20,6,50)

LexToken(مختص,'لکھیں',7,53)

LexToken(رموز,':',7,58)

LexToken(رموز,"'",7,60)

LexToken(مختص,'کامیاب',7,61)

LexToken(رموز,"'",7,67)

LexToken(ورنہ,'ورنہ',8,69)

LexToken(مختص,'لکھیں',9,74)

LexToken(رموز,':',9,79)

LexToken(رموز,"'",9,81)

LexToken(مختص,'ناکام',9,82)

LexToken(رموز,"'",9,87)

LexToken(تمام,'تمام',10,89)
```
اگر آپ اس کاوش میں حصہ لینا چاہتے ہیں تو رابطہ کیلیے مجھے ای میل کیجیے : zain@appslab.io


1. Lexical Anylisis
2. Regular Expressions
3. Programming Language
4. Compiler
5. Repository
