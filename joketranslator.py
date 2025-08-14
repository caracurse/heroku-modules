# Name: JokeTranslator
# Description: Fun joke - fake translator with multiple joke languages
# Author: @sansaramods
# Commands:
# .jtr | .jlangs
# ---------------------------------------------------------------------------------
# 🔒 Licensed under the GNU GPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ⚠️ All modules is not scam and absolutely safe.
# 👤 https://t.me/exodiast
#-----------------------------------------------------------------------------------
# meta developer: @sansaramods
#-----------------------------------------------------------------------------------

__version__ = (1, 3, 2)

from .. import loader, utils
from telethon.tl.types import Message

ru_vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
en_vowels = 'aeiouyAEIOUY'
all_vowels = ru_vowels + en_vowels

uwu_map = {
    'р': 'в', 'л': 'в', 'н': 'ня', 'Р': 'В', 'Л': 'В', 'Н': 'Ня',
    'r': 'w', 'l': 'w', 'n': 'nya', 'R': 'W', 'L': 'W', 'N': 'Nya',
    '!': '! >w<', '?': '? owo', '.': ' uwu', ',': ' uwu'
}        

emoji_dict = {
    **{c: '😺' for c in 'аАaA'},
    **{c: '🐘' for c in 'еЕёЁeE'},
    **{c: '😸' for c in 'иИiI'}, 
    **{c: '🦁' for c in 'оОoO'},
    **{c: '🐺' for c in 'уУuU'},  
    'б': '🐝', 'в': '🌊', 'г': '🐉', 'д': '🦕',
    'ж': '🔥', 'з': '🐍', 'й': '🍯', 'к': '🦘',
    'л': '🦁', 'м': '🐒', 'н': '🐄', 'п': '🐧',
    'р': '🐇', 'с': '🐍', 'т': '🐅', 'ф': '🦊',
    'х': '🦄', 'ц': '🦔', 'ч': '🐿️', 'ш': '🦉',
    'щ': '🦇', 'ъ': '⛰️', 'ы': '🌋', 'ь': '🏔️',
    'э': '🌌', 'ю': '🌠', 'я': '🌞',
    'b': '🐝', 'c': '🌵', 'd': '🐉', 'f': '🐟',
    'g': '🦍', 'h': '🏠', 'j': '🎷', 'k': '🦘',
    'm': '🐒', 'p': '🐧', 'q': '👑', 's': '🐍',
    't': '🐅', 'v': '🦄', 'w': '🌊', 'x': '🦔',
    'y': '🍯', 'z': '🦓'        
}

leet_dict = {
    **{c: '4' for c in 'аАaA'},
    **{c: '3' for c in 'еЕёЁeE'},
    **{c: '1' for c in 'иИiIлЛlL'},
    **{c: '0' for c in 'оОoO'},
    **{c: '7' for c in 'тТtT'},
    'з': '3', 'ч': '4', 'я': '9.1', 'ю': '1.0',
    'b': '8', 'd': '|)', 'g': '9', 's': '5',
    'z': '2', 'h': '|-|', 'k': '|<', 'm': '|\\/|',
    'n': '|\\|', 'p': '|>', 'q': '0_', 'r': '|2',
    'v': '\\/', 'w': '\\/\\/', 'x': '><'        
}                


