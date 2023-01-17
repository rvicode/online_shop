from django import template

register = template.Library()


@register.filter(name='translate_fa')
def trans_num(value):
    value = str(value)
    translation_table = value.maketrans('1234567890', '۱۲۳۴۵۶۷۸۹۰')
    return value.translate(translation_table)
