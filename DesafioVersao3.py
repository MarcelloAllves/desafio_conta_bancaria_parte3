import textwrap
from abc import ABC, abstractclassmethod, abstractproperty, abstractmethod
from datetime import datetime
"""
1. **`textwrap`**:
   - Biblioteca usada para manipular e formatar blocos de texto.
   - Ela é útil, por exemplo, para ajustar texto longo em múltiplas linhas, limitando o 
     número de caracteres por linha.
   - Principais funções:
     - `textwrap.wrap()`: Quebra um texto longo em uma lista de strings com um comprimento 
        especificado.
     - `textwrap.fill()`: Semelhante ao `wrap()`, mas retorna o texto formatado como um 
        único bloco.

2. **`abc (Abstract Base Classes)`**:
   - Essa biblioteca é usada para criar classes abstratas em Python.
   - Classes abstratas funcionam como "esqueletos" para outras classes, definindo métodos 
     que *devem* ser implementados em subclasses.
   - Elementos chave:
     - **`ABC`**: É a classe base para todas as classes abstratas.
     - **`@abstractclassmethod`**: Define métodos abstratos que devem ser implementados nas 
       subclasses.
     - **`@abstractproperty`**: Define propriedades abstratas que devem ser implementadas.

3. **`datetime`**:
   - Essa biblioteca oferece classes para manipulação de datas e horários.
   - É amplamente usada para trabalhar com tempo, calcular diferenças entre datas e formatar 
     valores de data e hora.
   - Principais funcionalidades:
     - `datetime.now()`: Retorna a data e hora atual.
     - `datetime.strptime()`: Converte strings em objetos de data e hora, baseado em um 
        formato especificado.
     - `datetime.strftime()`: Formata objetos de data e hora para strings.

@classmethod
    . Indica que o método é um método da classe e não de instâncias específicas.
    . Ele recebe automaticamente a classe () como primeiro parâmetro, ao invés de  
      (que seria uma instância).
Por que usar um  em vez do construtor diretamente?
    . Ele permite criar instâncias de forma mais controlada e com lógica adicional
        (como validações ou ajustes nos parâmetros antes de criar o objeto).
    . Útil em cenários onde você precisa criar objetos de várias subclasses ou quer oferecer 
        uma interface simples para inicialização.

@property
    O uso do decorador  no seu código transforma métodos em propriedades de acesso somente 
    leitura, permitindo que você acesse os atributos privados _saldo, _numero, _agencia, 
    _cliente e _historico como se fossem atributos públicos, mas mantendo o controle sobre 
    como eles são acessados. 
    Vamos detalhar o que o código faz:
        1. Transformar métodos em propriedades:
            . Em vez de acessar diretamente os atributos privados (como _saldo), você pode 
              usar os métodos decorados com @property como se fossem atributos comuns.
            . Isso melhora a encapsulação e protege o acesso direto a variáveis importantes.
        2. Propriedades definidas no código:
            . saldo:     Retorna o valor do saldo.
            . numero:    Retorna o número da conta.
            . agencia:   Retorna o código da agência.
            . cliente:   Retorna o cliente associado à conta.
            . historico: Retorna o histórico de operações da conta.
Por que usar o @property?
    . Encapsulamento: Mantém os atributos _saldo, _numero, etc., privados, mas ainda permite 
      acesso controlado a eles.
    . Futuras modificações: Se precisar adicionar lógica ao acesso (como validações), 
      você pode editar os métodos decorados sem mudar a forma como eles são chamados.
      
A classe  como uma classe abstrata, usando os conceitos de Programação Orientada a Objetos (POO). 
    1. ABC (Abstract Base Class):
        . A classe  herda de , o que significa que ela é uma classe abstrata. 
          Classes abstratas servem como "modelos" que outras classes podem herdar, 
          mas não podem ser instanciadas diretamente.
        . Através do módulo  abc (Abstract Base Classes), você pode usar decoradores 
          como  @abstract e @abstractclassmethod para definir métodos que obrigatoriamente 
          devem ser implementados pelas subclasses.
    2. Propriedade abstrata valor:
        . Decorada com  @property e @abstractpropety, a propriedade valor é definida como 
          obrigatória para qualquer classe que herde de Transacao.
        . As subclasses terão que implementar a lógica de como o valor será retornado.
    3. Método abstrato registrar:
        . Decorado com @abstractclassmethod, o método registrar é outro elemento que as 
          subclasses deverão implementar.
        . Ele recebe conta como parâmetro, presumivelmente para realizar alguma operação 
          com uma conta bancária.
Benefícios dessa abordagem:
    1. Padronização: Garante que todas as subclasses de Transacao sigam a mesma estrutura, 
       promovendo consistência no código.
    2. Reutilização: Evita duplicação de código ao criar um modelo comum para diferentes 
       tipos de transação (como saque, depósito, transferência).
    3. Flexibilidade: Cada subclasse pode implementar a lógica específica para o tipo de 
       transação.
    
"""


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):

    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo.")
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\nCliente não possui conta! ")
        return None  # Retorna None explicitamente se não houver contas.

    # Exibir todas as contas disponíveis para o cliente
    print("\nContas disponíveis:")
    for i, conta in enumerate(cliente.contas, start=1):
        print(f"{i}: {conta}")  # Presume que 'conta' tem um método __str__ para exibição amigável.

    # Solicitar ao usuário que escolha uma conta
    try:
        escolha = int(input("\nDigite o número da conta desejada: "))
        if 1 <= escolha <= len(cliente.contas):
            return cliente.contas[escolha - 1]  # Retorna a conta escolhida.
        else:
            print("\n@@@ Escolha inválida! @@@")
            return None
    except ValueError:
        print("\n@@@ Entrada inválida! Por favor, insira um número. @@@")
        return None


