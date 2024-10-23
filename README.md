# Ortiz's Essay Writer (OEM)

### O que é?
**Ortiz's Essay Writer** (OEM) é um pequeno programa em Python que automatiza a digitação, escrevendo todo o texto do arquivo `textoredacao.txt`. Ele foi projetado para ajudar os usuários a automatizar tarefas repetitivas de digitação, sendo especialmente útil para entradas de texto longas.

### Como instalar
Para instalar o OEM, você precisará do Python instalado em sua máquina, juntamente com uma biblioteca `keyboard`. Você pode instalar essa biblioteca usando o pip:

```bash
$ pip install keyboard
```

### Como usar

1. **Prepare o texto**: Coloque o texto que você deseja digitar automaticamente dentro do arquivo `textoredacao.txt`.
   
2. **Ajuste o atraso na digitação (opcional)**: Se o seu computador for lento ou você quiser controlar a velocidade de digitação, é possível definir um atraso entre cada caractere. Ao executar o programa, ele pedirá para você inserir um tempo de atraso (em segundos). Insira `0` para nenhum atraso ou um valor maior para desacelerar a digitação.

3. **Execute o programa**: Abra o prompt de comando no diretório onde o `essayWriter.py` está localizado e execute o seguinte comando:

```bash
$ py essayWriter.py
```

4. **Inicie a digitação**: Quando o script começar, clique na caixa de texto onde você deseja que o texto seja digitado (por exemplo, um documento ou campo de texto no navegador). Em seguida, pressione `1` no teclado para acionar o processo de digitação.

### Personalização

- **Alterar tecla de ativação**: Por padrão, o script começa a digitar quando você pressiona `1`. Você pode alterar essa tecla de ativação para qualquer outra, modificando a linha `keyboard.wait("1")` no código.
  
- **Tempo de atraso**: Se você estiver enfrentando lentidão, pode alterar o `DelayTime` dentro do script ou quando solicitado, tornando o processo de digitação mais suave para máquinas mais lentas.

> [!NOTE]
> Se o seu computador tiver desempenho inferior, a digitação pode ter atraso ao pressionar `1`. Você pode ajustar o atraso inserindo um valor maior quando solicitado ou modificando o parâmetro `DelayTime` no código.