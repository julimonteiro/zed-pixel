# Zed Pixel

Aplicativo instalado em `/Applications/Zed Pixel.app`. Abra pelo Finder ou use `zedpixel`. O Zed oficial e o comando `zed` continuam disponíveis.

Tema Pixel Arcade escuro, fonte VT323 na interface/editor, MesloLGM Nerd Font Mono no terminal, ícones de arquivos e logo em pixel art. As seis cores dos delimitadores distinguem níveis de `()`, `{}` e `[]`, conforme o parser da linguagem; depois se repetem. O tema não transforma todos os controles internos em sprites.

## Consultar CSV

1. Abra o CSV no editor. As colunas recebem cores pela extensão Rainbow CSV.
2. Abra a paleta (`Cmd+Shift+P`), execute `task: spawn` e escolha **CSV: Query RBQL (SELECT a1)**.
3. No terminal, digite uma consulta e pressione Enter:

```sql
SELECT a1
SELECT a1, a3
SELECT a1, a3 WHERE int(a3) > 1
```

Execute uma consulta por vez. `a1` é a primeira coluna, `a2` a segunda. Não é preciso `FROM`. O resultado aparece no terminal e é salvo em um arquivo separado em `~/Library/Application Support/ZedPixel/query-results/`; o caminho aparece no terminal. Execute a tarefa novamente para outra consulta.

A tarefa salva o CSV aberto antes da consulta e pressupõe cabeçalho. Em arquivos sem cabeçalho, acrescente `WITH (noheader)` ao final da consulta. O delimitador é detectado automaticamente. A integração usa RBQL com expressões Python; por isso, conversões numéricas usam `int(a3)` ou `float(a3)`.

## Fork local

Código em `/Users/jumonteiro/Documents/zed`, branch `pixel-local`. Login Zed, serviços hospedados pagos, ofertas de assinatura, colaboração pelos servidores Zed e atualizador oficial desativados na versão local. APIs próprias, agentes externos e modelos locais permanecem disponíveis; serviços externos podem cobrar pelo uso.

Perfil separado em `~/Library/Application Support/ZedPixel`, incluindo configurações, extensões, dados e ferramentas RBQL. Não há atualização automática; futuras atualizações do fork exigem nova compilação.

## Verificação

Compilação otimizada concluída. 155 testes de client, language_models e paths passaram. Assinatura local do aplicativo validada. Consultas RBQL `SELECT a1` e filtro numérico verificadas; o fluxo interativo mostra e salva o resultado sem modificar o CSV original. A abertura da tarefa pela interface não foi exercitada para não interromper a sessão em uso.

O arquivo `Zed Pixel.zip`, ao lado desta pasta, contém o aplicativo assinado. O perfil e a ferramenta RBQL foram configurados neste Mac e não estão incluídos no ZIP.
