# Przewodnik delegowania zadań do agentów

## Wprowadzenie

GitHub Copilot oferuje możliwość delegowania zadań do specjalistycznych agentów, które mogą automatycznie wykonywać różnorodne operacje w repozytorium. Ta funkcjonalność jest szczególnie przydatna w zarządzaniu dokumentacją, jakiej używamy w repozytorium sylabusów.

## Metody delegowania zadań

### 1. Z poziomu GitHub CLI

GitHub CLI (`gh`) umożliwia interakcję z repozytorium bezpośrednio z terminala:

```bash
# Instalacja GitHub CLI (jeśli jeszcze nie zainstalowane)
# Na macOS:
brew install gh

# Na Linux:
sudo apt install gh

# Logowanie do GitHub
gh auth login

# Przykłady użycia:
# Utworzenie issue
gh issue create --title "Aktualizacja sylabusu" --body "Opis zadania dla agenta"

# Utworzenie pull requesta
gh pr create --title "Automatyczna aktualizacja" --body "Zmiany wprowadzone przez agenta"

# Uruchomienie workflow
gh workflow run nazwa-workflow.yml
```

### 2. Poprzez GitHub API

Możesz także używać GitHub API bezpośrednio z konsoli:

```bash
# Ustawienie tokena (utwórz token w Settings > Developer settings > Personal access tokens)
export GITHUB_TOKEN="twój_token"

# Przykład: Utworzenie issue poprzez API
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/IS-UMK/sylabusy/issues \
  -d '{"title":"Zadanie dla agenta","body":"Opis zadania","labels":["automation"]}'
```

### 3. GitHub Actions Workflows

Możesz skonfigurować automatyczne workflow w katalogu `.github/workflows/`:

```yaml
name: Automatyczna walidacja sylabusów

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Sprawdź formatowanie Markdown
        run: |
          # Walidacja dokumentów
          for file in *.md; do
            echo "Sprawdzanie $file"
            # Tutaj można dodać więcej sprawdzeń
          done
```

## Przykładowe scenariusze użycia

### Automatyczna walidacja dokumentów

Agent może sprawdzać:
- Poprawność formatowania Markdown
- Kompletność sekcji w sylabusach
- Linki i referencje
- Spójność struktury między różnymi sylabusami

### Generowanie raportów

Agenty mogą automatycznie generować:
- Podsumowania zmian w sylabusach
- Statystyki dotyczące zawartości
- Listy tematów poruszanych w poszczególnych kursach

### Wsparcie w aktualizacjach

- Automatyczne sugestie poprawek
- Identyfikacja przestarzałych informacji
- Propozycje ujednolicenia formatowania

## Konfiguracja agentów dla tego repozytorium

### Rekomendowane etykiety (labels)

Warto utworzyć następujące etykiety w repozytorium:
- `automation` - zadania do automatyzacji
- `agent-review` - zadania wymagające przeglądu przez agenta
- `documentation` - zadania związane z dokumentacją
- `validation` - zadania walidacyjne

### Przykładowa konfiguracja workflow

Utwórz plik `.github/workflows/validate-syllabi.yml`:

```yaml
name: Walidacja sylabusów

on:
  pull_request:
    paths:
      - '**.md'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Sprawdź strukturę plików
        run: |
          echo "Sprawdzanie struktury sylabusów..."
          # Sprawdź czy wszystkie pliki .md mają wymagane sekcje
          
      - name: Walidacja linków
        run: |
          echo "Sprawdzanie poprawności linków..."
          # Sprawdź czy wszystkie linki są aktualne
```

## Najlepsze praktyki

1. **Dokumentuj zmiany**: Zawsze opisuj co agent ma zrobić
2. **Testuj lokalnie**: Przed delegowaniem, sprawdź czy zadanie jest jasno zdefiniowane
3. **Monitoruj wyniki**: Regularnie sprawdzaj logi i wyniki działania agentów
4. **Zabezpieczaj tokeny**: Nigdy nie commituj tokenów dostępu do repozytorium
5. **Rozpocznij od prostych zadań**: Najpierw przetestuj na mniejszych zadaniach

## Zaawansowane możliwości

### Integracja z IDE

GitHub Copilot może być zintegrowany z edytorami:
- Visual Studio Code
- JetBrains IDEs
- Neovim
- Vim

### Automatyczne review

Agenty mogą automatycznie:
- Sugerować poprawki w pull requestach
- Sprawdzać zgodność ze standardami repozytorium
- Identyfikować potencjalne problemy

## Bezpieczeństwo

⚠️ **Ważne uwagi dotyczące bezpieczeństwa:**

1. Używaj tokenów z ograniczonymi uprawnieniami
2. Regularnie rotuj tokeny dostępu
3. Nie udostępniaj tokenów w publicznych miejscach
4. Korzystaj z GitHub Secrets dla workflow
5. Monitoruj aktywność w repozytorium

## Wsparcie i pomoc

- **Dokumentacja GitHub Copilot**: https://docs.github.com/en/copilot
- **GitHub CLI**: https://cli.github.com/
- **GitHub API**: https://docs.github.com/en/rest
- **GitHub Actions**: https://docs.github.com/en/actions

## Feedback

Jeśli masz pytania lub sugestie dotyczące delegowania zadań do agentów, utwórz issue w tym repozytorium z etykietą `question` lub `enhancement`.
