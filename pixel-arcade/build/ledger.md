# Implementation ledger

- Client regression: original production client invoked authentication callback (RED). Local production policy added, sign-in/browser/credential entry points guarded; all 23 client tests pass (GREEN).
- Provider regression: original registry still exposed Zed cloud (RED). Production cloud provider omitted; all 131 language_models tests pass (GREEN), including local/API provider retention.
- Profile regression: custom profile wrote logs under Library/Logs/Zed (RED). Custom profile now covers data, config, logs, cache and state; paths isolation test passes (GREEN).
- UI: removed account action registration, sign-in/account/onboarding controls, hosted collaboration panel/menu, Zed edit prediction provider and upsells in local mode. Hosted channel URL flow gated.
- Updates: local initialization sets an empty updater global and registers no update actions. Packaging wrapper additionally sets the update explanation.
- Identity: separate Zed Pixel app bundle ID and default profile, also selected in direct/CLI/crash-handler launches. CLI installed under zedpixel; upstream zed scheme registration removed.
- Branding: source and all macOS channel app icons changed to grid-drawn logo, ICNS generated.
- Review: independent review found shared state paths, missing companion CLI, a stale collaboration menu, updater bypass, scheme registration and crash-handler order; all material findings addressed. Minor: explicit alternate --user-data-dir is not propagated to crash handler, which uses default ZedPixel logs, preserving official isolation.
- Full optimized build and packaged Finder/CLI/restart smoke checks pending.

## Resultado final
Compilação release-fast e 155 testes concluídos. Aplicativo Zed Pixel instalado, assinado localmente e arquivado em ZIP. CSV alterado para RBQL com SELECT a1, resultado separado do original.