@loader.tds
class JokeTranslator(loader.Module):
    """Fun joke translator with multiple fake languages"""

    strings = {
        "name": "JokeTranslator",
        "result": "<emoji document_id=6039779802741739617>✏️</emoji>Original:\n<blockquote expandable>{}</blockquote>\n<emoji document_id=6030657343744644592>🔁</emoji> <b>Translated to</b> {}\n<blockquote expandable>{}</blockquote>",
        "langs": "<blockquote expandable>\n<b>Supported languages</b>\n\n"
                "<emoji document_id=4972283471075476249>🛑</emoji> cat\n<emoji document_id=4972283471075476249>🛑</emoji> pirate (pi)\n<emoji document_id=4972283471075476249>🛑</emoji> dog (woof)\n<emoji document_id=4972283471075476249>🛑</emoji> uwu\n<emoji document_id=4972283471075476249>🛑</emoji> leet (1337)\n"
                "<emoji document_id=4972283471075476249>🛑</emoji> reverse (rev)\n<emoji document_id=4972283471075476249>🛑</emoji> emoji\n<emoji document_id=4972283471075476249>🛑</emoji> binary (bin)\n<emoji document_id=4972283471075476249>🛑</emoji> fuck (f)\n<emoji document_id=4972283471075476249>🛑</emoji> vowels (vow)\n</blockquote>",
        "error": "<emoji document_id=5774077015388852135>❌</emoji> Specify language and text. Example: .jtr cat Hello",
        "no_args": "<emoji document_id=5774077015388852135>❌</emoji> Not enough arguments!",
        "invalid_lang": "<emoji document_id=5774077015388852135>❌</emoji> Invalid language! Use .jlangs to see available languages",
    }
    
    strings_ru = {
        "result": "<emoji document_id=6039779802741739617>✏️</emoji><b>Оригинал</b>:\n<blockquote expandable>{}</blockquote>\n<emoji document_id=6030657343744644592>🔁</emoji> <b>Перевод на</b> {}\n<blockquote expandable>{}</blockquote>",
        "error": "<emoji document_id=5774077015388852135>❌</emoji> Укажите язык и текст. Пример: .jtr cat Привет",
        "no_args": "<emoji document_id=5774077015388852135>❌</emoji> Недостаточно аргументов!",
        "invalid_lang": "<emoji document_id=5774077015388852135>❌</emoji> Неверный язык! Используйте .jlangs для списка доступных языков",
        "langs": "<blockquote expandable>\n<b>Поддерживаемые языки</b>\n\n"
                "<emoji document_id=4972283471075476249>🛑</emoji> cat (кошачий)\n<emoji document_id=4972283471075476249>🛑</emoji> pirate (pi, пиратский)\n<emoji document_id=4972283471075476249>🛑</emoji> dog (woof, собачий)\n<emoji document_id=4972283471075476249>🛑</emoji> uwu\n<emoji document_id=4972283471075476249>🛑</emoji> leet (1337)\n"
                "<emoji document_id=4972283471075476249>🛑</emoji> reverse (rev, реверс)\n<emoji document_id=4972283471075476249>🛑</emoji> emoji (эмодзи)\n<emoji document_id=4972283471075476249>🛑</emoji> binary (bin, двоичный)\n<emoji document_id=4972283471075476249>🛑</emoji> fuck (f, мат)\n<emoji document_id=4972283471075476249>🛑</emoji> vowels (vow, гласные)\n</blockquote>",
    }

    async def jtrcmd(self, message: Message):
        """ use: .jtr <lang> <text> or reply .jtr <lang>"""
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        
        if reply:
            text = reply.raw_text
            if not args:
                await utils.answer(message, self.strings("error"))
                return
            lang = args.lower()
        else:
            if not args or len(args.split()) < 2:
                await utils.answer(message, self.strings("error"))
                return
            lang, text = args.split(maxsplit=1)
            lang = lang.lower()
        
        result = text
        valid_lang = False
        
        if lang in ["cat", "кошачий"]:
            valid_lang = True
            for vowel in all_vowels:
                if vowel in ru_vowels:
                    result = result.replace(vowel, "~мяу~")
                elif vowel in en_vowels:
                    result = result.replace(vowel, "~meow~")
            result = result.replace(".", " 😺")
        
        elif lang in ["pirate", "pi", "пиратский"]:
            valid_lang = True
            replacements = {
                'ты': 'ты, морской волк', 'you': 'ye scurvy dog',
                'я': 'капитан', 'i': 'captain',
                'мы': 'мы, команда', 'we': 'we crew',
                'привет': 'йо-хо-хо', 'hello': 'ahoy'
            }
            for k, v in replacements.items():
                result = result.replace(k, v)
            result = result.replace(".", "🏴‍☠️")
        
        elif lang in ["dog", "woof", "собачий"]:
            valid_lang = True
            consonants = 'бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz'
            for c in consonants:
                if c in 'рrРR':
                    result = result.replace(c, 'ррр' if c in 'рР' else 'rrr')
                elif c in 'лlЛL':
                    result = result.replace(c, 'вф' if c in 'лЛ' else 'woof')
                else:
                    result = result.replace(c, c*2)
            result = result.replace(".", " 🐶")
        
        elif lang in ["uwu", "u"]:
            valid_lang = True
            result = "".join(uwu_map.get(c, c) for c in result)
        
        elif lang in ["leet", "1337"]:
            valid_lang = True
            result = "".join(leet_dict.get(c.lower(), c) if c.isalpha() else c for c in result)
        
        elif lang in ["reverse", "rev", "реверс"]:
            valid_lang = True
            result = result[::-1]
        
        elif lang in ["emoji", "эмодзи"]:
            valid_lang = True
            result = " ".join(emoji_dict.get(c.lower(), c) if c.isalpha() else c for c in result)
        
        elif lang in ["binary", "bin", "двоичный"]:
            valid_lang = True
            result = " ".join(format(ord(c), '08b') for c in result)
        
        elif lang in ["fuck", "f", "мат"]:
            valid_lang = True
            if any(cyr in text.lower() for cyr in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
                result = " ".join(word + " нахуй" for word in result.split())
            else:
                result = " ".join(word + " fuck" for word in result.split())
        
        elif lang in ["vowels", "vow", "гласные"]:
            valid_lang = True
            new_text = []
            for char in result:
                if char.lower() in all_vowels.lower():
                    if char.isupper():
                        new_text.append(char * 3)
                    else:
                        new_text.append(char * 2)
                else:
                    new_text.append(char)
            result = "".join(new_text)
        
        if not valid_lang:
            await utils.answer(message, self.strings("invalid_lang"))
            return

        await utils.answer(message, self.strings("result").format(text, lang, result))

    async def jlangscmd(self, message: Message):
        """ check supported langs"""
        await utils.answer(message, self.strings("langs"))