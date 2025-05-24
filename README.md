# SISTEMA-RH-GPT

Mini-projeto educativo desenvolvido para simulação de processos seletivos via interface gráfica em Python. Este mini-projeto foi desenvolvido durante a disciplina ECOM031 - INTELIGÊNCIA ARTIFICIAL. Este projeto é um sistema de entrevista automatizada que avalia candidatos com base em critérios pré-definidos de experiência, formação e competências. Desenvolvido para estudos de processamento básico de linguagem natural em aplicações de RH. Projeto acadêmico sem vinculação a processos reais de seleção.

---

## EQUIPE:
1. Kauã Lessa Lima dos Santos
2. Luís Felipe Barros Pacheco
3. Diêgo de Araujo Correia

---

## PRÉ-REQUISITOS E INSTALAÇÃO

* Python 3.6 ou superior
* Biblioteca Tkinter (incluída na instalação padrão do Python)
* Em sistemas Linux, caso necessário instalar o Tkinter:
  ```bash
  sudo apt-get install python3-tk
  ```

---

## COMO CLONAR E EXECUTAR

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/KauaLessa/SISTEMA-RH-GPT
   cd SISTEMA-RH-GPT
   ```

2. **(Opcional) Ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Execute o sistema:**
   ```bash
   python main.py
   ```

*Requer ambiente com suporte a interface gráfica.*

---

## FUNCIONAMENTO PRINCIPAL

* Interface conversacional estilo chat
* Fluxo de 6 etapas de questionamento:
  1. Experiência profissional (anos)
  2. Formação acadêmica
  3. Nível de inglês
  4. Habilidades técnicas
  5. Pretensão salarial
  6. Disponibilidade
* Sistema de pontuação automática:
  - Até 7 pontos: Aprovado
  - 4-6 pontos: Aprovado parcialmente
  - Menos de 4: Reprovado
* Reconhecimento de números escritos por extenso
* Tratamento de variações linguísticas (ex: "técnico" vs "tecnico")

---

## EXEMPLO DE INTERAÇÃO

```
IA: Quantos anos de experiência você possui?
Você: Trabalhei por três anos
IA: Qual sua formação?
Você: Superior em ADS
IA: Qual seu nível de inglês?
Você: intermediário
... [continua]
IA: APROVADO PARCIALMENTE.
Justificativa: O candidato tem perfil mediano, com 5 pontos.
```

---

## ESTRUTURA DO PROJETO

* Sistema de mapeamento de palavras para valores numéricos
* Lógica de extração de dados de respostas textuais
* Critérios de avaliação configuráveis no código-fonte
* Interface gráfica responsiva com histórico de conversa
* Armazenamento estruturado de dados do candidato
* Validação de respostas em tempo real

---

## IMPORTANTE

* Projeto exclusivamente educacional
* Não substitui análise humana em processos seletivos
* Base de regras simplificada para fins didáticos
* Funciona melhor com respostas objetivas
* Sensível a variações de escrita (usar minúsculas sem acentos)
* Valores salariais devem ser informados numericamente (ex: 5000)
