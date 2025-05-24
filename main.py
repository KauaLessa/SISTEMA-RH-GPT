import tkinter as tk
from tkinter import scrolledtext
import re

# Armazena as respostas do candidato
dados_candidato = {
    "experiencia": None,
    "formacao": None,
    "ingles": None,
    "habilidades": None,
    "pretensao": None,
    "disponibilidade": None
}

etapa = 0  # Etapa da entrevista

# Converte palavras para números
def extrair_numero(resposta):
    mapeamento = {
        "um": 1, "dois": 2, "três": 3, "quatro": 4,
        "cinco": 5, "seis": 6, "sete": 7, "oito": 8,
        "nove": 9, "dez": 10
    }
    numeros = re.findall(r'\d+', resposta)
    if numeros:
        return int(numeros[0])
    for palavra, valor in mapeamento.items():
        if palavra in resposta.lower():
            return valor
    return None

# Avalia o candidato com base nas respostas
def avaliar_candidato(dados):
    if None in dados.values():
        return "Erro", "Informações incompletas."

    pontos = 0
    if dados["experiencia"] >= 3:
        pontos += 2
    elif dados["experiencia"] >= 1:
        pontos += 1

    if dados["formacao"] in ["superior", "graduado", "graduação"]:
        pontos += 2
    elif dados["formacao"] == "técnico":
        pontos += 1

    if dados["ingles"] in ["avançado", "fluente"]:
        pontos += 2
    elif dados["ingles"] == "intermediário":
        pontos += 1

    if "python" in dados["habilidades"]:
        pontos += 1
    if dados["pretensao"] <= 6000:
        pontos += 1
    if dados["disponibilidade"] in ["imediata", "agora", "disponível"]:
        pontos += 1

    if pontos >= 7:
        return "Aprovado", f"O candidato atendeu a quase todos os critérios com {pontos} pontos."
    elif pontos >= 4:
        return "Aprovado parcialmente", f"O candidato tem perfil mediano, com {pontos} pontos."
    else:
        return "Reprovado", f"Poucos critérios foram atendidos, total de {pontos} pontos."

# Processa cada resposta
def processar_resposta(resposta):
    global etapa

    resposta = resposta.lower()

    if etapa == 1:
        anos = extrair_numero(resposta)
        if anos is not None:
            dados_candidato["experiencia"] = anos
            etapa += 1
            return "Qual sua formação? (superior, técnico, graduação etc.)"
        else:
            return "Informe sua experiência em anos (ex: 'trabalhei por 3 anos')."

    elif etapa == 2:
        if any(palavra in resposta for palavra in ["superior", "graduação", "graduado"]):
            dados_candidato["formacao"] = "superior"
        elif "técnico" in resposta or "tecnico" in resposta:
            dados_candidato["formacao"] = "técnico"
        else:
            dados_candidato["formacao"] = "nenhuma"
        etapa += 1
        return "Qual seu nível de inglês? (básico, intermediário, avançado, fluente)"

    elif etapa == 3:
        if any(n in resposta for n in ["avançado", "fluente"]):
            dados_candidato["ingles"] = "avançado"
        elif "intermediário" in resposta:
            dados_candidato["ingles"] = "intermediário"
        else:
            dados_candidato["ingles"] = "básico"
        etapa += 1
        return "Liste algumas de suas habilidades técnicas (ex: Python, Java, SQL...)"

    elif etapa == 4:
        dados_candidato["habilidades"] = resposta
        etapa += 1
        return "Qual sua pretensão salarial? (ex: 5000)"

    elif etapa == 5:
        valor = extrair_numero(resposta)
        if valor:
            dados_candidato["pretensao"] = valor
            etapa += 1
            return "Qual sua disponibilidade para início? (imediata, 15 dias, etc.)"
        else:
            return "Informe um valor numérico para a pretensão salarial (ex: 4500)."

    elif etapa == 6:
        dados_candidato["disponibilidade"] = resposta
        status, justificativa = avaliar_candidato(dados_candidato)
        etapa += 1
        return f"{status.upper()}.\nJustificativa: {justificativa}"

    else:
        return "Entrevista finalizada. Reinicie o sistema para nova avaliação."

# Responde no chat
def responder(event=None):  # event=None permite chamar com botão ou tecla
    entrada = entrada_usuario.get().strip()
    if not entrada:
        return
    chat_log.insert(tk.END, "Você: " + entrada + "\n")
    resposta_bot = processar_resposta(entrada)
    chat_log.insert(tk.END, "IA: " + resposta_bot + "\n\n")
    entrada_usuario.delete(0, tk.END)

# Inicia a entrevista
def iniciar_entrevista():
    global etapa, dados_candidato
    etapa = 1
    for k in dados_candidato:
        dados_candidato[k] = None
    mensagem = (
        "Bem-vindo ao Sistema de Triagem de Candidatos!\n"
        "Faremos uma entrevista rápida para entender melhor seu perfil.\n"
        "Ao final, você será classificado como APROVADO, APROVADO PARCIALMENTE ou REPROVADO.\n"
        "Vamos começar!\n\n"
        "IA: Quantos anos de experiência você possui?"
    )
    chat_log.insert(tk.END, mensagem + "\n\n")

# Interface gráfica
janela = tk.Tk()
janela.title("Sistema de RH Inteligente")

chat_log = scrolledtext.ScrolledText(janela, width=80, height=25, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10)

entrada_usuario = tk.Entry(janela, width=80)
entrada_usuario.pack(padx=10, pady=(0, 5))

entrada_usuario.bind("<Return>", responder)  # <-- Aqui ativamos o Enter

botao_enviar = tk.Button(janela, text="Responder", command=responder)
botao_enviar.pack(pady=(0, 10))

iniciar_entrevista()
janela.mainloop()