def depositar(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # Verifica se o cliente foi encontrado
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Solicita o valor do depósito, com tratamento de exceção
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor do depósito deve ser positivo. @@@")
            return
    except ValueError:
        print("\n@@@ Entrada inválida! Por favor, insira um número válido. @@@")
        return

    # Cria uma transação de depósito
    transacao = Deposito(valor)

    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a transação
    cliente.realizar_transacao(conta, transacao)

    # Confirmação do sucesso
    print(f"\n=== Depósito de R${valor:.2f} realizado com sucesso! ===")


def sacar(clientes):
    # Solicita o CPF do cliente
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    # Verifica se o cliente foi encontrado
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    # Solicita o valor do saque com tratamento de exceções
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor <= 0:
            print("\n@@@ Operação falhou! O valor do saque deve ser positivo. @@@")
            return
    except ValueError:
        print("\n@@@ Entrada inválida! Por favor, insira um número válido. @@@")
        return

    # Cria a transação de saque
    transacao = Saque(valor)

    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a transação
    sucesso_transacao = cliente.realizar_transacao(conta, transacao)

    # Confirma sucesso ou informar falha
    if sucesso_transacao:
        print(f"\n=== Saque de R${valor:.2f} realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! Verifique seu saldo ou limites de saque. @@@")


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Obtendo a data e hora no momento da transação realizada.
    data_hora_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Cabeçalho do extrato com data e hora
    print("\n================ EXTRATO =================")
    print(f"Data e Hora: {data_hora_atual}")
    print("==========================================")

    # Processando as transações
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}\n\tData: {transacao['data']}"

    # Exibi transações e saldo
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")
    print("\n=== Extrato exibido com sucesso! ===")

    # Salva o extrato em arquivo no formato txt (opcional)
    salvar_extrato = input("Deseja salvar o extrato em arquivo? (S/N): ").strip().upper()
    if salvar_extrato == "S":
        nome_arquivo = f"extrato_{conta.numero}.txt"
        with open(nome_arquivo, "w") as arquivo:
            arquivo.write("========== EXTRATO ==========\n")
            arquivo.write(f"Data e Hora: {data_hora_atual}\n")
            arquivo.write("=============================\n")
            arquivo.write(extrato + "\n")
            arquivo.write(f"\nSaldo:\n\tR$ {conta.saldo:.2f}\n")
            arquivo.write("=============================")
        print(f"\n=== Extrato salvo no arquivo {nome_arquivo}! ===")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("\n CPF inválido! Certifique-se de que tenha 11 dígitos. ")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n Já existe cliente com esse CPF!")
        return

    nome = input("Informe o nome completo: ").strip()
    if not nome:
        print("\n Nome inválido! Certifique-se de que o campo não esteja vazio.")
        return

    try:
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        datetime.strptime(data_nascimento, "%d-%m-%Y")
    except ValueError:
        print("\nData de nascimento inválida! Use o formato dd-mm-aaaa.")
        return

    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ").strip()
    if not endereco:
        print("\nEndereço inválido! Certifique-se de que o campo não esteja vazio.")
        return

    # Confirmar os dados antes de criar o cliente
    print("\nConfirmação dos dados:")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Data de nascimento: {data_nascimento}")
    print(f"Endereço: {endereco}")
    confirmar = input("\nConfirma os dados do cliente? (S/N): ").strip().upper()
    if confirmar != "S":
        print("\nOperação cancelada pelo usuário.")
        return

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    if not cpf.isdigit() or len(cpf) != 11:
        print("\nCPF inválido! Certifique-se de que tenha 11 dígitos.")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print(f"\nCliente com CPF {cpf} não encontrado, fluxo de criação de conta encerrado!")
        return

    # Gerar número de conta automaticamente
    numero_conta = str(len(contas) + 1).zfill(6)

    # Verificar se o número da conta já existe
    if any(conta.numero == numero_conta for conta in contas):
        print("\nJá existe uma conta com esse número!")
        return

    # Criar e registrar a nova conta
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    # Mensagem de confirmação
    print("\n=== Conta criada com sucesso! ===")
    print(f"Titular: {cliente.nome}")
    print(f"Número da Conta: {conta.numero}")


