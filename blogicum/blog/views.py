from django.shortcuts import render

# 👇 временные посты, переделанные под тебя
entries = [
    {
        'id': 101,
        'location': 'Остров надёжды',
        'date': '12 марта 2023 года',
        'category': 'adventure',
        'text': 'Меня унесло на берег этого загадочного острова. Первый день выдался непростым.',
    },
    {
        'id': 102,
        'location': 'Остров надёжды',
        'date': '13 марта 2023 года',
        'category': 'daily-thoughts',
        'text': 'Сегодня я смог найти немного еды. Появился первый проблеск уверенности.',
    },
    {
        'id': 103,
        'location': 'Остров надёжды',
        'date': '20 марта 2023 года',
        'category': 'daily-thoughts',
        'text': 'Погода испортилась, приходится укрывать вещи от дождя. Настроение не сдаётся.',
    },
]

def main_feed(request):
    return render(request, 'index.html', {'entries': entries})

def entry_view(request, entry_id):
    entry = next((e for e in entries if e['id'] == entry_id), None)
    return render(request, 'detail.html', {'entry': entry})

def category_view(request, cat_slug):
    return render(request, 'category.html', {'slug': cat_slug})
