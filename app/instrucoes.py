v='''
Manual de Instruções: Sistema para Gerar Nomes de Guerra

Este manual descreve como usar o sistema desenvolvido em Python com a biblioteca CustomTkinter para gerar nomes de guerra com base em um arquivo Excel fornecido. Siga os passos abaixo para compreender e operar o sistema.

---

1. Interface Inicial
Elementos visíveis:

1.1. **Botão de Informação:**  
   Localizado no canto superior direito (ícone "i"), clique para abrir o manual de instruções do sistema.

1.2. **Campo de Arquivo com os Nomes:**  
   Uma entrada onde será exibido o caminho do arquivo Excel escolhido.

1.3. **Botão de Pesquisa de Arquivo:**  
   Clique para abrir uma janela que permitirá selecionar o arquivo Excel contendo os nomes.

1.4. **Menu Suspenso "Selecionar Coluna":**  
   Após carregar um arquivo, será possível selecionar a coluna desejada.

1.5. **Botão "Iniciar":**  
   Executa o processo de geração de nomes.

1.6. **Configurações Avançadas:**  
   Define opções personalizadas para a geração de nomes, como:
   - **Limite de Caracteres:** Define o tamanho máximo dos nomes.
   - **Desordenado:** Permite gerar nomes utilizando geração aleatória, não seguindo a ordem do nome completo.
   - **Comparar Existentes:** Verifica os nomes gerados em relação a uma lista de documento excel já existente.

---

2. Adicionando o Arquivo com os Nomes

2.1. Clique no botão verde de pesquisa ao lado do campo *"Caminho do arquivo Excel"*.  
   Uma janela será aberta para você selecionar o arquivo excel.
   
2.2. Escolha o arquivo Excel contendo os nomes que serão utilizados para a geração. Certifique-se de que ele tem colunas com dados válidos.

2.3. Após selecionar o arquivo:
   - O caminho do mesmo será exibido no campo correspondente.
   - As colunas do arquivo aparecerão no menu suspenso "Selecionar Coluna".

2.4. Escolha a coluna desejada no menu suspenso.  
   **Exemplo:** Se o Excel contém uma coluna chamada "Nomes Completos", selecione-a.

---

3. Configurações Avançadas
    Personalizando a Geração:

3.1. **Limite de Caracteres:**  
   Ajuste o número mínimo e máximo de caracteres para os nomes gerados.  
   Use as setas ou o campo numérico no menu de configurações.

3.2. **Desordenado:**  
   Ative a caixa de seleção para gerar os nomes em ordem aleatória.

3.3. **Comparar Existentes:**  
   Se desejar comparar os novos nomes com uma lista já existente, ative esta opção.

   - Clique em **"Iniciar"**:  
     Será aberta uma nova janela para selecionar um arquivo quer contenha os nomes de guerra existentes.
   - Após carregar o arquivo, e você poderá confirmar.

---

4. Iniciando a Geração

4.1. Certifique-se de que todas as configurações e arquivos estão configurados.
4.2. Clique no botão **"Iniciar"**.  
   O sistema confirmará a ação com uma mensagem. Responda **"Sim"** para começar o processo.

---

5. Solução de Problemas
    Erros Comuns:

5.1. **Erro: "Arquivo não encontrado":**  
   Certifique-se de que o caminho do arquivo está correto.

5.2. **Erro: "Arquivo sem colunas":**  
   O arquivo Excel deve conter ao menos uma coluna com dados válidos.

5.3. **Erro ao abrir o arquivo:**  
   Verifique se o arquivo está no formato Excel (.xls ou .xlsx).

5.4. **Botão "Iniciar" desativado:**  
   Certifique-se de que:
   - Um arquivo foi selecionado.
   - Uma coluna foi escolhida.

5.5. **Erro: "Permissão negada:**  
   Verifique se o arquivo está aberto em outro programa ou em segundo plano, se sim, certifique-se que o arquivo esteja fechado e tente rodar o sistema novamente).

---

6. Finalização

Ao término do processo de geração, os nomes serão criados conforme as configurações. Os nomes de guerra gerados serão salvos no mesmo arquivo em uma coluna a direita da selecionada no início da operação.

Para mais informações, entre em contato com o desenvolvedor(Se ele ainda estiver no exército, se não... boa sorte! ).


7. Dúvidas

7.1. **Como a geração funciona?:**
   A geração funciona pelo método de Combinação em que 'n' é a quantidade de palavras em um nome completo. É utilizado a fórmula [ C(n) = 2.n(n+1)/2 ] ou seja:
   em um nome com 4 palavras, respeitando a ordem seriam possíveis 10 combinações.

   Quando pressionado o checkbox [Item 3.2 deste manual], a ordem das palavras é ignorada, mudando a fórmula para uma Permutação onde 'n' é o numero de palavras em um nome completo. A fórmula passa a ser [ P(n) = n! ] ou seja:
   em um nome com 4 palavras, NÃO respeitando a ordem seriam possíveis 24 combinações.


---

**© 2024 - Nathan da Cruz Cardoso / Sd Ep Cruz / Cia C GUEs-9ªBda Inf Mtz**  
Agradeço por utilizar este sistema!
(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ 

'''