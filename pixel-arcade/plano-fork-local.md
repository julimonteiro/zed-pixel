# Fork local do Zed: plano de implementação

**Objetivo:** remover conta Zed, assinaturas e serviços pagos hospedados pelo Zed, preservando o editor, Git local, extensões, CSV, terminal, tema Pixel Arcade, modelos locais e APIs próprias.

**Arquitetura:** criar uma política central para o modo local, aplicada à inicialização dos serviços e aos pontos de entrada da interface. Não simular planos pagos nem alterar autorizações de servidores. Manter autenticações independentes de provedores externos.

**Tecnologias:** Rust, GPUI, Cargo e Metal/macOS.

## Restrições

- A versão instalada em /Applications/Zed.app é oficial e deve continuar disponível até o fork passar nos testes.
- Preservar as licenças e os avisos do projeto original.
- Preservar configurações e dados existentes.
- Separar identidade, configuração e atualizações do fork para que uma atualização oficial não o substitua.
- Nada de habilitar capacidades pagas em servidores remotos por alteração de flags locais.

## Revisão prioritária

1. Inicialização sem credenciais e sem rede não pode solicitar login.
2. URLs de autenticação e ações de comandos não podem reabrir o fluxo removido.
3. Configurações antigas que selecionam IA hospedada devem apresentar alternativa local, sem cobrança ou falha de inicialização.
4. APIs próprias e modelos locais devem permanecer utilizáveis.
5. O fork deve carregar as personalizações existentes e manter o aplicativo oficial disponível.

## Tarefas

- [ ] Criar política central de serviços locais e testes unitários para conta, cobrança, colaboração hospedada e provedor cloud indisponíveis; APIs e modelos locais disponíveis.
- [ ] Verificar falha dos testes antes de implementar a política.
- [ ] Aplicar a política em crates/client/src/client.rs, incluindo SignIn, reconexão, credenciais Zed e sign_in_with_optional_connect.
- [ ] Remover o registro de CloudLanguageModelProvider em crates/language_models/src/language_models.rs no fork e testar os provedores restantes.
- [ ] Mapear e remover pontos de login, upgrade, cobrança e previsões Zed em title_bar, agent_ui, onboarding, menus, paleta de comandos e configurações; testar ausência dos pontos de entrada.
- [ ] Desativar colaboração hospedada e fluxos que dependem da conta Zed. Preservar SSH e Git independentes.
- [ ] Definir identidade e diretórios próprios do fork e impedir o atualizador oficial de substituir seu binário.
- [ ] Compilar em macOS, executar testes das crates alteradas e verificações de formatação, depois testar inicialização sem conta e sem rede.
- [ ] Empacotar aplicativo separado, aplicar Pixel Arcade e testar colchetes, CSV, SELECT pelo DuckDB e terminal com Nerd Font.

## Estado verificado

Somente as opções públicas de title_bar foram alteradas na instalação atual: show_sign_in, show_user_menu, show_user_picture e show_onboarding_banner = false. Essas opções ocultam controles; não removem os serviços do aplicativo.

A implementação do fork ainda não começou. Não há Cargo/Rust instalado e xcrun não encontra metal. xcode-select aponta para /Library/Developer/CommandLineTools. A documentação do repositório exige Xcode completo com componentes macOS para compilar.

Próximo requisito externo: instalar Xcode pelo App Store/Apple Developer e concluir a configuração inicial. Depois instalar o toolchain Rust indicado por rust-toolchain.toml e CMake, executar os testes e implementar as tarefas acima.
