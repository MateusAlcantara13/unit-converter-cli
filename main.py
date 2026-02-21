import unicodedata


# ===================== FUNÇÕES UTILITÁRIAS =====================

def formatar_escolha(texto):
    """Remove acentos, espaços extras e converte para minúsculas.
    Isso garante que entradas como 'Temperatura' ou 'TEMPERATURA' sejam aceitas."""
    return (
        unicodedata.normalize('NFD', texto)
        .encode('ASCII', 'ignore')
        .decode('utf-8')
        .strip()
        .lower()
    )

def formatar_numero_inteiro(numero):
    """Converte a entrada do usuário para inteiro, removendo espaços."""
    return int(numero.strip())

def formatar_numero(numero):
    """Converte a entrada do usuário para float.
    Aceita tanto vírgula quanto ponto como separador decimal. ex: '32,5' ou '32.5'"""
    return float(numero.strip().replace(',', '.'))


# ===================== FUNÇÕES DE CONVERSÃO =====================

def fahrenheit_para_celsius(temperaturaF):
    """Converte temperatura de Fahrenheit para Celsius."""
    conversor = (temperaturaF - 32) / 1.8
    return conversor

def celsius_para_fahrenheit(temperaturaC):
    """Converte temperatura de Celsius para Fahrenheit."""
    conversor = (temperaturaC * 1.8) + 32
    return conversor

def km_para_milhas(distanciaKM):
    """Converte distância de quilômetros para milhas."""
    return distanciaKM * 0.6214

def milhas_para_km(distanciaMilhas):
    """Converte distância de milhas para quilômetros."""
    return distanciaMilhas * 1.609

def kg_para_libra(pesoKG):
    """Converte peso de quilogramas para libras."""
    return pesoKG * 2.20462

def libra_para_kg(pesoLibra):
    """Converte peso de libras para quilogramas."""
    return pesoLibra * 0.453592


# ===================== MAPEAMENTO DE CONVERSÕES =====================

# Dicionário que associa cada unidade e tipo de conversão à sua função e descrição.
# Facilita a expansão futura: basta adicionar uma nova chave ao dicionário.
conversoes = {
    'temperatura': {
        1: {
            'funcao': fahrenheit_para_celsius,
            'descricao': '°F para graus celsius'
        },
        2: {
            'funcao': celsius_para_fahrenheit,
            'descricao': '°C para Fahrenheit'
        }
    },

    'distancia': {
        1: {
            'funcao': km_para_milhas,
            'descricao': 'KM para milhas'
        },
        2: {
            'funcao': milhas_para_km,
            'descricao': 'Milhas para quilômetros'
        }
    },

    'peso': {
        1: {
            'funcao': kg_para_libra,
            'descricao': 'KG para libra'
        },
        2: {
            'funcao': libra_para_kg,
            'descricao': 'Libra para KG'
        }
    }
}


# ===================== FLUXO PRINCIPAL =====================

# Exibe o menu principal com todas as opções disponíveis
print('\n╔══════════════════════════════════════════════════════════╗')
print('║                      CONVERSOR                           ║')
print('╠══════════════════════════════════════════════════════════╣')
print('║  🌡  Temperatura                                          ║')
print('║      → Celsius para Fahrenheit                           ║')
print('║      → Fahrenheit para Celsius                           ║')
print('╠══════════════════════════════════════════════════════════╣')
print('║  📏  Distância                                           ║')
print('║      → Km para Milhas                                    ║')
print('║      → Milhas para Km                                    ║')
print('╠══════════════════════════════════════════════════════════╣')
print('║  ⚖   Peso                                                 ║')
print('║      → Kg para Libras                                    ║')
print('║      → Libras para Kg                                    ║')
print('╚══════════════════════════════════════════════════════════╝')

# Lê e formata a escolha da unidade, aceitando variações de digitação
escolha_unidade = formatar_escolha(input('Escolha a unidade que deseja trabalhar ex (Temperatura): '))

# Valida a escolha até o usuário inserir uma opção válida
while escolha_unidade not in ['temperatura', 'distancia', 'peso']:
    print('Unidade inválida !')
    escolha_unidade = formatar_escolha(input('Escolha a unidade que deseja trabalhar ex (Temperatura): '))

# ── Temperatura ──
if escolha_unidade == 'temperatura':
    print('Insira o tipo de conversão para temperatura')
    tipo_conversao = formatar_numero_inteiro(input('1: Fahrenheit para Celsius\n2: Celsius para Fahrenheit\n→ '))

    while tipo_conversao not in [1, 2]:
        print('Insira um tipo de conversão válido !')
        tipo_conversao = formatar_numero_inteiro(input('1: Fahrenheit para Celsius\n2: Celsius para Fahrenheit\n→ '))

    if tipo_conversao == 1:
        fahrenheit = formatar_numero(input('Insira a temperatura em fahrenheits, ex (32): '))
        consulta = conversoes['temperatura'][tipo_conversao]
        resultado = consulta['funcao'](fahrenheit)
        print(f'A conversão de {fahrenheit}{consulta["descricao"]} é {resultado:.2f}°C')
    else:
        celsius = formatar_numero(input('Insira a temperatura em graus celsius, ex (32): '))
        consulta = conversoes['temperatura'][tipo_conversao]
        resultado = consulta['funcao'](celsius)
        print(f'A conversão de {celsius}{consulta["descricao"]} é {resultado:.2f}°F')

# ── Distância ──
elif escolha_unidade == 'distancia':
    print('Insira o tipo de conversão para distância')
    tipo_conversao = formatar_numero_inteiro(input('1: KM para Milhas\n2: Milhas para KM\n→ '))

    while tipo_conversao not in [1, 2]:
        print('Insira um tipo de conversão válido !')
        tipo_conversao = formatar_numero_inteiro(input('1: KM para Milhas\n2: Milhas para KM\n→ '))

    if tipo_conversao == 1:
        quilometros = formatar_numero(input('Insira o valor em KM, ex (20): '))
        consulta = conversoes['distancia'][tipo_conversao]
        resultado = consulta['funcao'](quilometros)
        print(f'A conversão de {quilometros} {consulta["descricao"]} é {resultado:.2f} Milhas')
    else:
        milhas = formatar_numero(input('Insira o valor em milhas, ex (10): '))
        consulta = conversoes['distancia'][tipo_conversao]
        resultado = consulta['funcao'](milhas)
        print(f'A conversão de {milhas} {consulta["descricao"]} é {resultado:.2f} KM')

# ── Peso ──
else:
    print('Insira o tipo de conversão para peso')
    tipo_conversao = formatar_numero_inteiro(input('1: KG para Libras\n2: Libras para KG\n→ '))

    while tipo_conversao not in [1, 2]:
        print('Insira um tipo de conversão válido !')
        tipo_conversao = formatar_numero_inteiro(input('1: KG para Libras\n2: Libras para KG\n→ '))

    if tipo_conversao == 1:
        quilograma = formatar_numero(input('Insira o valor em KG ex (25.3): '))
        consulta = conversoes['peso'][tipo_conversao]
        resultado = consulta['funcao'](quilograma)
        print(f'A conversão de {quilograma} {consulta["descricao"]} é {resultado:.2f} Libra')
    else:
        libra = formatar_numero(input('Insira o valor em Libra ex (40): '))
        consulta = conversoes['peso'][tipo_conversao]
        resultado = consulta['funcao'](libra)
        print(f'A conversão de {libra} {consulta["descricao"]} é {resultado:.2f} KG')