def listar_contas(contas):
    if not contas:
        print("\nNenhuma conta encontrada!")
        return

    for i, conta in enumerate(contas, start=1):
        print("=" * 100)
        print(f"Conta {i}:")
        try:
            print(textwrap.dedent(str(conta)))
        except Exception as e:
            print(f"\nErro ao exibir a conta: {e}")



def menu_cadastro(clientes, contas):
    while True:
        menu_cadastro_texto = """\n
        ########## MENU CADASTRO ##########
        [1]    CADASTRAR UM NOVO USUÁRIO
        [2]    ABRIR NOVA CONTA
        [0]    SAIR DO SISTEMA BANCÁRIO
        OPÇÃO: """
        try:
            opcao = int(input(textwrap.dedent(menu_cadastro_texto)))
        except ValueError:
            print("\nEntrada inválida! Por favor, insira um número válido.")
            continue

        if opcao == 1:
            criar_cliente(clientes)
        elif opcao == 2:
            criar_conta(clientes, contas)
        elif opcao == 0:
            print("\n=== Saindo do menu de cadastro. ===")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")



def menu_usuario(clientes):
    while True:  # Mantém o menu ativo até o usuário escolher sair
        menu_usuario = """\n
        ########## MENU USUÁRIO ##########
            [1]    DEPOSITAR
            [2]    SACAR
            [3]    EXIBIR EXTRATO
            [4]    EXIBIR TODAS AS CONTAS DE UM USUÁRIO
            [0]    SAIR DO MENU USUÁRIO
        OPÇÃO: """
        try:
            opcao = int(input(textwrap.dedent(menu_usuario)))
        except ValueError:
            print("\nEntrada inválida! Por favor, insira um número válido.")
            continue

        if opcao == 1:
            depositar(clientes)
        elif opcao == 2:
            sacar(clientes)
        elif opcao == 3:
            exibir_extrato(clientes)
        elif opcao == 4:
            # Exibe todas as contas de um cliente específico
            cpf = input("Informe o CPF do cliente: ")
            cliente = filtrar_cliente(cpf, clientes)
            if cliente:
                for conta in cliente.contas:
                    print(conta)
            else:
                print("\nCliente não encontrado!")
        elif opcao == 0:
            print("\n=== Saindo do menu usuário. Até logo! ===")
            break
        else:
            print("\nOpção inválida! Por favor, escolha uma opção válida.")


def main():
    clientes = []  # Lista para armazenar clientes
    contas = []  # Lista para armazenar contas

    while True:
        cpf_cliente = input("Favor informar o CPF (somente números):\t")

        # Validação do CPF
        if not cpf_cliente.isdigit() or len(cpf_cliente) != 11:
            print("\nCPF inválido! Certifique-se de que tenha 11 dígitos.")
            continue

        cliente = filtrar_cliente(cpf_cliente, clientes)

        if cliente:
            print(f"\nBem-vindo, {cliente.nome}!")
            menu_usuario(clientes)  # Passa os clientes para o menu de usuários
        else:
            print("\nCliente não encontrado! Redirecionando para o cadastro.")
            menu_cadastro(clientes, contas)

        # Opção de sair
        sair = input("\nDeseja encerrar o programa? (S/N): ").strip().upper()
        if sair == "S":
            print("\n=== Encerrando o sistema bancário. Até logo! ===")
            break
main()