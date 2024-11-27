from django import template
import re
from django.utils.safestring import mark_safe  # 安全な文字列としてマークするために使用

register = template.Library()

@register.filter
def highlight(text, query):
    if query:
        # クエリをエスケープし、正規表現パターンを作成する
        pattern = re.compile(re.escape(query), re.IGNORECASE)
        
        # すべての一致する部分をハイライト用の <span> タグで囲む
        highlighted_text = pattern.sub(lambda match: f'<span class="highlight">{match.group(0)}</span>', text)
        
        # 安全な文字列としてマークして返す
        return mark_safe(highlighted_text)
    
    return text

