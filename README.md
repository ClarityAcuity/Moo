# Note

## Direnv

```bash
direnv allow
```

## venv

```bash
python -m venv .venv                      
source .venv/bin/activate
```

## ta-lib (homebrew)

```bash
brew install ta-lib
export TA_INCLUDE_PATH="$(brew --prefix ta-lib)/include"
export TA_LIBRARY_PATH="$(brew --prefix ta-lib)/lib"
```

## nix tab-lib (not setup yet)

To fix: venv pip / poetry still not found ta-lib

```bash
export NIXPKGS_ALLOW_UNSUPPORTED_SYSTEM=1
export PREFIX=(nix eval - f '<nixpkgs>' --raw ta-lib)
export TA_INCLUDE_PATH="$PREFIX/include"
export TA_LIBRARY_PATH="$PREFIX/lib"
```
