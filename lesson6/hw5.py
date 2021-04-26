# fith home work
import re


def normalize(str):
    map = {
        ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e',
        ord('ё'): 'ye', ord('ж'): 'j', ord('з'): 'z', ord('и'): 'i', ord('й'): 'yi', ord('к'): 'k',
        ord('л'): 'l', ord('м'): 'm', ord('н'): 'n', ord('о'): 'o', ord('п'): 'p', ord('р'): 'r',
        ord('с'): 's', ord('т'): 't', ord('у'): 'y', ord('ф'): 'f', ord('х'): 'h', ord('ц'): 'c',
        ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'sch', ord('ъ'): '', ord('ы'): 'u', ord('ь'): '',
        ord('э'): 'e', ord('ю'): 'yu', ord('я'): 'ya', ord('і'): 'i', ord('ї'): 'ii', ord('є'): 'ye',

        ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D', ord('Е'): 'E',
        ord('Ё'): 'YE', ord('Ж'): 'J', ord('З'): 'Z', ord('И'): 'I', ord('Й'): 'YI', ord('К'): 'K',
        ord('Л'): 'L', ord('М'): 'M', ord('Н'): 'N', ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R',
        ord('С'): 'S', ord('Т'): 'T', ord('Y'): 'Y', ord('Ф'): 'F', ord('Х'): 'H', ord('Ц'): 'C',
        ord('Ч'): 'CH', ord('Ш'): 'SH', ord('Щ'): 'SCH', ord('Ъ'): '', ord('Ы'): 'U', ord('Ь'): '',
        ord('Э'): 'E', ord('Ю'): 'YU', ord('Я'): 'YA', ord('І'): 'I', ord('Ї'): 'II', ord('Є'): 'YE'
    }
    str = str.translate(map)
    text = re.sub(r'\W', '_', str)
    return text
