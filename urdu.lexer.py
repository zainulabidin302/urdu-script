# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

urdu_letters = 'اب ت ٹ ث ج چ ح خ د ڈ ذ ر ڑ ز ژ س ش ص ض ط ظ ع غ ف ق ک گ ل م ن ں و ہ ھ ء ی ۓ'
digits  = '1234567890'

reserved = {
    'اگر':'اگر',
    'ورنہ': 'ورنہ',
    'جب تک': 'جب تک',
}

# List of token names.   This is always required
# مختص الفاظ وہ ہیں جن کا زبان میں کویئ خاص مطلب ہے

tokens = ['ھندسہ', 'مختص', 'حاشیہ' , 'جمع' ,'منفی','ضرب','تقسیم','برابر', 'سےبڑا' , 'سےچھوٹا' ,'رموز'] + list(reserved.values())

def t_ھندسہ(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_مختص(t):
    r"""[ابتٹثجچحخدڈذرڑزژسشصضطظعغفقکگلمنںوہھءیۓ]+"""
    t.type = reserved.get(t.value, 'مختص')  # Check for reserved words
    return t

# comments
def t_حاشیہ(t):
    r'\#.*'
    pass
    # No return value. Token discarded

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_جمع       = r'\+'
t_منفی      = r'-'
t_تقسیم     = r'/'
t_ضرب       = r'\*'
t_برابر     = r'='
t_رموز      = r'[\'\"' + r'؛:' + r']'
t_سےبڑا     = r'>'
t_سےچھوٹا   = r'<'

try:
    filename = 'پھلاپروگرام۔اردو'

    with open(filename, 'r', encoding='utf') as f:
        source = f.read()
    lexer = lex.lex()
    lexer.input(source)
    while True:
        token = lexer.token()
        if token is None:
            break
        print(token)


except Exception as e:
    print(e)