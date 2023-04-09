convidados = ["Kendrick Lamar", "Drake", "Cardi B", "J. Cole", "Travis Scott"]
for convidado in convidados:
    print(f"Olá {convidado}! Você está convidado para um jantar em minha casa no próximo sábado.")

convidado_ausente = "Drake"
convidados.remove(convidado_ausente)
print(f"\nInfelizmente, {convidado_ausente} não poderá comparecer ao jantar.\n")

print("Os seguintes convidados não poderão comparecer ao jantar:")
print(convidado_ausente)

novo_convidado = "Post Malone"
convidados.append(novo_convidado)
print(f"\n{convidado_ausente} será substituído por {novo_convidado}.\n")

for convidado in convidados:
    print(f"Olá {convidado}! Você está convidado para um jantar em minha casa no próximo sábado.")