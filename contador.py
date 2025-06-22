nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel", "Helena", 
    "Isabela", "João", "Ana", "Bruno", "Carlos", "Gabriel", "Isabela", "João",
    "Lucas", "Mariana", "Nathalia", "Otávio", "Paula", "Renato", "Sara", "Thiago", 
    "Úrsula", "Vanessa", "Wesley", "Yasmin", "Zeca", "Mariana", "Carlos", "Ana"
]
contagem = {}

for nome in nomes:
    if nome in contagem:
        contagem[nome] += 1
    else:
        contagem[nome] = 1
        
        
for chave,valor in contagem.items():
    print(f'{chave}: {valor}')

