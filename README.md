<div align="center">

# 🚤 EnjoyTagus — Agendamento de Passeios de Barco

**Projeto da unidade curricular de Programação I**

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Ano letivo](https://img.shields.io/badge/ano%20letivo-2022%2F2023-blue)
![Estado](https://img.shields.io/badge/estado-conclu%C3%ADdo-success)

</div>

---

## 📋 Índice

- [Sobre o projeto](#-sobre-o-projeto)
- [Informação académica](#-informação-académica)
- [Funcionalidades](#-funcionalidades)
- [Estrutura do projeto](#-estrutura-do-projeto)
- [Pré-requisitos](#-pré-requisitos)
- [Como executar](#-como-executar)
- [Formato dos ficheiros](#-formato-dos-ficheiros)
- [Regras de atribuição](#-regras-de-atribuição)
- [Conjuntos de teste](#-conjuntos-de-teste)
- [Autores](#-autores)

---

## 📖 Sobre o projeto

O **EnjoyTagus** é uma aplicação de linha de comandos, escrita em **Python**, que gere a agenda de passeios de barco no Tejo da empresa fictícia *Tagus Sailing*.

A cada atualização (de 30 em 30 minutos), o programa lê:

1. a lista de **skippers** e a respetiva disponibilidade;
2. a **agenda** de passeios já marcados;
3. os novos **pedidos** de passeio dos clientes;

e produz a nova agenda e a lista de skippers atualizada para o instante seguinte, atribuindo cada pedido ao skipper mais adequado.

---

## 🎓 Informação académica

| | |
|---|---|
| **Unidade curricular** | Programação I |
| **Instituição** | Faculdade de Ciências da Universidade de Lisboa (FCUL) |
| **Curso** | Licenciatura em Tecnologias de Informação (LTI) |
| **Ano letivo** | 2022/2023 — 1.º ano, 1.º semestre |
| **Grupo** | 131 |
| **Data de entrega** | 18 de dezembro de 2022 |

---

## ✨ Funcionalidades

- Leitura e validação de ficheiros de skippers, agenda e pedidos.
- Remoção da agenda dos passeios que já terminaram.
- Atribuição automática de cada pedido ao skipper mais adequado (idioma, nível, especialização, horas disponíveis).
- Passagem dos passeios para o dia seguinte quando ultrapassam o horário de funcionamento (08:00–20:00).
- Marcação como `not-assigned` dos pedidos sem skipper compatível.
- Escrita dos novos ficheiros `scheduleHHhMM.txt` e `skippersHHhMM.txt` para o instante seguinte (+30 min).
- Deteção de inconsistências entre o nome do ficheiro e o seu cabeçalho.

---

## 🗂️ Estrutura do projeto

```text
EnjoyTagus131/
├── update.py             # Ponto de entrada: lê os argumentos e corre a aplicação
├── scheduling.py         # Lógica de atualização da agenda e atribuição de skippers
├── readingFromFiles.py   # Leitura dos ficheiros de entrada (skippers, agenda, pedidos)
├── writingToFiles.py     # Escrita dos ficheiros de saída
├── dateTime.py           # Funções auxiliares para datas e horas
├── constants.py          # Constantes (índices dos campos, nº de linhas do cabeçalho, ...)
└── testSets/             # Conjuntos de teste com entradas e saídas esperadas
    ├── testSet1/
    ├── testSet2/
    ├── testSet3/
    └── testSet4/
```

---

## ⚙️ Pré-requisitos

- **Python 3.11** ou superior
- Nenhuma biblioteca externa (apenas a biblioteca standard)

Verificar a versão instalada:

```bash
python --version
```

---

## 🚀 Como executar

### 1. Clonar o repositório

```bash
git clone https://github.com/pedrorosa3/EnjoyTagus131.git
cd EnjoyTagus131
```

### 2. Correr o programa

O script `update.py` recebe **três argumentos**, por esta ordem:

```bash
python update.py <ficheiro_skippers> <ficheiro_agenda> <ficheiro_pedidos>
```

**Exemplo** com o primeiro conjunto de teste:

```bash
python update.py testSets/testSet1/skippers17h00.txt testSets/testSet1/schedule17h00.txt testSets/testSet1/requests17h00.txt
```

### 3. Resultado

São criados dois ficheiros **na pasta a partir da qual o comando foi executado**, com a hora seguinte no nome:

```text
schedule17h30.txt
skippers17h30.txt
```

> [!NOTE]
> Os ficheiros de saída são escritos na pasta atual. Se correr o programa dentro de uma pasta `testSets/testSetN`, os ficheiros com as saídas esperadas serão substituídos.

---

## 📄 Formato dos ficheiros

Todos os ficheiros começam com um cabeçalho de 7 linhas:

```text
Company:
Tagus Sailing
Day:
07:11:2022
Time:
17:00
Skippers:          ← ou Schedule: / Requests:
```

O nome do ficheiro tem de ser coerente com o cabeçalho (ex.: `skippers17h00.txt` → `Skippers:` e `17:00`).

### Skippers

```text
Nome, (idiomas), nível, preço/hora, especialização, máx. horas, horas acumuladas, (data fim, hora fim)
Ana Amaral, (english; french; portuguese), 1*, 40, price, 20, 12, (08:11:2022, 12:30)
```

### Agenda (schedule)

```text
Data, hora, duração, skipper, preço, cliente
07:11:2022, 14:00, 4, Carlos Santos, 400, Francisca de Jong
```

### Pedidos (requests)

```text
Cliente, (idiomas), nível, especialização, duração
Vladislav Maraev, (english; russian), 2*, price, 2
```

---

## 🧭 Regras de atribuição

Um skipper só pode receber um pedido se:

- tiver o **mesmo nível** (`1*`, `2*`, `3*`) e a **mesma especialização** (`price`, `comfort`, `speed`) pedidos;
- falar **pelo menos um** dos idiomas do cliente;
- não ultrapassar o seu **limite de horas** com o novo passeio.

Entre os skippers compatíveis, é escolhido o que fica livre **mais cedo**; em caso de empate, o **mais barato**, depois o com **menos horas acumuladas** e, por fim, por **ordem alfabética**.
Se o passeio terminar depois das 20:00, passa para o dia seguinte às 08:00.

---

## 🧪 Conjuntos de teste

Cada pasta em `testSets/` contém os ficheiros de entrada (`HHh00`) e as saídas esperadas (`HHh30`).

| Conjunto | Entrada | Observações |
|---|---|---|
| `testSet1` | 17h00 | Caso geral, inclui um pedido `not-assigned` |
| `testSet2` | 18h00 | Caso geral |
| `testSet3` | 10h00 | Caso geral |
| `testSet4` | 13h00 | Caso de erro: hora no cabeçalho não corresponde ao nome do ficheiro |

---

## 👥 Autores

| Nº | Nome |
|---|---|
| 62904 | **Pedro Rosa** — [@pedrorosa3](https://github.com/pedrorosa3) |
| 60290 | **João Martins** |

---

<div align="center">
<sub>Projeto académico desenvolvido no âmbito de Programação I · Tecnologias de Informação · FCUL · 2022/2023</sub>
</div>
