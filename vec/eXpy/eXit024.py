c=str(input('Que cidade você mora? ')).strip()
print(f'A cidade começa com "Santo"? {c[:5].lower() in "santo"}')