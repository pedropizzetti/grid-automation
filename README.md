# Estratégias de Automação em Grid

Implementação de automação em ambiente baseado em grid, com foco em tomada de decisão local, organização espacial e otimização de processos.

---

## Contexto

O projeto foi desenvolvido em um ambiente de simulação onde cada célula de um grid representa um estado independente, exigindo decisões baseadas em contexto local e interação com vizinhos.

As entidades são plantadas, monitoradas e colhidas automaticamente, com regras específicas para cada tipo.

O ambiente fornece uma API própria com funções e entidades específicas para interação com o grid.

---

## Conceitos aplicados

- Tomada de decisão baseada em estado  
- Interação com vizinhos (grid-based logic)  
- Reorganização dinâmica de elementos  
- Automação contínua de processos  
- Separação de responsabilidades  

---

## Estrutura

O código está dividido em três camadas principais:

- **Main**  
  Responsável pelo fluxo principal e iteração sobre o grid.

- **Engine**  
  Contém funções utilitárias e regras base (preparo de solo, colheita, controle de estado).

- **Strategies**  
  Implementa comportamentos específicos para cada entidade, incluindo lógica de decisão e otimização.

---

## Estratégias

### Cactus
Reorganização baseada em comparação com vizinhos, utilizando trocas locais para manter consistência no grid.

### Outras entidades
Pumpkin, Carrot, Sunflower e Wood possuem estratégias específicas de plantio, manutenção e colheita baseadas no estado atual.

---

## Objetivo

Explorar padrões de automação e organização de sistemas em um ambiente controlado, simulando problemas de lógica, consistência e otimização.

---

## Tecnologias

- Python

---

## Referência

Projeto desenvolvido a partir de um ambiente de simulação [(*The Farmer Was Replaced*)](https://store.steampowered.com/app/2060160/The_Farmer_Was_Replaced/)
