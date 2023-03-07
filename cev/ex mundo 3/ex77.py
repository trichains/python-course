# Cria uma tupla com as palavras
palavras = ('abacate', 'elefante', 'banana', 'bicicleta', 
            'computador', 'dinossauro', 'futebol', 'guitarra', 
            'programar', 'jardim')

# Cria um conjunto com as vogais
vogais = {'a', 'e', 'i', 'o', 'u'}

# Itera sobre as palavras
for palavra in palavras:
    
    # Imprime a palavra em maiúsculo
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    
    # Itera sobre as letras da palavra
    for letra in palavra:
        
        # Verifica se a letra é uma vogal
        if letra.lower() in ('aeiou'):
            print(letra, end=' ')
