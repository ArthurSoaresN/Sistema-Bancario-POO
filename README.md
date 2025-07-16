# Atividade Prática: Modelagem em POO - Sistema Bancário

Atividade para entender os conceitos fundamentais da Programação Orientada a Objetos (POO) através da modelagem de um sistema bancário básico em Python.

## Conceitos de POO Abordados



* **Classes e Objetos**: `Cliente`, `Conta`, `Transacao` são classes que servem como "moldes" para criar objetos (instâncias) com características (atributos) e comportamentos (métodos) específicos.

* **Encapsulamento**: Atributos como `_saldo`, `_numero` são protegidos (indicados pelo `_`), sendo acessados ou modificados apenas por métodos específicos (`sacar`, `depositar`, `@property`). Isso garante a integridade dos dados.

* **Herança**:

    * `PessoaFisica` **herda** de `Cliente`, reutilizando suas funcionalidades e adicionando características específicas de uma pessoa física (nome, CPF, data de nascimento).

    * `ContaCorrente` **herda** de `Conta`, especializando o comportamento de saque com limites e contagem de saques.

    * `Saque` e `Deposito` **herdam** de `Transacao`, compartilhando a estrutura básica de uma transação.

* **Polimorfismo**: O método `sacar` é um bom exemplo. A classe `Conta` tem um `sacar` genérico, mas `ContaCorrente` **reimplementa** (`sobrescreve`) esse método com regras adicionais (limite de saque e número de saques). Isso significa que `sacar` se comporta de forma diferente dependendo do tipo de conta.

* **Abstração (com `abc` - Abstract Base Classes)**: A classe `Transacao` é uma classe abstrata (definida com `ABC` e `@abstractmethod`). Isso significa que ela não pode ser instanciada diretamente, mas força as classes que a herdam (`Saque`, `Deposito`) a implementar seus métodos abstratos (`valor`, `registrar`). Isso garante que todas as transações sigam um padrão.